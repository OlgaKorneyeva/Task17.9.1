def qsort(array, left, right):
    middle = (left+right) // 2
    
    p = array[middle]
    i,j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
#---------------------------------------------------------        
def sort(array):
    qsort(array, 0, len(array)-1)
#---------------------------------------------------------
def binary_search(array, element, left, right): 
    if (left == right) and array[left] == element:
        return left

    if left > right: # если левая граница превысила правую,
        return -1 # значит элемент отсутствуетб, возвращаем -1 
    
    middle = (right+left) // 2 # находимо середину

    if (array[middle]==element):
        return middle

    if (array[middle]< element and array[middle+1]>element):
        return middle + 1 # возвращаем этот индекс

    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)  
#---------------------------------------------------------
sec = input("Введите последовательность чисел:")
num = int(input("Введите число:"))

sec_array = sec.split(" ")
print(sec_array)

num_array = []
for val in sec_array:
    num_array.append(int(val))
print(num_array)

sort(num_array)
print(num_array)

pos  = binary_search(num_array, num, 0, len(num_array)-1)
if (pos == -1):
    print("not found")
else:
    before = pos-1    

    if before>=0:
        print("element before:", before)
    else:
        print(num, "is the first element")

    if (pos < len(num_array)):
        print("element after:", pos)
    else:
        print(num, "is the last element")
