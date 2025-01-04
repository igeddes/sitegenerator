import unittest
from textnode import TextNode
from translation import text_node_to_html_node


class TestTextToHtml(unittest.TestCase):
    def test_text_tag(self):
        node = TextNode("This is a text node", "text")
        self.assertEqual(
            'This is a text node',
            text_node_to_html_node(node).to_html()
        )
    def test_bold_tag(self):
        node = TextNode("This is a bold node", "bold")
        self.assertEqual(
            '<b>This is a bold node</b>',
            text_node_to_html_node(node).to_html()
        )

    def test_italic_tag(self):
        node = TextNode("This is an italic node", "italic")
        self.assertEqual(
            '<i>This is an italic node</i>',
            text_node_to_html_node(node).to_html()
        )

    def test_code_tag(self):
        aa = TextNode("This is a code node", "code")
        self.assertEqual(
            '<code>This is a code node</code>',
            text_node_to_html_node(aa).to_html()
        )

    def test_link_tag(self):
        node = TextNode("This is a link node", "link", "http://www.google.com")
        self.assertEqual(
            '<a href="http://www.google.com">This is a link node</a>',
            text_node_to_html_node(node).to_html()
        )

    def test_image_tag(self):
        node = TextNode("This is an image node", "image", "images/123.jpg")
        self.assertEqual(
            '<img src="images/123.jpg" alt="This is an image node">',
            text_node_to_html_node(node).to_html()
        )

    def test_undefined_tag(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("This is an invalid node", "fake")
        self.assertTrue(str(context.exception).startswith("Invalid parameter"))
    
if __name__ == "__main__":
    unittest.main()