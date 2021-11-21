import string
from reuserable import bcolors
print(f'{bcolors.HEADER}')

#code starts here
# stri=input("Enter a string: ")
def spinalCase(getstring):
    return getstring.replace(' ','-').lower()
# print(spinalCase(stri))
def tolatin(Astring):
    consonant_list=list(string.ascii_lowercase)
    # generating vowel path
    vowels=['a','e','i','o','u']
    #generating consonant list
    for x in consonant_list:
        if x in vowels:
            consonant_list.remove(x)
    Astring = list(Astring)
    if Astring[0].lower() in vowels:
        Astring.append('way')
        return ''.join(Astring)
    elif Astring[0].lower()  in consonant_list:
        if Astring[1].lower() in consonant_list:
            hold = [Astring[0], Astring[1]]
            for i in hold:
                Astring.remove(i)
            for i in hold:
                Astring.append(i)
            Astring.append('ay')
            return ''.join(Astring)
        else:
            hold=Astring[0]
            Astring.remove(hold)
            Astring.append(hold)
            Astring.append('ay')
            return ''.join(Astring)
    else:
        return 'The first letter of the word cannot be a number or symbol'
count=0
#we want ot run the program 3 times in order to test all the possibilities
while count<3:
    test_string = input('Enter the string: ')
    print(tolatin(test_string))
    count+=1





















