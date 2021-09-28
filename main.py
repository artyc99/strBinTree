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

    def __add__(self, s):
        """
        Function that make support concatenation strBinTree with strings (adding by "+")
        :param s: value
        :return: None
        """
        if type(s) == Node:
            self.add(s.value)
        else:
            self.add(s)

        return self

    def __repr__(self):
        """
        Description of the object
        :return: str
        """
        # TODO: make normal repr
        pass

    def __len__(self):
        # TODO: make len function that returns count or nodes
        return len([value for value in self.__tree_iterate(self.root)])

    def __str__(self):
        """
        Function for printing strBinTree by layers(only for debugging, now unworking)
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

    def __iter__(self):
        return self.__tree_iterate(self.root)

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
        """
        Gen list values of Nodes
        :return: list of values Nodes
        """
        return [value for value in self]

    def get(self, str_arg):
        tmp_tree = self
        tmp_tree + str_arg
        lst_tree = tmp_tree.to_list()
        left_elem = lst_tree[lst_tree.index(str_arg) - 1] if lst_tree.index(str_arg) > 0 else None
        right_elem = lst_tree[lst_tree.index(str_arg) + 1] if lst_tree.index(str_arg) + 1 < len(lst_tree) else None

        coff1 = sum([l1 == l2 for l1, l2 in zip(str_arg, left_elem)]) if left_elem is not None else 0
        coff2 = sum([l1 == l2 for l1, l2 in zip(str_arg, right_elem)]) if right_elem is not None else 0

        if left_elem is None:
            return right_elem
        elif right_elem is None:
            return left_elem
        elif coff1 > coff2:
            return left_elem
        elif coff1 < coff2:
            return right_elem
        elif coff1 == coff2:
            if len(left_elem) < len(right_elem):
                return left_elem
            elif len(left_elem) > len(right_elem):
                return right_elem
            elif len(left_elem) == len(right_elem):
                return left_elem

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

    def __tree_iterate(self, root):
        '''
        Генератор упорядоченных значений элементов дерева.
        '''
        if root == None:
            return

        yield from self.__tree_iterate(root.left)
        yield root.value
        yield from self.__tree_iterate(root.right)

    def test(self):
        """
        Function for testing written code with BT
        :return: all what you need XD
        """

        if self.current_iteration_node == None:
            return

        for node in self.test():
            self.current_iteration_node.left = node
            yield node
        yield self.current_iteration_node.value
        for node in self.test():
            self.current_iteration_node.right = node
            yield node
        # yield from self.test(root.left)
        # yield root.value
        # yield from self.test(root.right)

    # def __next__(self, like):
    #     like = 1
    #     while True:
    #         yield like


def main():
    tree = StrBinTree(Node('height'))

    # tree1 = StrBinTree(Node(1))
    # tree1 + 2
    # tree1 + 0
    #
    # tree2 = StrBinTree(Node(5))
    # tree2 + 3
    # tree2 + 7
    #
    # tree1 + tree2
    #
    # print(tree1)

    # tree.add(5)
    # tree.add(6)
    # tree.add(7)
    # tree.add(3)
    # tree.add(2)
    # tree.add(4)
    # tree.add(-1)
    # tree.add(-5)
    # tree.add(0)
    # tree.add(2)
    # tree.add(2)

    tree + Node('test')
    tree + 'test2'
    tree.add('gode')
    tree.add('gooode')
    tree.add('important')
    tree.add('like')
    tree.add('kitchen')
    tree.add('people')
    tree.add('yes')
    tree.add('base')
    tree.add('cat')
    tree.add('dog')
    tree.add('early')
    tree.add('five')

    # val = -5
    # print(tree.isin(val))
    # tree.remove(val)
    # print(tree.isin(val))
    # print(tree.root.left.left)

    # tree.remove(1)
    # tree.to_list()

    # print(tree.to_list())
    # print(len(tree))

    # print(tree)
    # print((tree + 2))
    print(tree.get('goode'))
    # print(tree.to_list())


if __name__ == '__main__':
    main()
