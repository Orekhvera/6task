try :
    array = [int(i) for i in input('Введите значения массива через пробел: ').split()] 
    delta = int(input('Введите смещение DELTA: '))
    min_item = get_min(array)
    count = 0
    for item in array:
        if (item - min_item) == delta:
            count += 1
    print("минимальный элемента массива: ", min_item, " Количество чисел отличающихся на DELTA: ", count)
except:
    print("Ошибка!")
def get_min(array):
    min_item = 999999999 
    for item in array:
        if item < min_item:
            min_item = item
    return min_item