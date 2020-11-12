from PIL import Image,ImageFilter
import pytesseract 
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def prepare_image(img):
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != img.mode:
        img = img.convert('L')
    return img

def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img

def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (1)
    return (255)


def image_to_text(input_image):
    output_image = 'processed_captcha.png' 
    pass_factor = 90

    img = Image.open(input_image)
    img = prepare_image(img)
    img = remove_noise(img, pass_factor)
    img.save(output_image)
    converted_text = "".join(image_to_string("processed_captcha.png").upper().split())
    return converted_text

    

    