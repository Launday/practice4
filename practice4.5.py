import os
import re


class Note:
    def __init__(self):
        self._name = None
        self._surname = None
        self._phone = None
        self._birth = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth


def output(list_of_notes, number):
    for i in range(len(list_of_notes)):
        if number == list_of_notes[i].phone:
            print("Имя человека: {}\nФамилия: {}\nДата рождения {}".format(list_of_notes[i].name,
                                                                           list_of_notes[i].surname,
                                                                           ".".join(list_of_notes[i].birth)))
            return
    print("Такого номера нет в списке!")
    return


def main():
    with open('test.txt', 'r', encoding='utf-8') as file:
        f = file.readlines()
        list_of_notes = [0] * len(f)
        for i in range(len(f)):
            f[i] = f[i].split()
            list_of_notes[i] = Note()
            list_of_notes[i].name = f[i][0]
            list_of_notes[i].surname = f[i][1]
            list_of_notes[i].phone = f[i][2]
            list_of_notes[i].birth = f[i][3].split('.')

    number = input("Введите номер по форме +7(000)000-00-00:  ")
    if len(number) == 16 and number[0] == '+' and number[2] == '(' and number[6] == ')' and number[10] == '-' and number[13] == '-' and all(
            i.isdigit() for i in re.sub("[()+]", "", number).replace("-", "")):
        output(list_of_notes, number)
    else:
        print("Номер введен неверно!")
    os.system("PAUSE")
    os.system("cls")
    main()


if __name__ == "__main__":
    main()
