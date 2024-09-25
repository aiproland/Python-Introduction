mylist=[]

for i in range(101):
    mylist.append(i)

new_list=[i for i in range(101)]
# print(new_list)

infos=[('name ', 'roghaye') , ('family' , 'faraji')]
# dict_={}
# for k,v in infos:
#     dict_[k] = v
# print(dict_)

dict_ ={k:v  for k,v in infos }
# print(dict_)

myset = {k for k,v in infos}
print(myset)