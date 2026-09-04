import sys
from PyQt6.QtWidgets import QApplication
from ui import PhotoEditorUI
from image_processor import ImageProcessor

def main():
    app = QApplication(sys.argv)
    processor = ImageProcessor()
    window = PhotoEditorUI(processor)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
