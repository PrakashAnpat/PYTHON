from openpyxl import NUMPY
import numpy
stud_roll=numpy.array([1,2,3,4,5])
#char1=array([a,b,c,d,e])
#print(char1)
print(stud_roll)
print(stud_roll[0])
print(stud_roll[1])
print(stud_roll[2])
print(stud_roll[3])
print(stud_roll[4])
#modify elements
stud_roll[0]=6
stud_roll[1]=7
stud_roll[2]=8
stud_roll[3]=9
stud_roll[4]=10
print(stud_roll)
#In reverse order
print(stud_roll[-1])
print(stud_roll[-2])
print(stud_roll[-3])
print(stud_roll[-4])
print(stud_roll[-5])