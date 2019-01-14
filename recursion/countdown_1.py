def countdown(i):

  if i <= 0: #Базовый случай
    return 0
  
  else:
    print(i)
    return countdown(i-1) #Рекурсивный случай

countdown(10)