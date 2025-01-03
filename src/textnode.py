from enum import Enum
from typing import Optional, Union


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

    @classmethod
    def is_valid_value(cls, val):
        return val in [tt.value for tt in cls]


class TextNode:
    def __init__(
        self, text: str, text_type: Union[str, TextType], url: Optional[str] = None
    ) -> None:
        self.text = text
        if isinstance(text_type, str) and TextType.is_valid_value(text_type):
            self.text_type = TextType(text_type)
        elif isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            raise ValueError(f"Invalid parameter ({text_type}) provided for text_type")
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return (
            ", ".join(
                [
                    item
                    for item in (
                        f"TextNode({self.text}",
                        self.text_type.value,
                        self.url,
                    )
                    if item is not None
                ]
            )
            + ")"
        )
