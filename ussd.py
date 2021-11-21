
with open('C:\\users\\flemming eyong achem\\desktop\\data\\romeo.txt') as flem:
    lines=flem.readlines()
    word_list=[]
    for line in lines:
        word=line.strip()
        for i in word.split(' '):
            if not i in word_list:
                word_list.append(i)
    word_list.sort()
    # print(word_list)


#let me help a mate,
trial_list=[5,8,1,0,90]
trial_list2=[5,8,1,0,90]
#using the sort method
trial_list.sort()#sorts our original list
print(trial_list)
#using sorted() function
print(sorted(trial_list2))#this copies and gives a sorted list, but our original list is unchanged
#printing our original list
print(trial_list2)