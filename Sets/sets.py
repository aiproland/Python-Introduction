tags={'programming'  , 'AI'  , 'AI','Pandas'}
tags2=set(['programming' , 'python' , 'AI'  , 'Django' , 'React'])
# print(len(tags))

# print(tags-tags2)
# print(tags.difference(tags2))

# print(tags.intersection(tags2))

# print(tags^tags2)
# tags.add('numpy')
tags.update(['numpy' ,'math'])
# tags.remove('matplotlib')
tags.discard('matplotlib')
print(tags)
