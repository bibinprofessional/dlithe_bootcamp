def login(users,u,p):
    for i in users:
        if i['name']==u and i['pass']==p:
            return True,i['id'],i['name']
    else:
        return False, None,None

def password_change(users,id):
    for i in users:
        if i['id']==id:
            new_pass=input('enter a new password :')
            i['pass']=new_pass
            print('password changed successfully')
            break
    

def username_change(users,id):
    for i in users:
        if i['id']==id:
            new_name=input('enter a new username :')
            i['name']=new_name
            print('username changed successfully')
            return i['name']
        
def display_user(users,id):
    for i in users:
        if i['id']==id:

            print()
            print('####################################')
            print('Username :',i['name'])
            print('Password :',i['pass'])
            print('####################################')
            print()


users=[
    {'id':1,'name':'bibin','pass':'1234'},
    {'id':2,'name':'varsha','pass':'2341'},
    {'id':3,'name':'srujan','pass':'4232'}
]



while True:
    print('*****************************************************')
    print()
    print('WELCOME')
    print()
    opt=input('press 1 to login :')
    if opt=='1':
        username=input('enter username :')
        password=input('enter password :')

        log,id,name=login(users,username,password)

        if log:
            while True:
                print('Welcome ',name)
                print('------------------------------------------------')
                print()
                option=input('press 1 to edit password, 2 to edit username, 3 to display details :')
                if option=='1':
                    password_change(users,id)
                elif option=='2':
                    name=username_change(users,id)
                elif option=='3':
                    display_user(users,id)
                else:
                    break
        
        else:
            continue

    
    else:
        continue