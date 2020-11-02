# -*- coding: utf-8 -*-
"""
Code to insert data into XML file
"""

import xml.etree.cElementTree as ET

xml="Sample.xml"
tree= ET.ElementTree(file=xml)
root = tree.getroot()

def main(cond,pg,teeth,topx,topy,botx,boty):
    
    a = ET.Element("img")
    a.set('cond',cond)
    a.set('pg',pg)
    a.set('teeth',teeth)
    
    tx = ET.Element("topx")
    tx.text = topx
    
    ty = ET.Element("topy")
    ty.text = topy
    
    bx = ET.Element("botx")
    bx.text = botx
    
    by = ET.Element("boty")
    by.text = boty
    
    root.insert(0, a)
    a.insert(0, tx)
    a.insert(1, ty)
    a.insert(2, bx)
    a.insert(3, by)
   
    tree.write(xml)
#ET.dump(root)
