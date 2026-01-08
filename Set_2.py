color={'red','green','white','yellow','blue'}
color2={'yellow','green','blue','purple','orange'}
print(color)
print(color2)

set_union=color.union(color2)
print(set_union)

set_intersection=color.intersection(color2)
print(set_intersection)

set_difference=color.difference(color2)
print(set_difference)

print('length of color set is:',len(color))
print('length of color2 set is:',len(color2))   

