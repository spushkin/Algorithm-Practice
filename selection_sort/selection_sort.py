#Ищем наименьшее значение в массиве
def findSmallest(arr):

#Здесь храним наименьшее значение массива
  smallest = arr[0]
#Здесь храним номер наименьшего элемента в массиве
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

#Сортируем
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)): #loop (len - длина массива)
  #Находим наименьшее значение в массиве и добавляем его в конец нового массива 
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10])) #Задаем значения массива для сортировки