# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def intersection(list1, list2):
    list3 = []
    for value in list1:
        if value in list2 and value not in list3:
            list3.append(value)
    list3.sort()
    return list3


def union(list1, list2):
    list3 = list1
    for value in list2:
        if value not in list3:
            list3.append(value)
    list3.sort()
    return list3


def difference1(list1, list2):
    list3 = list1
    '''set(list1): transformă lista list1 într-un obiect de tip set (mulțime) pentru a elimina duplicatele
       apoi este convertita inapoi in list cu list(set(list1))
    '''
    list3 = list(set(list1))
    for value in list2:
        if value in list3:
            list3.remove(value)
    list3.sort()
    return list3


def difference2(list1, list2):
    list3 = list2
    list3 = list(set(list2))
    for value in list1:
        if value in list3:
            list3.remove(value)
    return list3


if __name__ == "__main__":
    lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
    lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
    print(intersection(lst1, lst2))
    print(union(lst1, lst2))
    print(difference2(lst1, lst2))
    print(difference1(lst1, lst2))
