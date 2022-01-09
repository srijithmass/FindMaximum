''' 
Program to the maximum marks without using builtin functions.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def max_marks(list1):
    max_mark=0
    for i in list1:
        if i>max_mark:
            max_mark=i
    return max_mark