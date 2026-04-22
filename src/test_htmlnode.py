import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("tag", "value", ["child1", "child2"], {
    "href": "https://www.google.com",
    "target": "_blank",
})
        expect = " tag: tag\n value: value\n children: ['child1', 'child2']\n props: href=https://www.google.com target=_blank"
        self.assertEqual(repr(node), expect)

    def test_props_to_html(self):
        churros = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        test = churros.props_to_html()
        expect = " href=https://www.google.com target=_blank"

        self.assertEqual(test, expect)
    
    def test_to_HTML(self):
        churros = LeafNode("a", "Hello, World!",props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        expect = "<a href=https://www.google.com>Hello, World!<\\a>"
        self.assertEqual(churros.to_html(), expect)
    
    def test_repr_LeafNode(self):
        node = LeafNode("tag", "value", props={
    "href": "https://www.google.com",
    "target": "_blank",
})
        expect = "tag: tag\nvalue: value\nprops: href=https://www.google.com target=_blank"
        self.assertEqual(repr(node), expect)

if __name__ == "__main__":
    unittest.main()