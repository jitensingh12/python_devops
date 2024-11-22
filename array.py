

### Question : find array length then find max number which will less than array length -- 

def find_max_elements(array):
    leng = len(array)
    #print(leng)
    arr = []
    value = 0
    for a in array:
        sum = a
        if sum >= leng:
            #sum = a
            print("loop a value is " + str(a))
            print("skip this value as this greate the target")
        else:
           arr.append(a)
           print("append array value is " + str(a))
    for i in arr:
        value = max(arr)
            #print(value)
    return(value)
if __name__ == '__main__':
    array = [10,2,3,5,5,4,6,7]
    result = find_max_elements(array)
    print(str(result) + '\n')
    #fptr.close()
