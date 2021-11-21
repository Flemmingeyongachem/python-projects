import re
regExp=['$','#','%','@','%','^','=','&','*','(','_','!','/','+','-','*']
str_var=input("enter the string: ")
if not re.search('[$#%@%^&*(_!/)=+ - *]',str_var):#check for special symbols in string
    print('string must contain atleast one symbol')
else:
    lis_index=[[letter,str_var.index(letter)] for letter in str_var if letter in regExp]#remove all symbols and their resp index to alist
    print(f'our symbol lis and index is {lis_index}')
    #knowing that strings are immutable objects for us to reverse and maintain the pos of a letter we must covert string to mutable object
    list_str=[letter for letter in str_var if not letter in regExp]
    print(f'converted string to list: {list_str}')
    list_str.reverse()#reverse the list
    print( f' reversed list is {list_str}')
    # list_str[0],list_str[-1]=list_str[-1],list_str[0] # swap the first and last values
    #inserting the symbols back to their respective indices
    for x,y in lis_index:
        list_str.insert(y,x)
    print(f'new list with symbols in place: {list_str}')
    emp=''.join(list_str) #coverting our list item back to a string
    print( f'the final out put is {emp}')














