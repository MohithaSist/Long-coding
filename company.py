log_data=[1,'Mohitha','123',2,'manager']
signin_data=[]
class Signin:
    def __init__(self):
        self.id=int(input("Enter your id : "))
        signin_data.append(self.id)
        self.name=input("Enter your name : ")
        signin_data.append(self.name)
        self.password=input("Enter your password : ")
        signin_data.append(self.password)
        self.dept=input("Enter your department : ")
        signin_data.append(self.dept)
        self.man_id=int(input("Enter manager id " ))
        signin_data.append(self.man_id)
        self.ph=input("Enter phone number : ")
        signin_data.append(self.ph)
        self.role=input("Enter your role(manager/emp) : ")
        signin_data.append(self.role)
        print()
        Signin.Welcome(self)
        
    def Welcome(self):
        print("Successfully Signedin!")
        print("Welcome",self.name+'!')
        print()
        if self.role=='manager':
            print("1.Manager details")
            print("2.Employee details")
            detail=int(input("Enter no : "))
            if detail==1:
                man=Manager()
                man.man_det()
            elif detail==2:
                emp=Employee()
                emp.employee()
            
class Login:
    def __init__(self):
        self.id=int(input("Enter your id : "))
        self.name=input("Enter your name : ")
        self.password=input("Enter your password : ")
        self.man_id=int(input("Enter manager id :" ))
        self.role=input("Enter your role(manager/emp) : ")
    
        if self.id==log_data[0] and self.name==log_data[1] and self.password==log_data[2]:
            Login.Welcome(self)
        else:
            print("Please Enter valid login and password!")
        if self.role=='manager' and log_data[4]=='manager':
            emp=Employee()
            emp.employee()
    def Welcome(self):
        print()
        print("Welcome",self.name+'!')
        print()
            
class Employee:
    def __init__(self):
        self.l1=[]
    def employee(self):
        
        self.emp1={"Emp_id":1,"Name":'Anu',"Dept":"Accounts","Gender":"Female","DOB":"27/4/1990",
                   "Ph_no":123456,"Man_id":3}
        self.emp2={"Emp_id":2,"Name":'kohka',"Dept":"sales","Gender":"male","DOB":"2/8/1995",
                   "Ph_no":126266,"Man_id":1}
        self.emp3={"Emp_id":3,"Name":'chandu',"Dept":"finance","Gender":"male","DOB":"23/6/2000",
                   "Ph_no":827266,"Man_id":2}
        self.emp4={"Emp_id":4,"Name":'pinaya',"Dept":"marketing","Gender":"Female","DOB":"9/3/2000",
                   "Ph_no":13326647,"Man_id":1}
        
        if log_data[3]==1  :
            self.l1.append(self.emp2)
            self.l1.append(self.emp4)
        elif log_data[3]==2:
            self.l1.append(self.emp3)
        elif log_data[3]==3:
            self.l1.append(self.emp1)
            
        Employee.print_details(self)

    def print_details(self):
        for emp in self.l1:
            for value in emp.values():
                print(value)
            print()
        pro=Projects()
        pro.proj()
        
class Manager:
    def __init__(self):
        self.l1=[]
    def man_det(self):
        self.man1={"man_id":1,"Name":'Mohitha',"Dept":"HR","Gender":"Female","DOB":"22/10/2003",
                   "Ph_no":8237868}
        self.man2={"man_id":2,"Name":'Vicky',"Dept":"sales","Gender":"male","DOB":"2/8/2001",
                   "Ph_no":8181782}
        self.man3={"man_id":3,"Name":'harsh',"Dept":"finance","Gender":"male","DOB":"23/6/2000",
                   "Ph_no":166552}
        self.l1.append(self.man1)
        self.l1.append(self.man2)
        self.l1.append(self.man3)

        Manager.print_details(self)
    def print_details(self):
        for man in self.l1:
            for i in man.values():
                print(i)
            print()
        pro=Projects()
        pro.proj()
    
        
class Projects:
    def proj(self):
        if signin_data[4]==1 or log_data[3]==1:
            proj1="Mobile App Development"
            print(proj1)
        elif signin_data[4]==2 or log_data[3]==2:
            proj2="Application Management And Development"
            print(proj2)
        elif signin_data[4]==3 or log_data[3]==3:
            proj3="Product Details"
            print(proj3)


if __name__=="__main__":
    
    print("1.Create new account")
    print("2.Login")
    choice=int(input("Enter your choice(1/2) : "))
    if choice==1:
        sign=Signin()
        
    elif choice==2:
        log=Login()
    
