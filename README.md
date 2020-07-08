# dats-science-
Basic codes for beginner  data analyst\scientist\AI/ML beginer
a=10
b=20
a=5;b=10
b,c=3.2,"Hello"
x=y=z="WOrld"
print(c)
print()
print("Value of a=\n",a)
print("Value of b=\n",b)
print(b,c)
print(b,c,sep=",")
c
print(a)
#%%

##division operartion in python 
print(1/3)

print(1//3)##floored division 
print(7%3)
print(round(1/3,2))
#%%
a=5
b=3.2
print(type(b))
print(a+b)
a="5"
b="3.2"
print(type(b))
#%%

##user input
name=input("enter your name")
print("hello",name)
#%%
x=10
y=5
if x<y:
    print("this is firest block")
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x & y are equal')
print("done")
#%%
##nasted if else
if x==y:
    print('x and y are equal')
else:
    if x<y:
        print('x is less than y')
    else:
        print('x is greater than y')
print("done")

#%%
x=10;y=8
if( x>7 and y>7):
    print('x is single digit positive number.')

#%%
x=5;y=8
if( x>7 and y>7) or x!=y:
    print('x is single digit positive number.')
 #%%
##user defiened function 
def cube(a):
    print("value is =",a)
    return a*a*a

##square 10
value=float(input("enter a number:"))
cube(value)
#%%
def hi():
    print("hello user!")
hi()
#%%
##conditional loop (while)
##a) initiaalizing of itr variable b) condiation evaluation c)increamemtation\decreatation 
count=100
while(count>=70):
    print(count)
    #count +1
    count=count-1
else:
    print("count value reached", count)
#%%
##iterative loop(for loop)
friends=['a','b','c',3.6]
for i in friends:
    print('happy diwali,',i)
#%%
##python numbers
a=5
print(type(a))

b=30.6
print(type(b))

c=3+2j
print(type(c))
#%%
##change of data type
print(int(-2.8))
print(float(5))
#%% library
import math
print(math.sqrt(4))
print(math.floor(10.7))
print(math.pow(2,3))    
print(round(math.pi,2))  
print(math.pi)
print(math.factorial(4))    
#%% library randonm number genration 
import random as rn
#rn.seed(10)
print(rn.random())
print(rn.randrange(50,100))
print(rn.uniform(50.5,100))
x=[1,2,3,4,5]
print(rn.choice(x))    
#%% string
my_string='hello'
print(my_string)
print()
my_string="""hi.hello."""
print(my_string)

my_string="""hello.\n hii."""
print(my_string)
#%% accesing data structure
#slicing
my_string=('pyhton is a programming language. python is intresting.')
print(my_string[0])
print(my_string[-3])
#[inclusive:exclusive]
print(my_string[3:10])
print(my_string[:10])  
print(my_string[3:])  
print(my_string[:]) 
##print(my_string[100]) 
print(len(my_string))
del my_string
print(my_string)
#%% list [data structures]
##del- deleting
##list are mutable or can be modified, tuples are not mutable or cannot be modified
##python list
mylist1=[1,3,5,4,2]

mylist2=[1,4.2,'python',4.2]
print(mylist1)
print(mylist2)
print(type(mylist2))
#%% use of sliccing operator
a=[10,20,30,40,50,60,70,80]
print(a[2])
print(a[0:3])
print(a[5:])
##mutable example [modification in the given list]
a[3]=55.0
print(a)
#%%creating range
x=list(range(0,15))
print(x)
## numpy library have function of listing numbers in ascending or descending order
#%%nasted list
b=['spam',2.0,5,[10,"raj"]] ##nasted list
print(b[3][1])
#%%appending multiple elements
my_list=[1,3,6,9]
my_new_list=[4,5,6,7,8]
my_list.extend(my_new_list)
my_list.append("shreyas")
print(my_list)
#%% tuples immutable{cannot be modified} 
##tuples have () bracket list have [] bracket
a=(5,'python',10+2j,6)
print(a)
print(type(a))
print(a[0])
#%% nasted tuples
n_tuples=('mouse',[8,4,6],(1,2,3),8)
print(n_tuples)
##n_tuples[2][3]=0 immutable
del n_tuples
#%%sets {}
my_set={1,2,3,4,5,6,1,5,3,5,4,8}
print(my_set)
my_set=(1,1.0,"hello","shreyas",(1,2,4))
print(my_set)
#%%##union and intersection 
A=[1,5,4,17,9,4,4,6,2]
B=[15,22,56,2,4,7,88,9,5]
setA=set(A)
setB=set(B)

print(setA | setB)
print(setA.union(setB))
print(setA & setB)
print(setA.intersection(setB))
print(setA-setB)
print(setB.difference(setA))

#%% Dictionaries ##dicttionarie objects are mutable
##creating  dictionary
my_d1={1:'a',2:'b'}
print(my_d1)

my_d2={'name':['shreays','nikita','alex'],"ID":[2,4,3]}
print(my_d2)
print(my_d2['name'])
#%%
##modification of values
my_d={"name":"shereyas","age":27}
print(my_d)

my_d['address']='mumbai'
print(my_d)
my_d.values()
#%% 'zip' allows you to merge data
##data merging 
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=dict(zip(a,b))
print(c)
#%%
##numpy library{arrays}
import numpy as np
np.__version__


a=np.array([1,2,3])
print(a)
print(type(a))
#%%2d array
a=np.array([(1,2,3),(5,5,6)])
print(a)
print(a.ndim) #to tell dimention of arrey
print(a.shape)
#%%accessing the array
##indexing and slicing
a=np.array([(1,2,3,4),(3,4,5,6),(1,2,3,4)])
print(a)
print(a[0,2])
print(a[:,2])
print()
print(a[0:2,])
#%%
#aggreagate functions
a=np.array([(8,9),(10,11),(12,13)])
print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.mean(a))
print(np.sqrt(a))
print(np.std(a))
print(np.log(a))
b=np.sqrt(a)
print(np.round(2))
#%%
import numpy as np
x=np.array([(1,2),(3,4)])
y=np.array([(5,6),(3,4)])
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x@y)
#print(np.dot(x,y))
##print(np.add(x,y))
#np.add(),np.subtract(),np.multiply,np.divide(),np.remainder()

#%% series
import pandas as pd
import numpy as np
data= np.array([101,102,103,104])
s= pd.Series(data)
print(s)

print(s[1])
s[1]=105
s[6]=105
print(s)
#%% key-pairs
data={'a':0.,'b':1.,'c':2.}
s=pd.Series(data)
print(s)
print(s['a'])
print()
print(s[-2:])
#%%data frame
data=[['shreyas',50],['sk',25],['kkk',85]]
df=pd.DataFrame(data,columns=['name','age'])
df
##df.colomns=["name","age"] used if there is need to name columns anda rows after completion of algorithm
##print(df)
#%%
data={'name':['amit','nikita','clara'],'age':[10,20,30]}
df=pd.DataFrame(data)
df

df=pd.DataFrame(data,index=['rank1','rank2','rank3'])
print(df)
df['name']
df[['name','age']]
#adding a column at end
df["address"]=["mumbai","pune","mumbai"]
df

#%% change order of column name
df=df[['name','address','age']]
df
#%% creat numerical variable and computable variable
df['newcol']=[5,10,12]
df

df["rervised_col"]=df['newcol']*2
df
#%% deleting a column
del df["newcol"]
df
#%%droppimg variable axis=1 variables, axis=0 observations

df=df.drop('rank1')
df=df.drop('revised_col',axis=1)
#%%%
print(df)
#%% accessing data using indexes and labels 
##df.loc[inclusive:inclusive]
print(df.loc['rank2'])
print(df.loc['rank2':'rank3'])
##df.iloc[inclusive:exclusive]
print(df.iloc[0:1])
print(df.loc["rank2":"rank3",["address","age"]])
print(df.iloc[:,[1,2]])
#%%
##saving a file\ data  export
df.to_csv(r'C:\Users\hp\Desktop\imarticus\python\sample.csv',
          index=True,header=True)##.txt as well
df.to_excel(r'C:\Users\hp\Desktop\imarticus\python\sample1.xlsx',
          index=True,header=True)
print("done")
#%%
##reading df from a file
df2=pd.read_csv(r'C:\Users\hp\Desktop\imarticus\python\sample.csv',
          index_col=0,header=0)
df2
df3=pd.read_excel(r'C:\Users\hp\Desktop\imarticus\python\sample1.xlsx',
         header=0)
df3
#%%preparing data
print(df.dtypes)
#print(df.age.dtype)
#print(df.shape)
#df.info()
#%%
df.set_value('rank2',['name','age'],["ramesh",40])
df["address"]=['pune','mumbai','banglore']
print(df)
#%% sorting data
df.sort_values(['name',"address"],ascending=False)
df.sort_values(['name',"address"])
df.sort_values(['name',"address"],ascending=[False,True])








































