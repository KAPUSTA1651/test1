# ooп- это обЪектно орентированное программирование
# основные столпы ооп это: н.0аследывание, инкапсуляция, полиморфизм
# class A:
#     def __init__(self, p, d):
#         self.p=p
#         self.d=d
#         # self.b()
#     def b(self):
#         print(self.p, self.d )
# class B(A):
#     def fly(self):
#         print(f'самалёт c {self.d} двигателями и с {self.p} пасажирами взлетел')
#         self.b()
#
# s=B(121,2).fly()
#
# class Plane():
#     def __init__(self):
#             pass
#     def d(self):


# a="привет"
#
# print(b)
# b=a.replace('и','+')
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# Создайте класс Soda (для определения типа газированной воды),
# выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
# В этом классе реализуйте метод show_my_drink(),

# class Coda():
# а иначе отобразится следующая фраза: «Обычная газировка».
#         if dobavka:
#     def __init__(self, dobavka=None):
#         else:
#             self.dobavka=dobavka
#     def show_my_drink(self):
#             self.dobavka=None
#             print(f'Газировка и {self.dobavka}')
#         if self.dobavka:
#             print("Обычная газировка")
#         else:
# go=Coda()
#
# go.show_my_drink()
# go1=Coda('Лимон')



# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# go1.show_my_drink()
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
# – С отрицательными числами ничего не выйдет!;
# – Ура, можно построить треугольник!;
# – Жаль, но из этого треугольник не сделать.
# – Нужно вводить только числа!;
# сумма длин двух любых сторон всегда больше третьей.
# Построить треугольник из отрезков можно лишь в одном случае:
#         def __init__(self, znachenie):
# class TriangleChecker():
#                 self.is_triangle()
#                 self.znachenie=znachenie
#                 a1=self.znachenie[0]
#         def is_triangle(self):
#                 a3=self.znachenie[2]
#                 a2=self.znachenie[1]
#                 #
#                 # if isinstance(i, (float, int)) and i>0:
#                 #     print('Жаль, но из этого треугольник не сделать.')
#                 # else:
#
#                 if a1>0 and a2>0 and a3>0:
#                                 print('Ура, можно построить треугольник!')
#                         if ((a1+a2)>=a3 or (a1+a3)>=a2 or (a2+a3)>=a1):
#                                 print('Жаль, но из этого треугольник не сделать.')
#                         else:
#                         print('С отрицательными числами ничего не выйдет!')
#                 else:
# go=TriangleChecker([5, 2, 6])
#

# Напиши класс "Банковский счёт" (BankAccount).
#
# Он должен иметь:
#
# приватный атрибут "баланс" (balance);
# метод для изменения баланса (set_balance(value));
# метод для вывода на экран текущего баланса (get_balance());
# метод зачисления денег на счёт (add(value));
# метод снятия денег со счёта (remove(value)).

#
# class BankAccount:
#     def __init__(self):
#
#

class BankAccount:
    def __init__(self, set_balance, balance, add, remove, get_balance):
        self.__balance = balance
        # self.set_balance = set_balance
        # self.add = add
        # self.remove = remove

    def set_balance(value):
        pass

    def add(value):
        pass

    def remove(value):
        pass

    def get_balance(self):
        print("Баланс на счете:", self.__balance)
