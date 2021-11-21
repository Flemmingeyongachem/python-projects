import calendar,reuserable,random
#the reusable module imported above contains a class of colors.
year=2021
month=8
list_colors=[reuserable.bcolors.HEADER,reuserable.bcolors.OKBLUE,reuserable.bcolors.BOLD,
             reuserable.bcolors.ENDC,reuserable.bcolors.OKGREEN,reuserable.bcolors.FAIL,reuserable.bcolors.OKCYAN
             ,reuserable.bcolors.WARNING]
for i in calendar.calendar(year):
    print(f'{random.choice(list_colors)}{i}',end='')
message='eloquently the version of the program changed when the version of python was upgraded.'
print()
for i in message:
    print(f'{random.choice(list_colors)}{i}',end='')
    print(f'{random.choice(list_colors)}{i}',end='')