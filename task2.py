import sympy # библиотека 
s = open(r"24.txt").readline() # открываем файл и читаем строку 
c = 0 # счетчик
sp = list(sympy.primerange(0, 10**6)) # через библиотеку создаем список простых чисел от 0 до 10^6
for i in sp: # перебор по списку простых чисел
    c += s.count(str(i)) # плюсуем найденных простых чисел из перебора

print(c)