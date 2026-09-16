import torch
from torchvision import transforms, models
from PIL import Image
import numpy as np

class ShieldPixEngine:
    def __init__(self, device=None):
        self.device = device if device else ('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT).to(self.device)
        self.model.eval()

    def protect_image(self, input_pil, output_path=None, epsilon=0.02, steps=25):
        if input_pil is None:
            return None, 0.0
        orig_pil = input_pil.convert('RGB')
        orig_w, orig_h = orig_pil.size
        transform_model = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor()])
        img_model_tensor = transform_model(orig_pil).unsqueeze(0).to(self.device)
        delta = torch.zeros_like(img_model_tensor, requires_grad=True)
        optimizer = torch.optim.Adam([delta], lr=0.005)
        for _ in range(steps):
            optimizer.zero_grad()
            adv_input = torch.clamp(img_model_tensor + delta, 0, 1)
            features = self.model(adv_input)
            loss = -torch.mean(torch.abs(features))
            loss.backward()
            optimizer.step()
            with torch.no_grad():
                delta.data = torch.clamp(delta.data, -epsilon, epsilon)
        noise_model = delta.detach().squeeze(0).cpu()
        noise_pil = transforms.ToPILImage()(noise_model)
        noise_full_pil = noise_pil.resize((orig_w, orig_h), Image.Resampling.LANCZOS)
        noise_np = (np.array(noise_full_pil, dtype=np.float32) / 255.0) - 0.5
        noise_np = noise_np * (2 * epsilon)
        orig_np = np.array(orig_pil, dtype=np.float32) / 255.0
        protected_np = np.clip(orig_np + noise_np, 0.0, 1.0)
        protected_img = Image.fromarray((protected_np * 255).astype(np.uint8))
        if output_path:
            protected_img.save(output_path)
        mse = np.mean((orig_np - protected_np) ** 2)
        ssim_score = max(0.0, 1.0 - (mse * 10))
        return protected_img, ssim_score
