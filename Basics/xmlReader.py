# -*- coding: utf-8 -*-
"""
Code for XML data Extraction
"""

import xml.sax

class DrawingHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.topx = ""
      self.topy = ""
      self.botx = ""
      self.boty = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "drawing":
         print("*****Drawing*****")
         title = attributes["type"]
         print("Type:", title)
         
      if tag == "page":
         print("*****New Page*****")
         title = attributes["pg"]
         print("Pg.:", title)
         
      if tag == "tab":
         print("*****New Table*****")
         title = attributes["num"]
         print("Table No.:", title)
      

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "topx":
         print("TopX:", self.topx)
      elif self.CurrentData == "topy":
         print("TopY:", self.topy)
      elif self.CurrentData == "botx":
         print("BotX:", self.botx)
      elif self.CurrentData == "boty":
         print("BotY:", self.boty)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "topx":
         self.topx = content
      elif self.CurrentData == "topy":
         self.topy = content
      elif self.CurrentData == "botx":
         self.botx = content
      elif self.CurrentData == "boty":
         self.boty = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)
   # override the default ContextHandler
   Handler = DrawingHandler()
   parser.setContentHandler(Handler)
   
   parser.parse("DrawingMaster.xml")
   
   
"""
XML structure
-------------
<drawing type="">
	<teeth num="">
		<page pg="">
			<tab num="">
				<topx>data</topx>
				<topy>data</topy>
				<botx>data</botx>
				<boty>data</boty>
			</tab>
        </page>
    </teeth>
</drawing>
"""