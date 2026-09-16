import gradio as gr
from PIL import Image
from core.engine import ShieldPixEngine

engine = ShieldPixEngine()

def process_image(input_img, preset, custom_epsilon, custom_steps):
    if input_img is None:
        return None, 'Please upload an image first.'
    if preset == 'Balanced (Recommended)':
        epsilon, steps = 0.02, 25
    elif preset == 'High Protection':
        epsilon, steps = 0.04, 35
    else:
        epsilon, steps = float(custom_epsilon), int(custom_steps)
    protected_img, ssim_score = engine.protect_image(input_img, output_path=None, epsilon=epsilon, steps=steps)
    return protected_img, f'Protection Applied Successfully! Quality Score: {ssim_score:.4f}'

with gr.Blocks(title='ShieldPix') as demo:
    gr.Markdown('# 🛡️ ShieldPix: AI Protection Tool')
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type='pil', label='Upload Image')
            preset_dropdown = gr.Dropdown(choices=['Balanced (Recommended)', 'High Protection', 'Custom'], value='Balanced (Recommended)', label='Protection Preset')
            epsilon_slider = gr.Slider(0.01, 0.08, 0.02, step=0.01, label='Epsilon')
            steps_slider = gr.Slider(10, 50, 25, step=5, label='Steps')
            protect_btn = gr.Button('Protect', variant='primary')
        with gr.Column():
            output_image = gr.Image(type='pil', label='Protected Image')
            status_output = gr.Textbox(label='Status')
    protect_btn.click(process_image, inputs=[input_image, preset_dropdown, epsilon_slider, steps_slider], outputs=[output_image, status_output])

if __name__ == '__main__':
    demo.launch()
