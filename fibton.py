#m=int(input('enter a number: '))
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
#for i in range(m+1 ,0,-1):
    #print(fib(i))

#farenheight to celsius
def fahToCel(fahtemp):
    celciustemp=(5/9)*(fahtemp-32)
    return  f'temperature in celcius is {celciustemp}'
#C = 5/9 x (F - 32)
def celToFah(value,celciustemp):
    fahtemp=((celciustemp*9)/5)+32
    return  f'temperature in celcius is {celciustemp}'
# finaldo=['','turtle doves','french hens','calling birds','golden ring','geese a-laying','swams a swimming','maids a-making','ladies dancing','lords a-leaping','pippers piing', 'drummers drumming']
# days_words=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Nineth','Tenth','Eleventh','Twelveth']
# words=['','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']


def christmasSong():
    days_words=['Twelveth','Eleventh','Tenth','Nineth','Eighth','Seventh','Sixth','FifthDay','FourthDay','ThirdDay','SecondDay','FirstDay']
    words=['twelve','eleven','ten','nine','eight','seven','six','five','four','three','two','']
    i=0
    new=''
    finaldo=['drummers drumming','pippers pipping','lords a-leaping','ladies dancing','maids a-milking','swams a swimming','geese a-laying','golden rings','calling birds','French hens','turtle doves','']
    words.reverse()
    finaldo.reverse()
    days_words.reverse()
    while i<12:
        if i==0:
            position = days_words[i]
            print(f'On the {position} of christmas,\n My true love sent to me \n {finaldo[i]}' )
        else:
            position = days_words[i]
            print(f'On the {position} of christmas,\n My true love sent to me \n  {new}')
            new= new + '\n' + words[i] + ' ' + finaldo[i]
        print('And a partridge in a pear tree!')
        print()
        i=i+1
christmasSong()