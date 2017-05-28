def bubble_sort(alist):
    # TODO your code here
    sorted = False
    if len(alist) < 2:
        return alist
    while sorted is False:
        nswaps = 0
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                #ph = alist[i]
                #alist[i] = alist[i+1]
                #alist[i+1] = ph
                nswaps += 1
        if nswaps == 0:
            sorted = True
    return alist

print(bubble_sort([4, 5, 3, 1, 2]))