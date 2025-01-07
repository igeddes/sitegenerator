import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from extraction import split_nodes_delimiter


class TestDecodeTextBlocks(unittest.TestCase):
    def test_code_tag(self):
        node = TextNode("This is text with a `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_result = [
            TextNode('This is text with a ', 'text'), 
            TextNode('code block', 'code'), 
            TextNode(' word.', 'text')
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_bold_tag(self):
        node = TextNode("This is text with a **bold** word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_result = [
            TextNode('This is text with a ', 'text'), 
            TextNode('bold', 'bold'), 
            TextNode(' word.', 'text')
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_italic_tag(self):
        node = TextNode("This is text with an *italic* word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_result = [
            TextNode('This is text with an ', 'text'), 
            TextNode('italic', 'italic'), 
            TextNode(' word.', 'text')
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_embedded_tag(self):
        node = TextNode("This is text with an *italic* word.", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_result = [
            TextNode('This is text with an ', 'bold'), 
            TextNode('italic', 'italic'), 
            TextNode(' word.', 'bold')
        ]
        self.assertEqual(new_nodes, expected_result)

if __name__ == "__main__":
    unittest.main()
