import re
import json

class wrapper:
    def homewrap(fun):
        def wrap_fun(*args, **kwargs): 
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print()
            print('                        WELCOME')
            print()
            res=fun(*args, **kwargs)
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return res
        return wrap_fun
    
    def userwrap(fun):
        def wrap_fun(*args, **kwargs): 
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print()
            res=fun(*args, **kwargs)
            print()
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return res
        return wrap_fun
    
class Register:
    def __init__(self):
        file1= open("oops_re_json/user_data.json")
        d=json.load(file1)
        self.d=d
        self.admin=d['admin_data'][0]
        self.data=d["user_data"]
    

    def regi(self):
        name=input('UserName : ')
        while True:
            dob=input('Date of Birth : ')
            if self.validate_dob(dob):
                break

        while True:
            email=input('Email Id : ')
            if self.validate_email(email) and self.duplicate_email(email):
                break

        while True:
            password=input('Password : ')
            if self.validate_password(password):
                break
        
        self.data.append({"name":name,"dob":dob,"email":email,"password":password})
        with open("oops_re_json/user_data.json", "w+") as file:
            json.dump(self.d,file,indent=4)


    def validate_dob(self,dob):
        format = re.compile(r'^(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
        if re.fullmatch(format,dob):
            return True
        else:
            print('Invalid Date of birth')
            return False

    def duplicate_email(self,email):
        if len(self.data)>0:
            for i in self.data:
                if i['email']==email:
                    print('Email already present')
                    return False
            return True
        else:
            return True

    def validate_email(self,email):
        
        format=re.compile(r"^\S+@\S+\.com$")
        if re.fullmatch(format,email):
            return True
        else:
            print('Invalid email')
            return False

    def validate_password(self,password):
        format = re.compile(r'^.{8,}$')
        if re.fullmatch(format,password):
            return True
        else:
            print('Password must contain minimum 8 characters')
            return False
        
class Login(Register):
    def log(self):
        while True:
            email=input('Email Id : ')
            password=input('Password : ')
            u,bool=self.check_credentials(email,password)
            if bool:
                break

        return u
    
    def check_credentials(self,email,password):
        if self.admin['email']==email and self.admin['password']==password:
            return self.admin,True
        
        elif len(self.data)>0:
            for i in self.data:
                if i['email']==email and i['password']==password:
                    return i,True
            print('Invalid Credentials')
            return None,False
        else:
            print('Invalid Credentials')
            return None,False

            
class landing(Login):

    @wrapper.homewrap
    def home(self):
        opt1=input('1 => login,\n2 => register\nPress : ')
        if opt1=="1":
            print()
            u=self.log()
            if u['name']=='admin':
                self.adminpage(u)
            else:
                self.user(u)
            print()

        elif opt1=="2":
            print()
            self.regi()
            self.home()
            print()

        else:
            print()
            print('Invalid Input')
            self.home()

    @wrapper.userwrap
    def user(self,u):
        print("                       Welcome ",u['name'])
        print()
        opt2=input('1 => display details,\n2 => Tasks\nPress : ')
        if opt2=='1':
            print()
            print('USER DETAILS')
            print()
            print('Name          : ',u['name'])
            print('Date of birth : ',u['dob'])
            print('Email         : ',u['email'])
            print('Password      : ',u['password'])
            print()

        else:
            print('Invalid Input')

    @wrapper.userwrap
    def adminpage(self,u):
        print("                       Welcome ",u['name'])
        print()
        opt2=input('1 => display admin details,\n2 => display user details\nPress : ')
        if opt2=='1':
            print()
            print('ADMIN DETAILS')
            print()
            print('Name          : ',u['name'])
            print('Email         : ',u['email'])
            print('Password      : ',u['password'])
            print()

            opt3=input('Press any key to go back')
            if opt3:
                self.adminpage(u)



        elif opt2=='2':
            print()
            print('USER DETAILS')
            print()
            for i in self.data:
                print('Name          : ',i['name'])
                print('Date of birth : ',i['dob'])
                print('Email         : ',i['email'])
                print('Password      : ',i['password'])
                print()
            
            opt3=input('Press any key to go back : ')
            if opt3:
                self.adminpage(u)

        else:
            self.adminpage(u)
            print('Invalid Input')



l=landing()
l.home()