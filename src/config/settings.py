from pathlib import Path

class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    ASSETS_DIR = BASE_DIR / "assets"
    INPUTS_DIR = ASSETS_DIR / "inputs"
    TEMPLATES_DIR = ASSETS_DIR / "templates"
    EXPORTS_DIR = BASE_DIR / "exports"
    JSX_DIR = BASE_DIR / "jsx"

    FRONT_PSD = TEMPLATES_DIR / "front.psd"
    BACK_PSD = TEMPLATES_DIR / "back.psd"