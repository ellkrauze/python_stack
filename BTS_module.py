class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):    #Добавление узла в дерево
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Значение уже существует в дереве!")

    def print_in_order(self):  #Печатаем дерево # IN-ORDER снизу вверх

        if self.root != None:
            print('В обратном порядке: ')
            self._print_in_order(self.root)
        else:
            print('Дерево пусто')

    def _print_in_order(self, cur_node):
        if cur_node != None:
            self._print_in_order(cur_node.left_child)
            print(str(cur_node.value))
            self._print_in_order(cur_node.right_child)

    def print_pre_order(self):  # PRE-ORDER - сверху вниз - пишем узел, на который встаем
        if self.root != None:
            print('В прямом порядке: ')
            self._print_pre_order(self.root)
        else:
            print('Дерево пусто')

    def _print_pre_order(self, cur_node):
        if cur_node != None:
            print(str(cur_node.value))
            self._print_pre_order(cur_node.left_child)
            self._print_pre_order(cur_node.right_child)

    def print_post_order(self):  # POST-ORDER начиная с детей
        if self.root != None:
            print('В концевом порядке: ')
            self._print_post_order(self.root)
        else:
            print('Дерево пусто')

    def _print_post_order(self, cur_node):
        if cur_node != None:
            self._print_post_order(cur_node.right_child)
            print(cur_node.value)
            self._print_post_order(cur_node.left_child)



    def find(self, value): # Поиск узла
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value): # Удаление узла
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # Предотвращает удаление несуществующего узла
        if node == None or self.find(node.value) == None:
            print("Узел, который вы хотите удалить, отсутствует в дереве!")
            return None

        def num_children(n):  # количество детей в узле
            num_children = 0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # CASE 1 (node has no children) - родитель забывает ребенка
        if node_children == 0:
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child) - бабушка удочеряет внучку, внучка принимает бабушку как маму
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child  # записываем "вес" ребенка ; проверка, если он правый,
                                                # то запис. вес правого и аналогично с левым
            else:
                child = node.right_child

            if node_parent != None:
                # replace the node to be deleted with its child # ребенок встает на место родителя
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            child.parent = node_parent

        def min_value_node(n):  # min value in right the branch for CASE 3
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # CASE 3 (node has two children) - на место узла встает in-order successor (eg: 50 - 51, 49 - 49.25)
        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value  # точнее, просто меняем значения
            self.delete_node(successor)

