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

    def __repr__(self):
        return f" tag: {self.tag}\n value: {self.value}\n children: {self.children}\n props:{self.props_to_html()}"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props
        
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        if self.props:
            return f"<{self.tag} {list(self.props.keys())[0]}={self.props[list(self.props.keys())[0]]}>{self.value}<\{self.tag}>"
        
        return f"<{self.tag}>{self.value}<\{self.tag}>"
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops:{self.props_to_html()}"