# -*- coding: utf-8 -*-
"""
Code for OCR using Tesseract
"""

import re
import io
import pandas as pd
from PIL import Image
import pytesseract
from wand.image import Image as wi
import getData

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\admin\Desktop\OCR\jTessBoxEditorFX\tesseract-ocr\tesseract.exe'
outfile="out.xlsx"

class Extractor():
    def __init__(self, filename):
        self.df=self.load_excel(outfile)
        self.table=[]
        self.outFile=outfile
        self.cond = self.teethNo = self.drawNo = self.orderNo = ''
        self.imageBlobs=self.convertPDF(filename)
        self.mapper()
    
    def load_excel(self, filename):
        df=pd.read_excel(filename)
        return df
    
    def sendToFile(self):
        self.df.to_excel(self.outFile,index=False)
    
    def convertPDF(self, filename):
        pdf = wi(filename= filename, resolution = 300)
        pdfImage = pdf.convert('jpeg')
        blobs=[]
        for img in pdfImage.sequence:
            imgPage = wi(image = img)
            blobs.append(imgPage.make_blob('jpeg'))
            if (pdfImage.sequence.index(img)==0):
                self.initialize(blobs[0])
        return blobs
    
    def initialize(self, imgBlob):
        
        if self.df.iloc[-1,0]==None:
            idt=1
        else:
            idt=self.df.iloc[-1,0] + 1
            
        
        im=Image.open(io.BytesIO(imgBlob))
        im1 = im.crop((237, 297, 1186, 558))
        text = pytesseract.image_to_string(im1, lang = 'eng')
        for line in text.split('\n'):
            match1 = re.search('Drawing No.: (\d{12})(\d{2})', line)
            if match1:
                self.drawNo = match1.group(1)
                self.teethNo = match1.group(2)
            match2 = re.search('Order No.: (.*)', line)
            if match2:
                self.orderNo = match2.group(1)
            match3 = re.search('(Hard|Soft)', line)
            if match3:
                self.cond = match3.group(1)
                
        self.table.extend([idt, self.drawNo, self.teethNo, self.cond, self.orderNo])
        return
            
    def mapper(self):
        pg1=[]
        pg2=[]
        pg1,pg2=getData.getData(self.cond, self.teethNo, pg1, pg2)
        self.OCR(pg1, pg2)
            
    def OCR(self, arr1, arr2):
        impg1=Image.open(io.BytesIO(self.imageBlobs[0]))
        impg2=Image.open(io.BytesIO(self.imageBlobs[1]))
        for i in arr1:
            im1=impg1.crop((i[0],i[1],i[2],i[3]))
            
            if i==arr1[0]:
                im1 = im1.rotate(270, expand=True)
                #im1.save("cropped%s.jpg" % i)
            
            text = pytesseract.image_to_string(im1, lang = 'eng')
            if i==arr1[0]:
                self.table.extend([text])
            """    
            print('----1----')
            print(i)
            print(text)
            """
            
            
        for i in arr2:
            im1=impg2.crop((i[0],i[1],i[2],i[3]))
            #im1.save("cropped%s.jpg" % i)
            
            text = pytesseract.image_to_string(im1, lang = 'eng', config='digits')
            if i==arr2[3]:
                a=text.split('\n')
                b=a[0].split(' ')
                c=a[1].split(' ')
                self.table.extend([b[0],c[0],b[1],c[1]])
            """    
            print('----2----')
            print(i)
            print(text)
            """
            
        self.makeTable()
            
    def makeTable(self):
        self.df.loc[len(self.df)]=self.table
        self.sendToFile()
        print("Done")
        
def main(filename):
    Extractor(filename)

if __name__ == "__main__":
    main("newdoc.pdf")


