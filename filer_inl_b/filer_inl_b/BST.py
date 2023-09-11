class BST:
    class Node:
        def __init__(self):
            self.left = None
            self.right = None
            self.data = None

    def __init__(self):
        self._root = None
        self.node_id = 0  # ONLY USED WITHIN to_graphviz()!
        pass

    def insert(self, element):
        """L ̈agger till ett element i tr ̈adet.
        Inga duplicerade element skall till ̊atas."""
        new_node =self.Node()
        new_node.data = element 
        if self._root is None:
            self._root = new_node
            return
        
        # söker reda på var noden ska stoppas in _ iterative lösning 
        current = self._root
        while current != None:
            parent = current 
            if element < current.data:
                current = current.left
            else:
                current = current.right 
        if element < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        

    def remove(self, element):
        """Tar bort det efterfr ̊agade elementet
        i trädet om det finns."""
        # Hjälpfunktion för att hitta och ta bort en nod.
        def remove_node(node, key):
            # Om noden är None eller det element vi letar efter,
            # returnerar vi nodens ersättare (nya noden efter borttagningen).
            if node is None:
                return node
            if key < node.data:
                node.left = remove_node(node.left, key)
            elif key > node.data:
                node.right = remove_node(node.right, key)
            else:
                # Om noden har högst en barnnod, eller inga barn alls.
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Om noden har två barn, hittar vi den minsta noden i
                # högra delträdet (successor) och ersätter den nuvarande noden med successorn.
                node.data = self.find_min(node.right).data
                node.right = remove_node(node.right, node.data)

            return node

        # Anropa hjälpfunktionen för att börja borttagningen från roten.
        self._root = remove_node(self._root, element)

    def find_min(self, node):
            # Hjälpfunktion för att hitta den minsta noden i ett träd.
            current = node
            while current.left is not None:
                current = current.left
            return current
    
        
    def find(self, element):
        """Letar upp det efterfrågade elementet
        i trädet. Returnerar True om det finns, False om det inte finns."""
        return self._find_recursive(self._root, element)

    def _find_recursive(self, node, element):
        """Hjälpfunktion för att rekursivt söka efter ett element i trädet."""
        if node is None:
            return False  # Elementet finns inte i trädet

        if element == node.data:
            return True  # Elementet har hittats i noden

        if element < node.data:
            # Om elementet är mindre än nodens data, sök i vänster delträd
            return self._find_recursive(node.left, element)
        else:
            # Annars, sök i höger delträd
            return self._find_recursive(node.right, element)


    def pre_order_walk(self):
        """Traverserar trädet enligt principen pre-order och lägger till varje nods värde i en lista."""
        result = []
        self._pre_order_recursive(self._root, result)
        return result

    def _pre_order_recursive(self, node, result):
        """Hjälpfunktion för att rekursivt utföra pre-order-traversal och lagra nodvärden i en lista."""
        if node is not None:
            result.append(node.data)  # Lägg till nodens värde i resultatlistan
            self._pre_order_recursive(node.left, result)  # Traversera vänster delträd
            self._pre_order_recursive(node.right, result)  # Traversera höger delträd


    def in_order_walk(self):
        """Traverserar trädet enligt principen in-order och lägger till varje nods värde i en lista."""
        result = []
        self._in_order_recursive(self._root, result)
        return result

    def _in_order_recursive(self, node, result):
        """Hjälpfunktion för att rekursivt utföra in-order-traversal och lagra nodvärden i en lista."""
        if node is not None:
            self._in_order_recursive(node.left, result)  # Traversera vänster delträd
            result.append(node.data)  # Lägg till nodens värde i resultatlistan
            self._in_order_recursive(node.right, result)  # Traversera höger delträd

    def post_order_walk(self):
        """Traverserar trädet enligt principen post-order och returnerar en lista med nodvärden."""
        result = []
        self._post_order_recursive(self._root, result)
        return result

    def _post_order_recursive(self, node, result):
        """Hjälpfunktion för att rekursivt utföra post-order-traversal och lagra nodvärden i en lista."""
        if node is not None:
            self._post_order_recursive(node.left, result)  # Traversera vänster delträd
            self._post_order_recursive(node.right, result)  # Traversera höger delträd
            result.append(node.data)  # Lägg till nodens värde i resultatlistan


    def get_tree_height(self):
        """Returnerar höjden på trädet. Om trädet är tomt returneras -1."""
        return self._get_tree_height_recursive(self._root)

    def _get_tree_height_recursive(self, node):
        """Hjälpfunktion för att rekursivt beräkna höjden på trädet."""
        if node is None:
            return -1
        left_height = self._get_tree_height_recursive(node.left)
        right_height = self._get_tree_height_recursive(node.right)
        return max(left_height, right_height) + 1


    def get_min(self):
        """Returnerar det minsta värdet i trädet."""
        if self._root is None:
            return None
        current = self._root
        while current.left is not None:
            current = current.left
        return current.data


    def get_max(self):
        """Returnerar det största värdet i trädet."""
        if self._root is None:
            return None
        current = self._root
        while current.right is not None:
            current = current.right
        return current.data

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


    def main():
        # Skapa en instans av BST
        bst = BST()

        # Lägg till några element i trädet
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.insert(6)
        bst.insert(8)

        # Utför olika operationer och skriv ut resultaten
        print("In-order traversal:", bst.in_order_walk())
        print("Post-order traversal:", bst.post_order_walk())
        print("Tree height:", bst.get_tree_height())
        print("Min value:", bst.get_min())
        print("Max value:", bst.get_max())
        print("Is 4 in the tree?", bst.find(4))
        print("Is 9 in the tree?", bst.find(9))

    


    if __name__ == '__main__':
        main()
