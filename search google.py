import pywhatkit
# musician=input("Enter the musician's name(s):  eg wizkid ft drake ")
# musician=musician.split()
# musician='-'.join(musician)
# print(musician)
message='My name is Flemming Eyong Achem'
# print(f'searching {musician} on youtube!....')
# pywhatkit.search(musician)
text=pywhatkit.text_to_handwriting(message,rgb=[0,0,255])
print(text)
# pywhatkit.info('alphabet',lines=4)