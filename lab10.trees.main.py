from BTS_module import *

def Fill(tree):
    print('Начните вводить значения. Чтобы окончить заполнение, введите "." ')
    node = 1
    while node != '.':
        node = input('Введите узел для вставки: ')
        if node != '.':
            tree.insert(int(node))

def Insert(tree):
    n = input('Введите узел для вставки: ')
    tree.insert(int(n))

def Delete(tree):
    n = input('Введите узел для удаления: ')
    tree.delete_value(int(n))

def Find(tree):
    n = input('Введите узел для поиска: ')
    node = tree.find(int(n))
    if node != None:
        print('Значение: ', node.value)
        if node.left_child !=None:
            print('Левый ребенок: ', node.left_child.value)
        else:
            print('Левого ребенка не существует')
        if node.right_child != None:
            print('Правый ребенок: ', node.right_child.value)
        else:
            print('Правого ребенка не существует')
        if node.parent != None:
            print('Родитель: ', node.parent.value)
        else:
            print('Нет родителя')
    else:
        print('Узел, который вы ищете, не существует!')

def Print_in_order(tree):
    tree.print_in_order()

def Print_pre_order(tree):
    tree.print_pre_order()

def Print_post_order(tree):
    tree.print_post_order()

def command():
    print('Заполнить дерево -  введите 0')
    print('Добавить значение в дерево - введите 1')
    print('Удалить значение в дереве - введите 2')
    print('Найти значение в дереве - введите 3')
    print('Напечатать дерево в обратном порядке - введите 4')
    print('Напечатать дерево в прямом порядке - введите 5')
    print('Напечатать дерево в концевом порядке - введите 6')
    print('Выйти - введите 7')
    com = input('\nВвод: ')
    return int(com)

def if_com(tree):
    com = command()
    while com != 7:

        if com == 0:
            Fill(tree)

        if com == 1:
            Insert(tree)

        if com == 2:
            Delete(tree)

        if com == 3:
            Find(tree)

        if com == 4:
            Print_in_order(tree)

        if com == 5:
            Print_pre_order(tree)

        if com == 6:
            Print_post_order(tree)

        com = int(input( '\nОжидание команды :'))
    else:
        print('\nЗавершение программы' )


# ------------------- MAIN PROGRAM ---------------------------------------------
tree = binary_search_tree()
if_com(tree)