from reuserable import bcolors
print(f'{bcolors.HEADER}')
def pallidrome(getstring):
    getstring_list = list(getstring)  # since strings are immutable, we conver the string to a mutable list
    indexfirst = getstring[0]  # get the index of the first char in the string
    indexlast = getstring[-1]  # get the last character in he string
    indexadder = getstring[-2]  # this is import,most pallidromic words have first char same as last in the word
    # so, to get the index of the last char u cant just use the string[-1],bec it will return 0,meaning
    # the last word is thesame as the first word,which is at position 0 in the string
    # net line below we map the first char in the list to its index and same to the last char
    indexlist = [[indexfirst, getstring.index(indexfirst)], [indexlast, getstring.index(indexadder) + 1]]
    mainlist = [indexfirst, indexlast]
    for x in mainlist:
        getstring_list.remove(x)
    getstring_list.reverse()
    for x, y in indexlist:
        getstring_list.insert(y, x)
    getstring_list.reverse()
    getstring_list = ''.join(getstring_list)
    if getstring_list == getstring:
        print(getstring_list)
        print("its a pallidrome")
    else:
        print(getstring_list)
        print("Not a pallidrome")
#calling our function


def checkPalli(getstring):
    revstr=list(getstring)
    revstr.reverse()
    getstring_list=list(getstring)
    revstr=''.join(revstr);getstring=''.join(getstring_list)
    if revstr==getstring:
        print('its a pallidrome')
    else:
        print('its not  a pallidrome')




def matchLetterToIndex(word):
    getstring_list=[]#creat an empty list
    for x in word:#iterating letters of word
        emp = [x, word.index(x)]#emp is a list comtaining the letter in the word and its index position
        if emp in getstring_list:#eg if the pair ['s',0] already exist in the list,we ..
            emp = [x, (getstring_list[-1])[1] + 1]#get the index of the last char before the repeated char,and add one to it.
        getstring_list.append(emp)# we append each char,index sublist to our list.
    return getstring_list #returning our requires list





def retCapitalized(getstring):
    app=[]#create an empty list
    for i in getstring:
        app.append(i)#append each word in the sentence to the list
    for i in range(len(app)):
        if '.' in app[-1]:#if the '.' is at the end of the string we ignore it by replacing it with ''
            app[-1]=app[-1].replace('.','')
        elif '.' in app[i]:#search for '.' in the string if present
            if app[i+1]==' ':#search for space after '.' if true
                app[i+2]=app[i+2].capitalize()#the index of '.' and' ',to get the next word,capitalise the word
            else:
                app[i+1]=app[i+1].capitalize()#else if just '.' and not '. ',index of '.'plus 1 to get the next word
                app[i]=app[i] +' '
        else:# if there are no '.' or '. ' in word simply capitalise the word
            app[0]=app[0].capitalize()
    return ''.join(app) + '.'#converting list to str object to form our new sentence.

#calling our function
# stringword = input('Enter a string: ')  # getting the input string
# print(retCapitalized(stringword))

def mixed(list_input):
    suml=0;str_list=[]
    for i in list_input:
        if isinstance(i,list):
            for j in i:
                if isinstance(j, int):
                    suml = suml + j
                elif isinstance(j, str):
                    str_list.append(j)
        elif isinstance(i,tuple):
            for k in i:
                if isinstance(k, int):
                    suml = suml + k
                elif isinstance(k, str):
                    str_list.append(k)
        else:
            if isinstance(i,int):
                suml=suml+i
            elif isinstance(i,str):
                str_list.append(i)
            else:
                print("no value of  type str or int in list")
    return f'sum of all the integers is {suml}',' '.join(str_list)
my_trial_list1=[[6,2,2,'type','tasklist',6],(4,3,2,'in'),8,4,4,'cmd']
# print(mixed(my_trial_list1))

my_trial_list=[[6,8,4,(6,6,5,4)],5,6,8,6,[5,6,7,'6'],6]
def countSame(list_input,count_int):
    count=0
    for i in list_input:
        if isinstance(i,list):
            for k in i:
                if isinstance(k,tuple):
                    for j in k:
                        if j == count_int:
                            count += 1
                elif k==count_int:
                    count+=1
        elif isinstance(i,tuple):
            for j in i:
                if j==count_int:
                    count+=1
        else:
            if i==count_int:
                count+=1
    return f'The input number {count_int} occurred {count} times in the data structure'
print(countSame(my_trial_list,6))



















# or
# result=''
# stringword=stringword.capitalize()
# stringword=stringword.split('.')
# for i in stringword:
#     result+=i[0].upper()+ i[1:] +'. '
# print(result[:])













# store = []
# # Collect string input from the user
# word = input("Enter word: ")
#
# for i in range(len(word)):
#     """loop that splits the string and returns a list with their indexes
#     :param len(word)
#     """
#     car = [word[i], i]
#     store.append(car)
# print("The string Characters and Indexes are: {}" .format(store))
#calling our function
# hey='lopd go to hell'
# print(hey.title())





