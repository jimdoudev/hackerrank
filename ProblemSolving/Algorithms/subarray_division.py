def birthday(s, d, m):
    res,value,i,temp = 0,0,0,0
    if len(s) < 2:
        if d == s[0]:
            return 1
        else:
            return 0
    else:
        while i < len(s):
            value += s[i]
            temp += 1
            if temp == m:
                if value == d:
                    res += 1
                    value,temp,i = 0,0,0
                    s.pop(0)
                else:
                    value,temp,i = 0,0,0
                    s.pop(0)
            else:
                i += 1
    return res