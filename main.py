class Node:
    def __init__(self, value):
        """
        Initialising Node obj
        :param value: value of the node
        """
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self, splitter=':'):
        """
        Description of the Node object
        :param splitter: splitter for the report
        :return: str
        """
        return f'<{__name__}.Node object having({self.left} {splitter} {self.value} {splitter} {self.right})>'

    def __str__(self, splitter=':'):
        """
        Function for printing node
        :param splitter: splitter for the string
        :return: str
        """
        return f'{self.left} {splitter} {self.value} {splitter} {self.right}'

    def __del__(self):
        """
        Function for destructing node
        :return: None
        """
        del self.value
        del self.right
        del self.left


class StrBinTree:
    def __init__(self, root):
        """
        Initialising StrBinTree obj
        :param root: start node
        """
        self.root = root

    def add(self, s, node=None):
        """
        Adding new nodes
        :param s: value of new node
        :param node: node of the subtree were we need to add and current node
        :return: None
        """

        if node is None:
            node = self.root
        if s >= node.value:
            if node.right is not None:
                self.add(s, node.right)
            else:
                node.right = Node(s)
        else:
            if node.left is not None:
                self.add(s, node.left)
            else:
                node.left = Node(s)

    def __add__(self, s):
        """
        Function that make support concatenation strBinTree with strings (adding by "+")
        :param s: value
        :return: None
        """
        self.add(self, s)

    def __repr__(self):
        """
        Description of the object
        :return: str
        """
        # TODO: make normal repr
        pass

    def __len__(self):
        # TODO: make len function that returns count or nodes
        pass

    def __str__(self):
        """
        Function for printing strBinTree by layers
        :return: str
        """
        layer_split = self.__slayer_master()

        buff = layer_split

        out = []

        while True:
            list_is = False
            out_buff = []
            for layer in buff:
                if type(layer) is not list:
                    out_buff.append(layer)
                else:
                    list_is = True
                    buff = layer
                    out.append(out_buff)
            if not list_is:
                out.append(buff)
                break

        test = out[::-1][0]
        test = test[:len(test) - 1]
        out[len(out) - 1] = test

        out_string = ''

        out_string += 'Layer #0: '
        out_string += str(self.root.value) + '\n'

        for layer_index, layer in enumerate(out):
            out_string += f'Layer #{layer_index + 1}: '
            for node in layer:
                out_string += str(node) if node is not None else '*'
                out_string += ' '
            out_string += '\n'

        return out_string

    def isin(self, s, node=None):
        """
        Function is created for checking availability of string.

        :param s: searchable string in nodes
        :param node: node of subtree where we are finding node and current node in iteration
        :return: returning the True if element is found or False if element did not found
        """

        if node is None:
            node = self.root
        if node.value == s:
            return True
        else:
            return self.isin(s, node.left) if node.left is not None \
                else False or self.isin(s, node.right) if node.right is not None \
                else False

    def remove(self, s, node=None, node_prev=None):
        """
        Function for deleting nodes by value
        :param s: value of deleted node
        :param node: node which is start of subtree where we are finding node to delete and our current node
        :param node_prev: link to the previous node and needed for unlinking fonded node
        :return: True if success or False if unsuccess
        """

        if node is None:
            node = self.root
        if node.value == s:
            if node.right is not None:
                if node.right.left is None:
                    node.value = node.right.value
                    node.right = node.right.right
                else:
                    elem = lambda elem_node: (elem(elem_node.left)
                                              if elem_node.left.left is not None else elem_node) \
                        if elem_node.left is not None else elem_node
                    find_node = elem(node.right)
                    node.value = find_node.left.value
                    find_node.left = None
            elif node.left is not None:
                node = node.left
            else:
                node_prev.right = None
        else:
            self.remove(s, node.left, node_prev=node) if node.left is not None else False
            self.remove(s, node.right, node_prev=node) if node.right is not None else False

    def to_list(self):
        # TODO: write to list func (check print(strBinTree.root), i think that normally its depth left down)
        pass

    def get(self):
        # TODO: write get func ( i think its normal find )
        pass

    def __slayer_master(self, tree_layer=None):
        """
        This Function needed to group nodes by layers in the list
        :param tree_layer: start layer list with nodes
        :return: list with layers from top to bottom(leafs)
        """

        tree_layer = [self.root] if tree_layer is None else tree_layer
        next_tree_layer = []

        for node in tree_layer:
            if node is not None:
                if node.left is not None:
                    next_tree_layer.append(node.left)
                else:
                    next_tree_layer.append(None)
                if node.right is not None:
                    next_tree_layer.append(node.right)
                else:
                    next_tree_layer.append(None)

        str_tree_layer = [node.value if node is not None else None for node in next_tree_layer]

        out = str_tree_layer

        if str_tree_layer != [None] * len(str_tree_layer):
            buf = self.__slayer_master(tree_layer=next_tree_layer)
            out.append(buf)
            return out
        else:
            return

    def test(self):
        """
        Function for testing written code with BT
        :return: all what you need XD
        """

        elem = lambda node: (elem(node.left) if node.left.left is not None else node) if node.left is not None else node
        print(elem(self.root).value)


def main():
    node = Node(2)

    tree = StrBinTree(Node(1))
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(3)
    tree.add(2)
    tree.add(4)
    tree.add(-1)
    tree.add(-5)
    tree.add(0)
    # val = -5
    # print(tree.isin(val))
    # tree.remove(val)
    # print(tree.isin(val))
    # print(tree.root.left.left)

    # tree.remove(1)
    # tree.to_list()

    # print(tree.to_list())

    print(help(StrBinTree))


if __name__ == '__main__':
    main()
