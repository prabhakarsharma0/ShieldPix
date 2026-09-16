import sys
import os

# Core & CLI modules ka path set karo
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cli.main import cli

if __name__ == "__main__":
    cli()
