from textnode import TextNode
from textnode import TextType

def main():
    churros = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    print(churros)

main()
