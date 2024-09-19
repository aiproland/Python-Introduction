names =['roghae' , 'armita','ali','hadi']
# names.append('leila')


numbers =[1,23,-9,40,90]
# numbers.append(87)

def add_list(member ,mylist = [1,2,3]):
    mylist.append(member)
    print(mylist)


# add_list(67)
# add_list( member='leila')

def summation(*nums):

    sum_ = 0
    for i in nums:
        sum_+=i

    print(sum_)

# summation(3,6,80,99,37,-9,-8)


def profile(**info):

    return info

print(profile(name = 'roghaye' , family = 'faraji' , age = 29))
print(profile(name = 'armita' , favorites ='progrmming' , phone ='0912xx'))
