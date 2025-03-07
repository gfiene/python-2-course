array = [2, 1, 3, 4,56,7 ,7, 2, 2,2 ,7 , 8, 5, 1, 12, 2, 2,2,2 ,22,2 ,2 ,22, 22,  2  ]
toRemove = 2
def removeValue(array, toRemove):
    for i in range(len(array)):
        if array[i] == toRemove:
            array[i] = None

    return array.sort(key=None)
print(removeValue(array, toRemove))
