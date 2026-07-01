from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts_list = node.text.split(delimiter)
            if len(parts_list) % 2 == 0:
                raise Exception("invalid markdown syntax")
    
            for i in range(len(parts_list)):
                if i % 2 == 0:
                    if parts_list[i] != "":
                        new_nodes.append(TextNode(parts_list[i], TextType.TEXT))
                else:
                    if parts_list[i] != "":
                        new_nodes.append(TextNode(parts_list[i], text_type))

    return new_nodes