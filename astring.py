from Beautifulstring import name_str
import random as ran
class name_strs(name_str):
    def __init__(self):
        self.__name = 'Hallo world!'
    def Disorganization_name(self):
        self.__name = self.__name.split(' ')
        ran.shuffle(self.__name)
        self.__name = ' '.join(self.__name)
        return self.__name
    def extraction_name(self):
        self.__name = self.__name.split(' ')
        self.__name = ran.choice(self.__name)
        self.__name = ''.join(self.__name)
        return self.__name
    def cope_fill_name(self,path,mude):
        try:
            with open(path,mude) as f:
                data = f.read()
                return data
        except FileNotFoundError:
            pass
    def paste_fill_name(self,data,path=r'C:\Program Files',taxt_name='a.txt'):
        fill = path+taxt_name
        with open(fill,'w') as f:
            f.write(data)