def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    #create a new string
    #add first character of fullname to new string
    #iterate through the fullname string 
    #find the index of the blank space and add the NEXT character to new string

    initials = fullname[0].upper()

    for i in range(len(fullname)):
        if fullname[i] == " " and fullname[i+1] != None:
            initials += fullname[i+1].upper()

    return initials

def main():
    """Main function to make importable"""

    initials = input("What is your full name?\n")
    print(get_initials(initials))

if __name__ == '__main__':
    main()