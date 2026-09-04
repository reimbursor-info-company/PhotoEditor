from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QScrollArea, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QScrollArea, QLabel
from PIL import Image
import io

class PhotoEditorUI(QMainWindow):
    def __init__(self, processor):
        super().__init__()
        self.processor = processor
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Photo Editor Pro")
        self.setGeometry(100, 100, 1200, 800)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout()
        
        # Image display
        self.image_label = QLabel()
        self.image_label.setMinimumSize(600, 600)
        self.image_label.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0;")
        layout.addWidget(self.image_label)
        
        # Controls panel
        controls_layout = QVBoxLayout()
        
        # Load button
        load_btn = QPushButton("Load Image")
        load_btn.clicked.connect(self.load_image)
        controls_layout.addWidget(load_btn)
        
        # Color Grading
        controls_layout.addWidget(QLabel("Color Grading"))
        self.saturation_slider = QSlider(Qt.Orientation.Horizontal)
        self.saturation_slider.setRange(0, 200)
        self.saturation_slider.setValue(100)
        self.saturation_slider.sliderMoved.connect(lambda: self.apply_filter('color_grading'))
        controls_layout.addWidget(QLabel("Saturation"))
        controls_layout.addWidget(self.saturation_slider)
        
        self.contrast_slider = QSlider(Qt.Orientation.Horizontal)
        self.contrast_slider.setRange(50, 200)
        self.contrast_slider.setValue(100)
        self.contrast_slider.sliderMoved.connect(lambda: self.apply_filter('color_grading'))
        controls_layout.addWidget(QLabel("Contrast"))
        controls_layout.addWidget(self.contrast_slider)
        
        self.brightness_slider = QSlider(Qt.Orientation.Horizontal)
        self.brightness_slider.setRange(-100, 100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.sliderMoved.connect(lambda: self.apply_filter('color_grading'))
        controls_layout.addWidget(QLabel("Brightness"))
        controls_layout.addWidget(self.brightness_slider)
        
        # Lens Distortion
        controls_layout.addWidget(QLabel("Lens Distortion"))
        self.distortion_slider = QSlider(Qt.Orientation.Horizontal)
        self.distortion_slider.setRange(-50, 50)
        self.distortion_slider.setValue(0)
        self.distortion_slider.sliderMoved.connect(lambda: self.apply_filter('lens_distortion'))
        controls_layout.addWidget(self.distortion_slider)
        
        # Noise Reduction
        controls_layout.addWidget(QLabel("Noise Reduction"))
        self.noise_slider = QSlider(Qt.Orientation.Horizontal)
        self.noise_slider.setRange(0, 100)
        self.noise_slider.setValue(0)
        self.noise_slider.sliderMoved.connect(lambda: self.apply_filter('noise_reduction'))
        controls_layout.addWidget(self.noise_slider)
        
        # Sharpening
        controls_layout.addWidget(QLabel("Sharpening"))
        self.sharpening_slider = QSlider(Qt.Orientation.Horizontal)
        self.sharpening_slider.setRange(0, 100)
        self.sharpening_slider.setValue(0)
        self.sharpening_slider.sliderMoved.connect(lambda: self.apply_filter('sharpening'))
        controls_layout.addWidget(self.sharpening_slider)
        
        # HDR Tone Mapping
        controls_layout.addWidget(QLabel("HDR Tone Mapping"))
        self.exposure_slider = QSlider(Qt.Orientation.Horizontal)
        self.exposure_slider.setRange(50, 200)
        self.exposure_slider.setValue(100)
        self.exposure_slider.sliderMoved.connect(lambda: self.apply_filter('hdr_tone_mapping'))
        controls_layout.addWidget(QLabel("Exposure"))
        controls_layout.addWidget(self.exposure_slider)
        
        self.gamma_slider = QSlider(Qt.Orientation.Horizontal)
        self.gamma_slider.setRange(50, 200)
        self.gamma_slider.setValue(100)
        self.gamma_slider.sliderMoved.connect(lambda: self.apply_filter('hdr_tone_mapping'))
        controls_layout.addWidget(QLabel("Gamma"))
        controls_layout.addWidget(self.gamma_slider)
        
        # Save button
        save_btn = QPushButton("Save Image")
        save_btn.clicked.connect(self.save_image)
        controls_layout.addWidget(save_btn)
        
        controls_layout.addStretch()
        
        layout.addLayout(controls_layout)
        central_widget.setLayout(layout)
    
    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.processor.load_image(file_path)
            self.display_image()
    
    def display_image(self):
        img = self.processor.get_current_image()
        if img:
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            pixmap = QPixmap()
            pixmap.loadFromData(img_bytes.getvalue())
            scaled_pixmap = pixmap.scaledToWidth(600)
            self.image_label.setPixmap(scaled_pixmap)
    
    def apply_filter(self, filter_name):
        if filter_name == 'color_grading':
            self.processor.apply_color_grading(
                self.saturation_slider.value() / 100.0,
                self.contrast_slider.value() / 100.0,
                self.brightness_slider.value()
            )
        elif filter_name == 'lens_distortion':
            self.processor.apply_lens_distortion(self.distortion_slider.value() / 100.0)
        elif filter_name == 'noise_reduction':
            self.processor.apply_noise_reduction(self.noise_slider.value() / 100.0)
        elif filter_name == 'sharpening':
            self.processor.apply_sharpening(self.sharpening_slider.value() / 100.0)
        elif filter_name == 'hdr_tone_mapping':
            self.processor.apply_hdr_tone_mapping(
                self.exposure_slider.value() / 100.0,
                self.gamma_slider.value() / 100.0
            )
        
        self.display_image()
    
    def save_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPEG Files (*.jpg)")
        if file_path:
            self.processor.save_image(file_path)
