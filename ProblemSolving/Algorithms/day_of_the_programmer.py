import datetime

def dayOfProgrammer(year):
    feb = 0
    if(year < 1918):
        if year % 4 == 0:
            feb = 29
        else:
            feb = 28
    elif(year > 1918):
        if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            feb = 29
        else:
            feb = 28
    else:
        feb = 15            
    months = [31, feb, 31, 30, 31, 30, 31, 31]
    x = datetime.datetime(year, 9, 256 - sum(months))
    return x.strftime("%d.%m.%Y")