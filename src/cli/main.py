import argparse
from src.config.settings import Settings
from src.core.engine import Engine


def main():
    parser = argparse.ArgumentParser(description="Mockup Automation Pro V2")
    parser.add_argument("--input", required=True, help="Path to SVG input file")

    args = parser.parse_args()

    engine = Engine(svg_path=args.input)
    engine.run()