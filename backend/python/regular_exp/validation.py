import re

class register_validate:
    def __init__(self):
        self.user_data=[]

    def validate_mail(self,email):
        format=re.compile(r"^\S+@\S+\.com$")
        if re.fullmatch(format,email):
            return True
        return False


    def validate_pass(self,password,name):
        format=re.compile(f"^[A-Z](?=.*[0-9])(?=.*[^a-zA-Z0-9])(?!.*{re.escape(name)}*).*$")
        if re.fullmatch(format,password):
            return True
        return False
    def validate_dob(self,dob):
        pass
    def validate_emp_id(self,emp_id):
        pass



v=register_validate()

name=input('enter name :')

email=input('enter mail id :')
if not v.validate_mail(email):
    print('Invalid Email format')

password=input('enter password :')
if not v.validate_pass(password,name):
    print('Invalid password format')

dob=input('enter dob :')
if not v.validate_dob(dob):
    print('Invalid dob format')

emp_id=input('enter emp_id :')
if not v.validate_emp_id(emp_id):
    print('Invalid emp_id format')

    


