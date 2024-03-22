#This program is supposed to calculate sum till 5 let's say
#The variable "sum" is initialized to 0
#For loop starts
#But range in For loop would always go till one number less than 5
#so this will calculate sum till 4
#This logical error can be corrected if we give range(5+1) then it will give correct sum of consecutive numbers which is 15
#Lastly printing the sum
sum = 0
for i in range(5):
    sum += i
print("Sum of numbers till 5 is: "+str(sum))
