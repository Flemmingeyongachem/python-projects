def checkBoomerang(list):
    posBoom=[]
    for item in range(len(list)-2):
        if((list[item]==list[item+2]) and (list[item]!=list[item+1])):
            posBoom.append([list[item],list[item+1],list[item+2]])
    count=0
    for elt in posBoom:
        if isinstance(elt,type(list)):
            count+=1
    return f'{count} boomerangs found, {posBoom}'
trial_list=[9, 5, 9, 5, 1, 1, 1]
trial_list1=[5, 6, 6, 7, 6, 3, 9]
trial_list2=[4, 4, 4, 9, 9, 9, 9]
trial_list3=[3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]
print(checkBoomerang(trial_list))
print(checkBoomerang(trial_list1))
print(checkBoomerang(trial_list2))
print(checkBoomerang(trial_list3))








# alternative form of the bomerang implimentation
# count=0
# for i in range(len(list) - 2):
#     if list[i] == list[i + 2] and list[i] != list[i + 1]:
#         count += 1
# return count












