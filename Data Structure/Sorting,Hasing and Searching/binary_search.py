def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <=last and not found :
        mid = (first + last) // 2
        if a_list[mid] == item :
            found = True
        else:
            if a_list[mid] > item:
                last = mid -1
            else:
                first = mid + 1
    return found
def rec_binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid= len(a_list) //2
        if a_list[mid] == item :
            return True
        else:
            if a_lsit[mid] > item:
                return rec_binary_search(a_list[:mid],item)
            else:
                return rec_binary_search(a_list[mid+1:],item)
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,] 
print(binary_search(test_list, 3)) 
print(rec_binary_search(test_list, 13))
