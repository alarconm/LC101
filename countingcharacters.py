def counting_characters(a_string):
    '''count all of the characters in a string by putting into a dictionary'''
    new_dictionary = {}
    for character in a_string:
        if character in new_dictionary:
            new_dictionary[character] += 1
        else:
            new_dictionary[character] = 1
    return new_dictionary

print(counting_characters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."))
