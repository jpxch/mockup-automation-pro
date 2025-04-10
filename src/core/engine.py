from src.config.settings import Settings
from src.core.photoshop import Photoshop
from src.core.exporter import Exporter


class Engine:
    def __init__(self, svg_path: str):
        self.svg_path = svg_path
        self.ps = Photoshop()
        self.exporter = Exporter()

    def run(self):
        print(f"[+] Running Mockup Auotomation Pro")
        print(f"[+] Using SVG: {self.svg_path}")

        self.ps.process_mockup(Settings.FRONT_PSD, self.svg_path, "front.png")
        self.ps.process_mockup(Settings.BACK_PSD, self.svg_path, "back.png")

        print("[+] Done.")