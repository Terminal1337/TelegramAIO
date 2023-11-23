from PIL import Image
from pytesseract import pytesseract

def parse():
#Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Define path to image
    path_to_image = 'screenshot.png'
#Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
#Open image with PIL
    img = Image.open(path_to_image)
#Extract text from image
    text = pytesseract.image_to_string(img)
    text = str(text).split("answer>")[0]; text = str(text).split("is: ")[1]
    text = text.split(".")[0]
    return text


