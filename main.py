class Magistr:
    def __init__(self, name, raiting, age, wd="" , argument=0):
        self.name = name
        self.raiting = raiting
        self.age = age
        self.wd = wd
        self.argument = argument
        if self.wd != "":
            self.raiting = self.raiting + len(self.wd)
            if self.age >= 14.5:
                self.age = self.age - (abs(len(self.wd)) // 10)
                print(f"Обновлённый рейтинг {self.raiting}, обновлённый возраст {self.age}")
            else:
                print(f"Обновлённый рейтинг {self.raiting}, возраст не изменился")
        if self.argument != 0:
            arg = (self.argument - self.age) * self.raiting
            print(f"Результат числа-аргумента : {arg}")
    def raiting_change(self, value):
        vopros = int(input("Что вы хотите сделать: увеличить или уменьшить рейтинг?"))
        if vopros == 1:
            self.raiting = self.raiting + value
            if self.age >= 14.5:
                self.age = self.age - (abs(value) // 10)
                print(f"Обновлённый рейтинг {self.raiting}, обновлённый возраст {self.age}")
            else:
                print(f"Обновлённый рейтинг {self.raiting}, возраст не изменился")
        elif vopros == 2:
            self.raiting = self.raiting - value
            self.age = self.age + (abs(value) // 10)
            print(f"Обновлённый рейтинг {self.raiting}, обновлённый возраст {self.age}")
        else:
            raise TypeError("Error, неправильный ввод данных")
    def str(self):
        print(f"Mag {self.name} with {self.raiting} rating looks {self.age} years old")
    def __eq__(self, other): # для функции ==
        vopros2 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros2 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting == sc
        elif vopros2 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age == sc
        elif vopros2 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name == sc
        else:
            raise TypeError("Error, неправильный ввод данных")
    def __ne__(self, other): # для функции !=
        vopros3 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros3 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting != sc
        elif vopros3 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age != sc
        elif vopros3 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name != sc
        else:
            raise TypeError("Error, неправильный ввод данных")
    def __lt__(self, other): # для функции <
        vopros3 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros3 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting < sc
        elif vopros3 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age < sc
        elif vopros3 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name < sc
        else:
            raise TypeError("Error, неправильный ввод данных")
    def __le__(self, other): # для функции <=
        vopros3 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros3 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting <= sc
        elif vopros3 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age <= sc
        elif vopros3 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name <= sc
        else:
            raise TypeError("Error, неправильный ввод данных")
    def __gt__(self, other): # для функции >
        vopros3 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros3 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting > sc
        elif vopros3 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age > sc
        elif vopros3 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name > sc
        else:
            raise TypeError("Error, неправильный ввод данных")
    def __ge__(self, other): # для функции >=
        vopros3 = input("Что вы хотите сравнить: raiting, age или name?")
        if vopros3 == "raiting":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.raiting
            return self.raiting >= sc
        elif vopros3 == "age":
            if not isinstance(other, (int, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо int")
            sc = other if isinstance(other,int) else other.age
            return self.age >= sc
        elif vopros3 == "name":
            if not isinstance(other, (str, Magistr)):
                raise TypeError("Операнд справа должен быть либо экземпляром класса, либо str")
            sc = other if isinstance(other,str) else other.name
            return self.name >= sc
        else:
            raise TypeError("Error, неправильный ввод данных")
Yoda = Magistr("Jeembo",100,40)
Yoda.raiting_change(20)
Yoda.str()
print(Yoda == 120)
print(Yoda != 120)
print(Yoda < 120)
print(Yoda <= 120)
print(Yoda > 120)
print(Yoda >= 120)