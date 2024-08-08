##########################solution1#######################################

number=1098

sum_=0
while number>0:
    sum_+=number%10

    number //=10

print(sum_)
##########################solution2#######################################
mylist=[3,6,-9,76]
length=len(mylist)
for i in range(length):
    print(mylist[length-i-1])