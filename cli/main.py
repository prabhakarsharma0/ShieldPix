import click
from rich.console import Console
from core.engine import ShieldPixEngine

console = Console()

@click.group()
def cli():
    """ShieldPix: Adversarial Image Sanitizer CLI"""
    pass

@cli.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True), help="Input image file path.")
@click.option('--output', '-o', required=True, type=click.Path(), help="Output protected image file path.")
@click.option('--epsilon', '-e', default=0.02, type=float, help="Noise intensity bound (default: 0.02).")
@click.option('--steps', '-s', default=25, type=int, help="Optimization steps (default: 25).")
def sanitize(input, output, epsilon, steps):
    """Immunize an image against unauthorized AI scrapers and models."""
    console.print("[bold blue][*] ShieldPix Engine Initializing...[/bold blue]")
    
    engine = ShieldPixEngine()
    
    console.print("[yellow][*] Applying EOT Adversarial Protection...[/yellow]")
    ssim_score = engine.protect_image(input, output, epsilon=epsilon, steps=steps)
        
    console.print(f"[bold green][+] Protection Complete![/bold green]")
    console.print(f"[bold white]Saved to:[/bold white] {output}")
    console.print(f"[bold cyan]SSIM Quality Score:[/bold cyan] {ssim_score:.4f}")

if __name__ == "__main__":
    cli()
