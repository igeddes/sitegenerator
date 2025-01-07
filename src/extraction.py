from htmlnode import LeafNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: TextNode, delimiter: str, text_type: TextType):
    
    result = []
    for node in old_nodes:
        text_types = (node.text_type, text_type)
        for count, section in enumerate(node.text.split(delimiter)):
            result.append(TextNode(section, text_types[count%2]))
    return result

def main():
    pass

if __name__ == "__main__":
    main()