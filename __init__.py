import re
from random import shuffle,choice

class name_str:
    def __init__(self):
        self.__name = 'Hallo Would'

    def get_name(self):
        return self.__name

    def __drow(self):
        print(self.__name)
        return

    def print_name(self):
        return self.__drow()

    def end_name(self, name):
        self.__name = self.__name + name
        return self.__name

    def first_name(self, name):
        self.__name = name + self.__name
        return self.__name

    def middle_name(self, name, step=1):
        self.__name = list(self.__name)
        step -= 1
        self.__name.insert(step, name)
        self.__name = ''.join(self.__name)
        return self.__name

    def cut_name(self, new_name):
        '''
        只支持一个字符！
        mean:
        Only one character is supported！
        '''
        name = list(new_name)
        for i in name:
            new_name = re.escape(i)
            self.__name = re.sub(new_name, '', self.__name)
            return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name


    a_name = property(get_name, set_name)


