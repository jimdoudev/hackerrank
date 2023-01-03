def timeConversion(s):
    to_chars = list(s)
    if(to_chars[-2] == "P"):
        if(to_chars[0] == "1" and to_chars[1] == "2"):
            to_chars[0] = "1"
            to_chars[1] = "2"
        else:
            to_chars[0] = str(int(to_chars[0]) + 1)
            to_chars[1] = str(int(to_chars[1]) + 2)
    else:
        if(to_chars[0] == "1" and to_chars[1] == "2"):
            to_chars[0] = "0"
            to_chars[1] = "0"

    return("".join(to_chars[0:-2]))