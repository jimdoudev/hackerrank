import math

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        upper = math.ceil(grade / 5) * 5
        if(grade < 38):
            new_grades.append(grade)
        elif(upper - grade < 3):
            new_grades.append(upper)
        else:
            new_grades.append(grade)
    return(new_grades)