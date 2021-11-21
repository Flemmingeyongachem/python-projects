import pywhatkit
musician=input("Enter the musician's name(s):  eg wizkid ft drake ")
musician=musician.split()
musician='-'.join(musician)
print(musician)
print(f'searching {musician} on youtube!....')
pywhatkit.playonyt(musician)
