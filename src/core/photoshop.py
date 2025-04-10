import subprocess
from pathlib import Path
from src.config.settings import Settings


class Photoshop:
    def process_mockup(self, ps_path: Path, svg_path: str, export_path: str):
        print(f"[+] Processing: {psd_path.name}")

        jsx_path = Settings.JSX_DIR / "apply.jsx"

        subprocess.run([
            "c:\\Program Files\\Adobe\\Adobe Photoshop 2025\\Photoshop.exe",
            "-r"
            str(jsx_path),
        ])