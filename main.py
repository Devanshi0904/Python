#==========if===============
#1.check the two number are same
# i=10
# j=10

# if i==j :
#     print("Number are same")

#2.even number
# num=int(input("Enter Number 1 to 10 "))
# if num%2==0:
#     print(f"{num} is even")

#3.odd number
# num=int(input("Enter Number 1 to 10 "))
# if num%2!=0:
#     print(f"{num} is odd")



#===============if,elif,else=====================
#4.greater number of three number
# a=10 
# b=50
# c=30

# if (a>b and a>c):
#     print(f"{a} is greater")
# elif (b>a and b>c):
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greatre")

#5.check even odd

# num=int(input("Enter Number"))
# if num%2==0:
#      print(f"{num} is even")
# else:
#     print(f"{num} is odd")


#=======While loop, For loop===
#6.print 1 to 10

#======While loop======
# i=1
# while(i<=10):
#     print(i)
#     i=i+1

#=========for loop===========   
# for i in range(1,14):
#     print(i)

#7.table of any number
# num=int(input("Enter a Number"))

# for i in range(1,11):
#     print(f"{num} x ",i,"= ",num*i)

#8.fibonacci series
# a=0
# b=1
# print(a)
# print(b)
# for i in range(7):
#     c=a+b
#     a=b
#     b=c
#     print(c)


#9.factorial number
# num=int(input("Enter The Number "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print(fact)

#=================Array=======

#10.find sum of array

# a=[1,2,3,4,5]
# sum=0

# for i in a:
#     sum+=i
# print(sum)

#11.display even number from given array

# array=[2,32,44,53,13]

# for i in array:
#     if i%2 == 0:
#         print(i)


#12.display odd number from given array

# array1=[2,32,44,53,13]
# array1=[15,16,13,11,8,3]

# for i in array1:
#     if i%2 != 0:
#         print(i)



#13.print in ascending array

# array2=[2,32,44,53,13]
# array2.sort()
# print(array2) 
 
# array2=[44,53,13,2,32]
# array2=[2,13,32,44,53]
# array2=[59,9,10,11,23,45]
# n=0
# for i in array2:
#     n+=1
# print(n)

# for i in range(n):
#     swap=False
#     for j in range(0,n-i-1):
#         print("***********************",i)
#         if array2[j] > array2[j+1]:
#             array2[j],array2[j+1]=array2[j+1],array2[j]
#             swap=True
#     if swap== False:
#         break
        
# print(array2)
# print("Max Number:-",array2[n-1])                                                           


#========================String===================

#14.get the length of string

# text="hello world!"
# count=0

# for i in text:
#     count+=1
# print(count)

# 15.check if character in string

# text="hello python!"
# ch=input("Enter Your Character ")
# found=False

# for i in text:
#     if i==ch:
#         found=True
#         break
# if(found==True):
#     print("character found!")                                 
# else:
#     print("character not found")


#15.check if word in string

# string="Wello World"
# word=input("enter word:- ")
# found=False
# count1=0
# count2=0
# for i in string:
#     count1+=1
# # print(count1)
# for i in word:
#     count2+=1
# # print(count2)
# for i in range(count1-count2+1):
#     match=True

#     for j in range(count2):
#         print("==================",string[i+j] != word[j])
#         if string[i+j] != word[j]:
#             print("++++++++++++++++++++++++",word)
#             match=False
#             break
#     if match:
#         found=True
#         break
# if found:
#     print("Your Word Found")
# else:
#     print("Sorry Not Found")

# s="Hello World Good"
# s2=[]
# result=""
# check="Good"

# for i in s:
#     if i!=" ":
#         result+=i
#         print("result-1",result)
#     else:
#         s2.append(result)
#         print("result-2",result)
#         result=""
        
# # if result !=" ":
# #     s2.append(result)
# s2.append(result)
# # print(s2)

# found=False
# print("s2............",s2)
# if check in s2:
#     found=True
    
# if found:
#     print("Yes")
# else:
#     print("No")

# 16.replace a string with another word
# text="hello world!"
# new_string=""
# new_chr=input("Enter Your Char:- ")

# for i in text:
#     if i=="h":
#         new_string+=new_chr
#     else:
#         new_string+=i
# print(new_string)

#17.reverse a string
# string="hello world!"
# reverse=""
# for i in string:
#     reverse=i+reverse
# print(reverse)



#18.reverse case string
# string="Hello WoRLd"
# new_string=""

# for i in string:
#     if "A" <= i <="Z":
#         new_string+=chr(ord(i)+32)
#     elif 'a' <= i <= 'z':
#         new_string+=chr(ord(i)-32)
#     else:
#         new_string+=i
# print(new_string)

# 19.remove all duplicate for given string

# string="madam"
# new_string=""

# for i in string:
#     if i not in new_string:
#         new_string+=i
# print(new_string)


#==============Other Program===========

# 20. palindrome number
# number=121
# temp=number
# sum=0
# while number!=0:
#     rem=number%10
#     sum=sum*10+rem
#     number=number//10
# if(sum==temp):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 21.factorial
# num=int(input("Enter The Number:- "))
# fact=1

# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#22. sum of digit
# num=563
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

#23. swap two number
# a=5
# b=10
# a=a+b
# b=a-b
# a=a-b
# print("Numbers after Swaping:-","a:-",a,"b:-",b)

#24. sum of two number

# def add(a,b):
#     sum=a+b
#     return sum

# result=add(10,5)
# print(result)

#25. average of five number

# def average(a,b,c,d,e):
#     sum=a+b+c+d+e
#     number=
#     aver=sum/5
#     return aver

# def average(*args):
#     total=0
#     count=0
#     for i in args:
#         total=total+i
#         count+=1
#     avg=total/count
#     print("Avg of numbers:- ",avg)

# average(10,20,30,40,50)
# average(10,20)
# result=average(10,20,30,40,50)
# print(result)

#26. call by value 

# number=100

# def call_by_value(number):
#     number=500
#     print("Function Number:-",number)

# call_by_value(number)
# print("Outer Function Number:-",number)

#26.call by reference

# def call_by_reference(mylist):
#     mylist.append("Patel")
#     print("Inside Function List:-",mylist)

# info=["Tisha"]
# call_by_reference(info)
# print("Outer Function List:-",info)

# print("====================================================================================")

# armstrong
# for i in range(100,1000):
#     number=i
#     temp=number
#     sum=0
#     while number!=0:
#         rem=number%10
#         sum+=rem**3
#         number=number//10
#     if(sum==temp):
#             print(f"{temp}")

# print("====================================================================================")
# *  
# * *  
# * * *  
# * * * *  
# * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

# ===== OR =====
# *
# **
# ***
# ****
# *****
# ******

# for i in range(6):
#     print("*"*(i+1))

# print("====================================================================================")
#           *  
#         * *  
#       * * *  
#     * * * *  
#   * * * * *

# for i in range(1,6):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

# ======= OR =======
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,6):
#     print(" "*(5-i)+'*'*i)

# print("====================================================================================")
#           *  
#         * * *  
#       * * * * *  
#     * * * * * * *  
#   * * * * * * * * * 

# for i in range(1,6):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print(" ")

# print("====================================================================================")
# * * * * * * * * * * *  
#   * * * * * * * * *  
#     * * * * * * *  
#       * * * * *  
#         * * *  
#           *  

# for i in range(6,0,-1):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print(" ")

# print("====================================================================================")
# * * * * * *  
# * * * * * *  
# * * * * * *  
# * * * * * *  
# * * * * * * 

# for i in range(1,6):
#     for j in range(6):
#         print("*",end=" ")
#     print(" ")

# ====== OR ======
# ******
# ******
# ******
# ******
# ******
# ******

# for j in range(6):
#     print("*"*6)


# print("====================================================================================")
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *  

# for i in range(1,6):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print(" ")
# for i in range(6,0,-1):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print(" ")

# ======== OR ======

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# * * * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 

# for i in range(1,6):
#     print(" "*(6-i)+"* "*i)
# for j in range(6,0,-1):
#     print(" "*(6-j)+"* "*j)

# print("====================================================================================")
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# * 

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

# ======== OR =======
# ******
# *****
# ****
# ***
# **
# *

# for i in range(6,0,-1):
#     print("*"*i)

# print("====================================================================================")
# * * * * * *  
#   * * * * *  
#     * * * *  
#       * * *  
#         * *  
#           * 

# for i in range(6,0,-1):
#     for k in range(6-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")

# ============== OR ==============
# ******
#  *****
#   ****
#    ***
#     **
#      *

# for i in range(6,0,-1):
#     print(" "*(6-i)+"*"*i)

# print("====================================================================================")
# * * * * * *  
# *         *  
# *         *  
# *         *  
# *         *  
# * * * * * *

# for i in range(6):
#     for j in range(6):
#         if(i==0 or j==0 or i==5 or j==5):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# print("====================================================================================")
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

# print("====================================================================================")
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

# num=1
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# print("====================================================================================")
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# num=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# print("====================================================================================")
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

# ch=1
# for i in range(1,6):
#     for j in range(i):
#         print(chr(64+ch),end=" ")
#         ch+=1
#     print()

# print("====================================================================================")
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

# ch=1
# for i in range(1,6):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#         ch+=1
#     print()

