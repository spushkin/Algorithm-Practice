num = 10

def countdown(num):
    if num == 0: #Базовый случай(предотвращаем зацикливание)
        print("End")
        return
    print(num)  
    countdown(num-1) #Рекурсивнвый случай (функция вызывает сама себя)
countdown(num) #Вызываем функцию