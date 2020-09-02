#search function for string(s)

def look(keys, *strings):
    stringlist = []
    for string in strings:
        if keyword in string:
            stringlist.append(string)
    
    return stringlist
    
