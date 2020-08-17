# -*- coding: utf-8 -*-
"""
Code to extract text from an Image using tesseract
"""

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\admin\Desktop\OCR\jTessBoxEditorFX\tesseract-ocr\tesseract.exe'

im = Image.open("myimg.jpg")
text = pytesseract.image_to_string(im, lang = 'eng')

print(text)