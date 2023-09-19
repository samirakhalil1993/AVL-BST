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
        self._root = self._insert_rec(self._root, element)
    
    def _insert_rec(self, node, element):
        if node is None:
            # Create a new node with the given element
            new_node = self.Node()
            new_node.data = element
            new_node.height = 1  # New node has a height of 1
            return new_node
        
        if element < node.data:
            # Insert into the left subtree
            node.left = self._insert_rec(node.left, element)
        elif element > node.data:
            # Insert into the right subtree
            node.right = self._insert_rec(node.right, element)
        else:
            # Duplicate element, do nothing (no duplicates allowed)
            return node

        # Update the height of this node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Perform AVL balancing
        return self._balance(node)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, node):
        # Get the balance factor
        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            if self._balance_factor(node.left) >= 0:
                # Left Left Case
                return self._rotate_right(node)
            else:
                # Left Right Case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            if self._balance_factor(node.right) <= 0:
                # Right Right Case
                return self._rotate_left(node)
            else:
                # Right Left Case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root


    def remove(self, element):
        """Tar bort det efterfr ̊agade elementet
        i trädet om det finns."""
        if self.find(element):  # Check if the element exists in the tree
            self._root = self._remove_rec(self._root, element)

    def _remove_rec(self, node, element):
        if node is None:
            return node

        if element < node.data:
            # Element to be deleted is in the left subtree
            node.left = self._remove_rec(node.left, element)
        elif element > node.data:
            # Element to be deleted is in the right subtree
            node.right = self._remove_rec(node.right, element)
        else:
            # Node with the element to be deleted found

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.data = self._get_min_value(node.right)
            node.right = self._remove_rec(node.right, node.data)

            # Update the height of this node
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # Perform AVL balancing
            return self._balance(node)

    def _get_min_value(self, node):
        """Helper function to find the minimum value node in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    # ... (rest of the code, including balancing methods)
        
    def find(self, element):
        """Letar upp det efterfr ̊agade elementet
        i tr ̈adet. Returnerar True om det finns, False om det inte finns."""
        return self._find_rec(self._root, element)

    def _find_rec(self, node, element):
        if node is None:
            # Element is not found
            return False
        elif element == node.data:
            # Element found
            return True
        elif element < node.data:
            # Search in the left subtree
            return self._find_rec(node.left, element)
        else:
            # Search in the right subtree
            return self._find_rec(node.right, element)

    def pre_order_walk(self):
        """Traverserar tr ̈adet enligt principen pre
        order och l ̈agger till varje nods v ̈arde i listan."""
        result = []
        self._pre_order_rec(self._root, result)
        return result

    def _pre_order_rec(self, node, result):
        if node is not None:
            # Process the current node (add its value to the result list)
            result.append(node.data)
            
            # Recursively traverse the left subtree
            self._pre_order_rec(node.left, result)
            
            # Recursively traverse the right subtree
            self._pre_order_rec(node.right, result)

    def in_order_walk(self):
        """Traverserar tr ̈adet enligt principen in
        order och l ̈agger till varje nods v ̈arde i listan."""
        result = []
        self._in_order_rec(self._root, result)
        return result

    def _in_order_rec(self, node, result):
        if node is not None:
            # Recursively traverse the left subtree
            self._in_order_rec(node.left, result)
            
            # Process the current node (add its value to the result list)
            result.append(node.data)
            
            # Recursively traverse the right subtree
            self._in_order_rec(node.right, result)

    def post_order_walk(self):
        """Traverserar tr ̈adet enligt principen post
        order och l ̈agger till varje nods v ̈arde i listan."""
        result = []
        self._post_order_rec(self._root, result)
        return result

    def _post_order_rec(self, node, result):
        if node is not None:
            # Recursively traverse the left subtree
            self._post_order_rec(node.left, result)
            
            # Recursively traverse the right subtree
            self._post_order_rec(node.right, result)
            
            # Process the current node (add its value to the result list)
            result.append(node.data)

    def get_tree_height(self):
        """Returnerar h ̈ojden p ̊a tr ̈adet. Om tr ̈adet
         ̈ar tomt returnerar ni -1."""
        if self._root is None:
            return -1
        return self._get_tree_height_rec(self._root)

    def _get_tree_height_rec(self, node):
        if node is None:
            return 0
        left_height = self._get_tree_height_rec(node.left)
        right_height = self._get_tree_height_rec(node.right)
        return 1 + max(left_height, right_height)

    def get_min(self):
        """Returnerar det minsta v ̈ardet i tr ̈adet."""
        if self._root is None:
            raise ValueError("The tree is empty")
        return self._get_min_rec(self._root)

    def _get_min_rec(self, node):
        if node.left is None:
            return node.data
        return self._get_min_rec(node.left)


    def get_max(self):
        """Returnerar det st ̈orsta v ̈ardet i tr ̈adet."""
        if self._root is None:
            raise ValueError("The tree is empty")
        return self._get_max_rec(self._root)

    def _get_max_rec(self, node):
        if node.right is None:
            return node.data
        return self._get_max_rec(node.right)

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
