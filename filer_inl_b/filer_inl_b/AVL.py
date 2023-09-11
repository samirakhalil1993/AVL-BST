class AVL:
    class Node:
        def __init__(self):
            self.left = None
            self.right = None
            self.data = None
            self.height = None

    def __init__(self):
        self._root = None
        self.node_id = 0  # ONLY USED WITHIN to_graphviz()!
        pass

    def insert(self, element):
        """L ̈agger till ett element i tr ̈adet.
        Inga duplicerade element skall till ̊atas."""
        pass

    def remove(self, element):
        """Tar bort det efterfr ̊agade elementet
        i trädet om det finns."""
        pass
        
    def find(self, element):
        """Letar upp det efterfr ̊agade elementet
        i tr ̈adet. Returnerar True om det finns, False om det inte finns."""
        pass

    def pre_order_walk(self):
        """Traverserar tr ̈adet enligt principen pre
        order och l ̈agger till varje nods v ̈arde i listan."""
        pass

    def in_order_walk(self):
        """Traverserar tr ̈adet enligt principen in
        order och l ̈agger till varje nods v ̈arde i listan."""
        pass

    def post_order_walk(self):
        """Traverserar tr ̈adet enligt principen post
        order och l ̈agger till varje nods v ̈arde i listan."""
        pass

    def get_tree_height(self):
        """Returnerar h ̈ojden p ̊a tr ̈adet. Om tr ̈adet
         ̈ar tomt returnerar ni -1."""
        pass

    def get_min(self):
        """Returnerar det minsta v ̈ardet i tr ̈adet."""
        pass

    def get_max(self):
        """Returnerar det st ̈orsta v ̈ardet i tr ̈adet."""
        pass

    def to_graphviz_rec(self, data, current):
        my_node_id = self.node_id
        data += "\t" + str(my_node_id) + \
            " [label=\"" + str(current.data) + "\"];\n"
        self.node_id += 1
        if current.left is not None:
            data += "\t" + str(my_node_id) + " -> " + \
                str(self.node_id) + " [color=blue];\n"
            data = self.to_graphviz_rec(data, current.left)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" + str(my_node_id) + " -> " + \
                str(self.node_id) + " [style=invis];\n"

        self.node_id += 1
        if current.right is not None:
            data += "\t" + str(my_node_id) + " -> " + \
                str(self.node_id) + " [color=red];\n"
            data = self.to_graphviz_rec(data, current.right)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\t" + str(my_node_id) + " -> " + \
                str(self.node_id) + " [style=invis];\n"

        return data

    def to_graphviz(self):
        data = ""
        if self._root is not None:
            self.node_id = 0
            data += "digraph {\n"
            data += "\tRoot [shape=plaintext];\n"
            data += "\t\"Root\" -> 0 [color=black];\n"
            data = self.to_graphviz_rec(data, self._root)
            data += "}\n"
        return data
