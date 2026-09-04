from PIL import Image
import photo_plugins
import io

class ImageProcessor:
    def __init__(self):
        self.current_image = None
        self.current_path = None
    
    def load_image(self, path):
        self.current_path = path
        self.current_image = Image.open(path)
        return self.current_image
    
    def save_image(self, path):
        if self.current_image:
            self.current_image.save(path)
            return True
        return False
    
    def apply_color_grading(self, saturation, contrast, brightness):
        if not self.current_image:
            return None
        
        img_bytes = io.BytesIO()
        self.current_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        result = photo_plugins.color_grading(list(img_bytes.getvalue()), saturation, contrast, int(brightness))
        self.current_image = Image.open(io.BytesIO(bytes(result)))
        return self.current_image
    
    def apply_lens_distortion(self, distortion):
        if not self.current_image:
            return None
        
        img_bytes = io.BytesIO()
        self.current_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        result = photo_plugins.lens_distortion(list(img_bytes.getvalue()), distortion)
        self.current_image = Image.open(io.BytesIO(bytes(result)))
        return self.current_image
    
    def apply_noise_reduction(self, strength):
        if not self.current_image:
            return None
        
        img_bytes = io.BytesIO()
        self.current_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        result = photo_plugins.noise_reduction(list(img_bytes.getvalue()), strength)
        self.current_image = Image.open(io.BytesIO(bytes(result)))
        return self.current_image
    
    def apply_sharpening(self, amount):
        if not self.current_image:
            return None
        
        img_bytes = io.BytesIO()
        self.current_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        result = photo_plugins.sharpening(list(img_bytes.getvalue()), amount)
        self.current_image = Image.open(io.BytesIO(bytes(result)))
        return self.current_image
    
    def apply_hdr_tone_mapping(self, exposure, gamma):
        if not self.current_image:
            return None
        
        img_bytes = io.BytesIO()
        self.current_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        result = photo_plugins.hdr_tone_mapping(list(img_bytes.getvalue()), exposure, gamma)
        self.current_image = Image.open(io.BytesIO(bytes(result)))
        return self.current_image
    
    def get_current_image(self):
        return self.current_image
