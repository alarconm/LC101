def factors(n):
    '''find all factors of numbers from 1 up to n and assign in key value of a dictionary'''
    new_dict = {}
    for i in range(1, n+1):
        new_list = []
        for j in range(1, n+1):
            if i % j == 0:
                new_list.append(j)
        new_dict[i] = new_list
    return new_dict

def reverse(a_dict):
    new_dict = {}
    for key in a_dict:
        if a_dict[key] in new_dict:
            new_dict[a_dict[key]].append(key)
        else:
            new_dict[a_dict[key]] = [key]
    return new_dict

        

def main():
    print(reverse(factors(6)))

if __name__ == "__main__":
    main()



