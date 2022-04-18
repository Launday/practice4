import os


class Deque:
    def __init__(self, lists):
        self.lists = lists

    def __add_top__(self, obj):
        self.lists.append(obj)

    def __add_bottom__(self, obj):
        self.lists.insert(0, obj)

    def __del_up__(self):
        self.lists.pop()

    def __del_bottom__(self):
        self.lists.pop(0)

    def __size__(self):
        return len(self.lists)

    def __top__(self):
        return self.lists[-1]

    def __bottom__(self):
        return self.lists[0]


def menu():
    global list_of_matrix
    print(
        "Введите команду:\n1)Задать очередь и назвать ее\n2)Вывести очередь\n3)Добавить в конец\n4)Добавить в начало\n5)Удалить из конца\n6)Удалить из начала\n7)Посмотреть первый элемент очереди\n8)Посмотреть последний элемент очереди\n9)Вывести размер очереди\n10)Выход")
    choose = input()
    if choose == '10':
        return
    if choose in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        if choose == '1':
            name = input("Введите имя ")
            que = input("Введите элементы очереди через пробел! ").split()
            list_of_matrix[name] = Deque(que)
        elif choose == '2':
            name = input("Введите имя ")
            if name in list_of_matrix:
                print(*(list_of_matrix[name].lists))
            else:
                print("Такой очереди нет в списке")
        elif choose == '3':
            name = input("Введите имя ")
            if name in list_of_matrix:
                element = input("Введите элемент, который хотите добавить в очередь ")
                list_of_matrix[name].__add_top__(element)
            else:
                print("Такой очереди нет в списке")

        elif choose == '4':
            name = input("Введите имя ")
            if name in list_of_matrix:
                element = input("Введите элемент, который хотите добавить в очередь ")
                list_of_matrix[name].__add_bottom__(element)
            else:
                print("Такой очереди нет в списке")
        elif choose == '5':
            name = input("Введите имя ")
            if name in list_of_matrix:
                list_of_matrix[name].__del_up__()
            else:
                print("Такой очереди нет в списке")
        elif choose == '6':
            name = input("Введите имя ")
            if name in list_of_matrix:
                list_of_matrix[name].__del_bottom__()
            else:
                print("Такой очереди нет в списке")
        elif choose == '7':
            name = input("Введите имя ")
            if name in list_of_matrix:
                print(list_of_matrix[name].__bottom__())
            else:
                print("Такой очереди нет в списке")
        elif choose == '8':
            name = input("Введите имя ")
            if name in list_of_matrix:
                print(list_of_matrix[name].__top__())
            else:
                print("Такой очереди нет в списке")
        elif choose == '9':
            name = input("Введите имя ")
            if name in list_of_matrix:
                print(list_of_matrix[name].__size__())
            else:
                print("Такой очереди нет в списке")
    else:
        print("Введена неверная команда!")
    os.system("PAUSE")
    os.system('cls')
    menu()


if __name__ == "__main__":
    global list_of_matrix
    list_of_matrix = {'f': Deque([1, 2, 3, 4, 5])}

    menu()
