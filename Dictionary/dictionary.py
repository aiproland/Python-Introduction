Profile_info_person1 ={'name':'roghaye'  ,'family':'faraji'  , 'phone':'0919xxx'  }
Profile_info_person2 ={'name':'armita'  ,'family':'razavi'  , 'phone':'0912xxx'  }

# print(Profile_info_person2['family'])
Profile_info_person1['gender'] = 'female'
Profile_info_person1['phone'] = '0912xxx'

# del Profile_info_person1['phone']
# print(Profile_info_person2.get('phone' , 'the mentioned key is not in dictionary'))

# print(Profile_info_person1)
# print(Profile_info_person1.items())
for key,value in Profile_info_person2.items():
    print(" key : " , key)
    print(" value : " , value)


