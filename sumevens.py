def sum_evens(evenlist):
    """sum all of the even numbers in 'evenlist' and return the value"""

    evens = 0

    for i in range(len(evenlist)):
        if evenlist[i] % 2 == 0:
            evens += evenlist[i]

    return evens


print(sum_evens([1,3,4,5,6,7,10]))
