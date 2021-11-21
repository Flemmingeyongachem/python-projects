encrypted=input('Enter the cipher or encrypted message: ')
listed=[]
for x in encrypted:
    if x.isalpha():
        listed.append(x)
    if x.isspace():
        listed.append(x)
y=''
for x in listed:
    y=y+x
listed=y
print(listed[::-1])

