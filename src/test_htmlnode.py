import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_no_params(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        

    def test_one_positional(self):
        node = HTMLNode("a")
        self.assertEqual('HTMLNode(tag="a")', str(node))

    def test_two_positional(self):
        node = HTMLNode("p", "This is text")
        self.assertEqual('HTMLNode(tag="p", value="This is text")', str(node))

    def test_three_positional(self):
        node1 = HTMLNode()
        node2 = HTMLNode("p", "This is text", [node1])
        self.assertEqual('HTMLNode(tag="p", value="This is text", children=[HTMLNode()])', str(node2))

    def test_all_positional(self):
        node1 = HTMLNode()
        node2 = HTMLNode("p", "This is text", [node1], {"url": "http://boot.dev"})
        self.assertEqual('HTMLNode(tag="p", value="This is text", children=[HTMLNode()], props={\'url\': \'http://boot.dev\'})', str(node2))

    def test_no_children(self):
        node = HTMLNode("p", "This is text", props={"url": "http://boot.dev"})
        self.assertEqual('HTMLNode(tag="p", value="This is text", props={\'url\': \'http://boot.dev\'})', str(node))
    
    def test_only_value(self):
        node = HTMLNode(value="This is text")
        self.assertEqual('HTMLNode(value="This is text")', str(node))

    def test_to_html_not_implemented(self):
        node = HTMLNode(value="This is text")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual('href="https://www.google.com" target="_blank"', node.props_to_html())

class TestHTMLLeafNode(unittest.TestCase):
    def test_no_inputs(self):
        with self.assertRaises(TypeError):
            node = LeafNode()
        
    def test_no_value(self):
        node = LeafNode("p", None, {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'href': 'https://www.google.com'})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_value_only(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Just plain text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        self.assertEqual("Just plain text", node.to_html())

    def test_all_options(self):
        node = LeafNode("img", "This is a picture", {"src": "myimg.jpg", "alt": "Logo"})
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "This is a picture")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"src": "myimg.jpg", "alt": "Logo"})
        self.assertEqual('<img src="myimg.jpg" alt="Logo">This is a picture</img>', node.to_html())


class TestHTMLParentNode(unittest.TestCase):
    def test_no_inputs(self):
        with self.assertRaises(TypeError):
            node = ParentNode()
        
        
    def test_no_tag(self):
        node = ParentNode(None, None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("must have a tag" in str(context.exception))

    def test_no_children1(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("one or more children" in str(context.exception))

    def test_no_children2(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("one or more children" in str(context.exception))


    def test_complex(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(len(node.children), 4)
        self.assertEqual(node.props, None)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_parent_as_child(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("i", []),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(len(node.children), 4)
        self.assertEqual(node.props, None)
    
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertTrue("child nodes should be" in str(context.exception))

if __name__ == "__main__":
    unittest.main()