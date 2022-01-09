''' 
Program to mark the maximum of marks using the list method sort
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def max_marks(marks):
    marks.sort()
    max_mark=marks[-1]
    return max_mark