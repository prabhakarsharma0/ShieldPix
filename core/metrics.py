from skimage.metrics import structural_similarity as ssim

def check_ssim_quality(orig_tensor, adv_tensor) -> float:
    """Calculates Structural Similarity Index (SSIM) between original and protected tensors."""
    orig_np = orig_tensor.squeeze(0).cpu().detach().permute(1, 2, 0).numpy()
    adv_np = adv_tensor.squeeze(0).cpu().detach().permute(1, 2, 0).numpy()
    
    score, _ = ssim(orig_np, adv_np, full=True, channel_axis=2, data_range=1.0)
    return float(score)
