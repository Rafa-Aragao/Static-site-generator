from enum import Enum

class TextType(Enum):
    plain_text = "plain"
    bold_text = "bold"
    italic_text = "italic"
    code_text = "code"
    link_format = "link"
    image_format = "image"

class TextNode():
    def __init__(self):
        self.text = None
        self.text_type = TextType()
        self.url = None
        
    def __eq__(self, value):
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"