def fact(x):
  if x == 1: #Базовый случай
    return 1
  else:
    return x * fact(x-1) #Рекурсивный случай

print(fact(7)) #Ищем Factorial числа 7 (7!)