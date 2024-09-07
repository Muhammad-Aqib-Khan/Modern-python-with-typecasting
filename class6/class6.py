from typing import Union

perType = Union[float , int]
percentage : list[perType] = [88.6 , 99.9,50,55,65]
grades : list[str] = []

for per in percentage :
    grade : str = ""
    if per >= 80 :
        grade = "+A"
    elif per >= 70 :
        grade = "A"
    elif per >= 60 :
        grade = "B"
    elif per >= 50 :
        grade = "C" 
    else :
        grade = "Fail"
    grades.append(grade)
print(percentage)
print( grade)