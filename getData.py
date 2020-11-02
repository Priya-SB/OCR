# -*- coding: utf-8 -*-
"""
Code to retrieve data from XML file
"""

import xml.etree.cElementTree as ET

xml="DrawingMaster.xml"
tree= ET.ElementTree(file=xml)
root = tree.getroot()

def getData(cond,teeth,arr1,arr2):
    
    for i in root:
        if (i.get('type') == cond):
            for k in i:
                if (k.get('num') == teeth):
                    for l in k:
                        if (l.get('pg') == '1'):
                            for m in l:
                                strlist = (m.text).split (",")
                                strlist = list(map(int, strlist))
                                arr1.append(strlist)
                        else:
                            for m in l:
                                strlist = (m.text).split (",")
                                strlist = list(map(int, strlist))
                                arr2.append(strlist)
                                
    return arr1,arr2