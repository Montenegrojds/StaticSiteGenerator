import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(),"")

    def test_one_props(self):
        node = HTMLNode(props={"id":"1234"})
        self.assertEqual(node.props_to_html(), ' id="1234"')

    def test_multiple_props(self):
        node = HTMLNode(props={"id": "1234", "class": "container"})
        result = node.props_to_html()
        self.assertTrue(result== ' id="1234" class="container"' or result==' class="container" id="test"')
if __name__ == "__main__":
    unittest.main()