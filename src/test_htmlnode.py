import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_params(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

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
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()