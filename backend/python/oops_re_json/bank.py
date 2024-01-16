import json
import re
import os
import random


class Register:
    def __init__(self):
        try:
            file= open("oops_re_json/banking.json")
            dic=json.load(file)
            self.dic=dic
            self.admin=dic['admin_data'][0]
            self.user=dic["user_data"]
        except FileNotFoundError as e:
            print(e)

    def register(self):
        while True:
            print()
            name=input('Name : ')
            if self.validate_name(name):
                break

        while True:
            print()
            dob=input('Date of Birth : ')
            if self.validate_dob(dob):
                break

        while True:
            print()
            email=input('Email Id : ')
            if self.validate_email(email) and self.duplicate_email(email):
                break
        
        while True:
            print()
            password=input('Password : ')
            if self.validate_password(password):
                break
        
        self.user.append({"name":name,"dob":dob,"email":email,"password":password})
        with open("oops_re_json/banking.json", "w+") as file:
            json.dump(self.dic,file,indent=4)
    

    def validate_name(self,name):
        if name.isalpha():
            return True
        
        print('Invalid Name !!!')
        return False

    def validate_dob(self,dob):
        format = re.compile(r'^(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')

        if re.fullmatch(format,dob):
            year=int(dob[:4])
            month=int(dob[5:7])
            date=int(dob[8:10])

            if year>2024:
                print('Invalid Date of birth !!!')
                return False
            
            
            if month==(4 or 6 or 9 or 11):
                if date>30:
                    print('Invalid Date of birth !!!')
                    return False
                
            elif month==2:
                if self.leap(year):
                    if date>29:
                        print('Invalid Date of birth !!!')
                        return False
                else:
                    if date>28:
                        print('Invalid Date of birth !!!')
                        return False
            
            return True
        else:
            print('Invalid Date of birth !!!')
            return False
        
    def validate_email(self,email):
        
        format=re.compile(r"^\S+@\S+\.com$")
        if re.fullmatch(format,email):
            return True
        else:
            print('Invalid email !!!')
            return False
        
    def duplicate_email(self,email):
        if len(self.user)>0:
            for i in self.user:
                if i['email']==email:
                    print('Email already present !!!')
                    return False
            return True
        else:
            return True
        
    def validate_password(self,password):
        format = re.compile(r'^.{8,}$')
        if re.fullmatch(format,password):
            return True
        else:
            print('Password must contain minimum 8 characters !!!')
            return False
        
    def leap(self,year):
        if (year % 400 == 0) and (year % 100 == 0):
            return True

        elif (year % 4 ==0) and (year % 100 != 0):
            return True

        else:
            return False

class Login(Register):
    def login(self):
        
        while True:
            print()
            email=input('Email Id : ')
            password=input('Password : ')
            data,bool=self.check_credentials(email,password)
            if bool:
                break

        return data
    
    def check_credentials(self,email,password):
        if self.admin['email']==email and self.admin['password']==password:
            return self.admin,True
        
        elif len(self.user)>0:
            for i in self.user:
                if i['email']==email and i['password']==password:
                    return i,True
            print('Invalid Credentials')
            return None,False
        else:
            print('Invalid Credentials')
            return None,False


class Banking:
    def __init__(self,email):
        try:
            file= open("oops_re_json/banking.json")
            dic=json.load(file)
            self.dic=dic

            self.user=dic['user_data']
            for i in self.user:
                if i['email']==email:
                    self.data=i
                    if self.check_account():
                        self.acc_name=i['banking']['acc_name']
                        self.acc_no=i['banking']['acc_no']
                        self.acc_bal=i['banking']['acc_bal']
                        self.transaction_pin=i['banking']['transaction_pin']
                    else:
                        self.acc_name,self.acc_no,self.acc_bal,self.transaction_pin=None,None,None,None
                    break
        
        except FileNotFoundError as e:
            print(e)

    
    def create_account(self):
        if self.check_account():
            print('account already exits !!!')
        
        else:
            acc_name=input('enter account holder name : ')
            ran_num=random.randint(1000,9999)
            acc_no="1000cbank"+str(ran_num)
            acc_bal=0
            transaction_pin=input('Enter transaction pin :')
            self.data['banking']={"acc_name":acc_name,"acc_no":acc_no,"acc_bal":acc_bal,"transaction_pin":transaction_pin}

            with open("oops_re_json/banking.json", "w+") as file:
                json.dump(self.dic,file,indent=4)

            print('Bank account created successfully ')

    def display_account(self):
        if self.check_account():
            print('ACCOUNT DETAILS')
            print()
            print('Acc holder Name    : ',self.acc_name)
            print('Acc number         : ',self.acc_no)
            print('Acc balance        : ',self.acc_bal)
            print('Transaction pin    : ',self.transaction_pin)
            print()
        else:
            print('No bank account found')

    def deposit(self):
        if self.check_account():
            amount=int(input('Enter amount : '))
            a_no=input('Enter account number : ')
            t_pin=input('Enter transaction pin : ')

            if a_no==self.acc_no and t_pin==self.transaction_pin:
                self.acc_bal=str(int(self.acc_bal)+amount)

                self.data['banking']['acc_bal']=self.acc_bal

                with open("oops_re_json/banking.json", "w+") as file:
                    json.dump(self.dic,file,indent=4)

                print(f'Deposit Successfull !!! The current balance of {self.acc_no} is {self.acc_bal}')


                
            
            else:
                print('Invalid data !!!')
        
        else:
            print('No bank account found')

    def withdraw(self):
        if self.check_account():
            amount=int(input('Enter amount : '))
            a_no=input('Enter account number : ')
            t_pin=input('Enter transaction pin : ')

            if a_no==self.acc_no and t_pin==self.transaction_pin:
                if amount<int(self.acc_bal):
                    self.acc_bal=str(int(self.acc_bal)-amount)

                    self.data['banking']['acc_bal']=self.acc_bal
                    
                    with open("oops_re_json/banking.json", "w+") as file:
                        json.dump(self.dic,file,indent=4)
                    
                    print(f'Deposit Successfull !!! The current balance of {self.acc_no} is {self.acc_bal}')
                else:
                    print('Insufficient Balance !!!')
            
            else:
                print('Invalid data !!!')
        
        else:
            print('No bank account found')



    def check_account(self):
        if 'banking' in self.data:
            return True
        return False
    
        


class Page(Login):

    def landing(self):
        os.system('cls')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        print('                        WELCOME')
        print()
        while True:
            print()
            opt1=input('1 => login,\n2 => register,\ne => exit\nPress : ')
            if opt1=='1':
                data=self.login()
                if data['name']=='admin':
                    self.adminpage(data)
                else:
                    self.userpage(data)

            elif opt1=='2':
                self.register()
                self.landing()
            
            elif opt1==('e' or 'E'):
                quit()

            else:
                print('Invalid Input !!!')
                print()

    
    def adminpage(self,data):
        os.system('cls')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        print("                       Welcome ",data['name'])
        print()
        while True:
            print()
            opt2=input('1 => display admin details,\n2 => display user details,\nb => go back,\ne => exit\nPress : ')
            if opt2=='1':
                print()
                print('ADMIN DETAILS')
                print()
                print('Name          : ',data['name'])
                print('Email         : ',data['email'])
                print('Password      : ',data['password'])
                print()

                opt3=input('Press any key to go back : ')
                if opt3:
                    continue



            elif opt2=='2':
                print()
                print('USER DETAILS')
                print()
                for i in self.user:
                    print('Name          : ',i['name'])
                    print('Date of birth : ',i['dob'])
                    print('Email         : ',i['email'])
                    print('Password      : ',i['password'])
                    print()
                
                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2==('b' or 'B'):
                break

            elif opt2==('e' or 'E'):
                quit()

            else:
                print('Invalid Input !!!')
                continue

    def userpage(self,data):
        os.system('cls')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        print("                       Welcome ",data['name'])
        print()
        while True:
            print()
            opt2=input('1 => display details,\n2 => banking,\nb => go back,\ne => exit\nPress : ')
            if opt2=='1':
                print()
                print('USER DETAILS')
                print()
                print('Name          : ',data['name'])
                print('Date of birth : ',data['dob'])
                print('Email         : ',data['email'])
                print('Password      : ',data['password'])
                print()

                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2=='2':
                self.bankingpage(data)

            elif opt2==('b' or 'B'):
                break

            elif opt2==('e' or 'E'):
                quit()

            else:
                print('Invalid Input !!!')
                continue

    def bankingpage(self,data):
        os.system('cls')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print()
        print("                 Welcome "+str(data['name'])+", To C-bank")
        print()
        while True:
            print()
            b=Banking(data['email'])
            opt2=input('1 => display account details,\n2 => create new bank account,\n3 => deposit,\n4 => withdraw,\nb => go back,\ne => exit\nPress : ')
            print()
            if opt2=='1':
                b.display_account()
                print()
                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2=='2':
                b.create_account()
                print()
                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2=='3':
                b.deposit()
                print()
                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2=='4':
                b.withdraw()
                print()
                opt3=input('Press any key to go back : ')
                if opt3:
                    continue

            elif opt2==('b' or 'B'):
                break

            elif opt2==('e' or 'E'):
                quit()

            else:
                print('Invalid Input !!!')
                continue
            



            


p=Page()
p.landing()