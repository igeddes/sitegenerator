from typing import Optional, Dict, List

class HTMLNode:
    def __init__(self, 
        tag: Optional[str] = None, 
        value: Optional[str] = None, 
        children: Optional[List[object]] = None,
        props: Optional[Dict[str, str]] = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f'HTMLNode({", ".join(
            [
                f'{key}="{value}"'
                for key, value in self.__dict__.items()
                if value is not None and isinstance(value, str)
            ] + [
                f"{key}={value}"
                for key, value in self.__dict__.items()
                if value is not None and not isinstance(value, str)
            ]
        )})'
    



if __name__ == "__main__":
    aa = HTMLNode("apple", "orange", [], {"tank": "empty", "distance": "no"})
    print(aa)
