def translate(hex):    #translates input in row of digits
    
    number = []
    for i in range(3):
        for j in range(3):
            if hex[i][j] == " ":
                number.append(0)
            if hex[i][j] == "|":
                number.append(1)
            if hex[i][j] == "_":
                number.append(2)
            if hex[i][j] == "\\":
                number.append(3)
            if hex[i][j] == "/":
                number.append(4)
    return number