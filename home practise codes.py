print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#%%Write a Python program to get the Python version you are using.
print('version')
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
#%% Write a Python program to display the current date and time.
import datetime
before = datetime.datetime.now()
print ("Current date and time : ")
print (before.strftime("%Y-%m-%d %H:%M:%S"))
#%% Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
def area(r):
    print('value is=',r)
    return pi*r**2
value=float(input("enter a number:"))
area(value)
#%%alternate method {not sved in memory}
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#%% accept user first name and last name print thrm in reverse order
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
#%%  generate list and tuples
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
#%%accept filename from user and print extension
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
#%% to display exam schedule
import datetime
exam_st_date = (11, 12, 2014)
print('exam date is:')
print (exam_st_date.strftime("%Y-%m-%d))
#%%
exam_st_date = (11,12,2014)
print( "The examination will start from _%i / %i / %i"%exam_st_date)
#%%Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
import math
op=int(input['n'])
print(n+n*n+n*n*n)
#%%
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
#%%
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))
#%%
exam_st_date = (11, 12, 2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
#%%
a = int(input("Input an integer : "))
n1 = int( " " % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
#%%
print(abs.__doc__)
#%%
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
#%%
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2020, 7, 11)
delta = l_date - f_date
print(delta.days)
#%%
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
#%%`
