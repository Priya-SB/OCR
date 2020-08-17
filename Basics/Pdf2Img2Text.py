# -*- coding: utf-8 -*-
"""
Code to convert a PDF doc into Images and run tesseract OCR on it
"""

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\admin\Desktop\OCR\jTessBoxEditorFX\tesseract-ocr\tesseract.exe'

pdf = wi(filename = "mypdf.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

for txt in recognized_text:
    print(txt)