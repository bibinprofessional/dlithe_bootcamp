class user:
    def __init__(self,fname,lname,dob,email):
        self.fname=fname
        self.lname=lname
        self.dob=dob
        self.email=email

    def fullname(self):
        print('Fullname of the user is ',self.fname+' '+self.lname)

    def age_above(self):
        if 2023-int(self.dob[-4:]) >55:
            print('Age above 55')
        else:
            print('Age below 55')


    def valid_email(self):
        if '@' in self.email:
            print('Valid Email')
        else:
            print('Invalid Email')


u=user('bibin','lal','29-02-2000','bibinasd')
u.fullname()
u.age_above()
u.valid_email()