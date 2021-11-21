import pathlib as pl,hashlib
import  os,sys,subprocess,sudo
# os.makedirs('C:\\users\\flemming eyong achem\\desktop\\database')
from datetime import datetime
matricule=input("Enter you Matricule: ")
# timestr=datetime.now().strftime('%Y%m%d-%H%M%S-%f')
dir_path=os.path.join('C:\\users\\flemming eyong achem\\desktop\\database',matricule)
folder=os.makedirs(dir_path)
# folder=os.path.dirname(os.path.abspath('C:\\users\\flemming eyong achem\\desktop\\database'))
# os.system('cd ./databases')
# os.system(f'cd C:\\users\\flemming eyong achem\\desktop\\database\\{matricule}')
# i have changed the working path for this project
# PycharmProjects\pythonProject
os.chdir(f'./{matricule}')
os.path.join(f'C:\\users\\flemming eyong achem\\desktop\\database\\{folder}',str(os.system(f'type nul>{matricule}.txt')))
# folder=os.path.join('C:\\users\\flemming eyong achem\\desktop\\database',str(os.system(f'type nul> {matricule}.txt')))
# my_file=os.path.join(folder,'{}.txt'.format(matricule))
# with open(os.path.join(dir_path,'B' + timestr),'w') as fp:
#     fp.write('Exact time is: ' + timestr)
# make the code above cross platform
# os.path.join(os.path.expanduser('~'),'Desktop')
# class Department:
#     programs=[]
#     def __init__(self, name):
#         self.name=name
# class Student(Department):
#     def __init__(self,name,matricule,dept,age):
#         self.name=name
#         self.matricule=matricule
#         self.dept=dept
#         self.age=age
#     def marks(self):
#         count=0
#         for i in range(0,5):
#             count += 1
#             with open(f'{matricule}.txt','w') as fp:
#                 score1=int(input(f'Enter score{count}: '))
#                 fp.write(score1 + '\n')

details=[]
with open(f'{matricule}.txt','w') as fp:
    name=input("Enter Your Name: ")
    name=hashlib.sha256(name.encode('ascii')).digest()
    details.append(name)
    details.append(matricule)
    fp.write(f'{matricule} : {name}\n')
newname=input("enter ur name in db: ")
print(details)
if hashlib.sha256(newname.encode('ascii')).digest()==details[0]:
    print('True')
else:
    print("incorrect password!!")
    n=int(input("""enter:\n 1:forgot password\n2:reset password\n"""))
    if n==1:
        past=input("Enter a new password: ")
        details[0]=hashlib.sha256(past.encode('ascii')).digest()
        print('password rest was successful')
        print(details)
    elif n==2:
        print("enter new pass: ")
        got=input()
        details[0] = hashlib.sha256(got.encode('ascii')).digest()
        print('password reset was successful')
        print(details)
    else:
        print('invalid command!!')










