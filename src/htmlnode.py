class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f" {list(self.props.keys())[0]}={self.props[list(self.props.keys())[0]]} {list(self.props.keys())[1]}={self.props[list(self.props.keys())[1]]}"

churros = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
print(churros.props_to_html())