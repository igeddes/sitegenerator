from typing import Optional, Union, Dict, List


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List[object]] = None,
        props: Optional[Dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    @property
    def open_tag(self):
        if props := self.props_to_html():
            return f"<{self.tag} {props}>"
        return f"<{self.tag}>"

    @property
    def close_tag(self):
        if self.tag in [
            "img",
        ]:
            return ""
        return f"</{self.tag}>"

    def tag_data(self, data: Union[str, List[str]]) -> str:
        if isinstance(data, list):
            data = "".join(data)
        return f"{self.open_tag}{data}{self.close_tag}"

    def __repr__(self):
        return f"""HTMLNode({", ".join(
            [
                f'{key}="{value}"'
                for key, value in self.__dict__.items()
                if value is not None and isinstance(value, str)
            ] + [
                f"{key}={value}"
                for key, value in self.__dict__.items()
                if value is not None and not isinstance(value, str)
            ]
        )})"""


class LeafNode(HTMLNode):
    def __init__(
        self, tag: Optional[str], value: str, props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")

        if not self.tag:
            return self.value

        return self.tag_data(self.value)


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: List[object], props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNodes must have a tag")
        if not self.children:
            raise ValueError("ParentNodes must be associated with one or more children")

        return self.tag_data([child.to_html() for child in self.children])


if __name__ == "__main__":
    pass
