a = 1333335
print(a)
print(str(a))
print(len(str(a)))


for i in 'hello':
    print(i)

print(str(a).count("3"))
#1
start = input("Если вы хотите начать работу с калькулятором введите: start ")
a = int(input("tell your number:"))
print(len(str(a)))
are = 0
for i in str(a):
    are += int(i)
print(are)
j = len(str(a))
print(f"среднее арифметическое: {are / j}")

print(str(a).count("0"))
#2
size = int(input("tell your number:"))
for i in range(8):
    for j in range(8):
        if (i +j) % 2 == 0:
            print("_" * size,  end="")
        else:
            print("*" * size,  end="")
    print()
#3
import random
lvl = int(input("Выберете уровень сложности: легко-1, средний-2, сложный-3:"))
if lvl==1:
    ch=2
elif lvl==2:
    ch=5
else:
    ch=8
ball=5/ch
kol=0
while ch>0:
    i=random.randint(2,9)
    if lvl==1:
        i1=random.randint(2,3)
    elif lvl==2:
        i1=random.randint(2,6)
    else:
        i1 = random.randint(2, 9)
    ch = ch - 1
    print(i, 'x', i1)
    otv = int(input("Введите ответ "))
    if otv == i * i1:
        print("Молодец!")
#4
n = int(input("number"))
for i in range(n):
    print(" " * (n - i - 1)+ "* " * (i + 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

