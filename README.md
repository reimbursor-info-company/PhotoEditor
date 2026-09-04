# Photo Editor Pro

![License](https://img.shields.io/badge/License-Professional-blue.svg)
![Platform](https://img.shields.io/badge/Platform-macOS%2011+-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.9+-3776ab.svg?logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-1.80+-ce422b.svg?logo=rust&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Release](https://img.shields.io/badge/Release-v2.0-blueviolet.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
![Maintenance](https://img.shields.io/badge/Maintenance-Active-green.svg)

Professional-grade photo editing with native performance

## Overview

Photo Editor Pro is a lightweight yet powerful image editing application designed for photographers and creative professionals. Built with a modern Python GUI and high-performance Rust backend, it delivers professional-grade image processing with real-time preview capabilities.

## Features

### Advanced Filters

| Filter | Description | Use Case |
|--------|-------------|----------|
| **Color Grading** | Fine-tune saturation, contrast, and brightness | Creative color correction |
| **Lens Distortion** | Correct or apply barrel/pincushion effects | Lens correction or artistic effects |
| **Noise Reduction** | Intelligent noise removal preserving detail | High-ISO photo cleanup |
| **Sharpening** | Enhance clarity with precision control | Image enhancement and detail recovery |
| **HDR Tone Mapping** | Professional tone mapping with exposure/gamma | Dynamic range processing |

### Performance

- Native Rust Backend: Compiled to ARM64 machine code for optimal performance
- Real-Time Preview: Instant filter feedback with slider adjustment
- Efficient Processing: Handles large images without lag
- Low Memory Footprint: Optimized for modern Mac systems
- Intuitive PyQt6 interface with non-destructive editing

## System Requirements

| Requirement | Specification |
|------------|--------------|
| OS | macOS 11.0+ (ARM64/Apple Silicon) |
| Python | 3.9 or higher |
| RAM | 4GB minimum (8GB recommended) |
| Disk | 100MB free space |
| Architecture | Apple Silicon (M1/M2/M3 or newer) |

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/reimbursor-info-company/PhotoEditor.git
cd PhotoEditor
```

### 2. Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### 3. Install Dependencies
```bash
cd src
pip install -r requirements.txt
```

### 4. Run Application
```bash
python3 main.py
```

## Usage

### Basic Workflow

Load Image: Click "Load Image" button and select PNG, JPEG, BMP, GIF, TIFF, or WebP

Apply Filters: Adjust sliders for desired effect and watch real-time preview updates. Stack multiple filters for complex edits.

Save Result: Click "Save Image" and choose output format and location. Exports as PNG with full quality.

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| ESC | Exit application |
| CMD+O | Open image |
| CMD+S | Save image |

## Performance

Photo Editor Pro achieves professional-grade performance through native Rust compilation with SIMD optimization, vectorized operations for faster processing, memory-efficient streaming image processing, and multi-threaded CPU core utilization.

### Benchmarks (M1 Pro)

- Color Grading: ~50ms for 4K image
- Noise Reduction: ~150ms for 4K image
- HDR Tone Mapping: ~100ms for 4K image

## Architecture

The application uses a layered architecture: PyQt6 GUI layer handles real-time preview and user controls, the image processor interface layer manages data flow, and the Rust native extension (.so) executes all filter operations in compiled machine code for maximum performance.

Filter implementations include:
- color_grading(): Saturation, contrast, and brightness adjustment
- lens_distortion(): Radial distortion effects
- noise_reduction(): 3x3 kernel averaging denoising
- sharpening(): Unsharp mask with Laplacian kernel
- hdr_tone_mapping(): Gamma correction and exposure adjustment

## File Format Support

### Input Formats

PNG, JPEG/JPG, BMP, GIF, TIFF, WebP, ICO, PNM

### Output Formats

PNG (Default), JPEG (via save dialog)

## Project Structure

```
|── main.py
├── ui.py
├── image_processor.py
├── requirements.txt
└── photo_plugins.cpython-39-darwin.so
```

## Troubleshooting

### Application Won't Start

```bash
python3 --version  # Should be 3.9+
pip list | grep -E "PyQt6|Pillow"
```

### Filter Not Responding

- Ensure image is loaded
- Try with smaller image first
- Check available system memory

### Performance Issues

- Reduce image resolution
- Close other applications
- Check available disk space

## License

OperSource Edition

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

Built with dedication for photographers who demand professional tools
