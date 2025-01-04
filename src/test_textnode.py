import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_alternate_text_types(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_providing_null_url(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_mismatching_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_mismatching_texttype(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_mismatching_url(self):
        node = TextNode("This is a text node", "text", "https://www.works.not")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.works.net")
        self.assertNotEqual(node, node2)

    def test_invalid_texttype_str(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "norman", "https://www.works.not")

    def test_invalid_texttype_obj(self):
        with self.assertRaises(AttributeError):
            TextNode("This is a text node", TextType.NORMAN, "https://www.works.not")


if __name__ == "__main__":
    unittest.main()
