class Student :
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
        print("NAME:", self.name, "ROLL_NUMBER:", self.roll_no, "MARKS:", self.marks)
    def calculate_percentage(self):
        print(self.name," Your %age is:",(self.marks*100/500))

    

student=Student("SUPLEX_CITY",101,108)
student.display()
student.calculate_percentage()


#BANK ACCOUNT
class BankAccount:
    def __init__(self,Ac_name,Ac_no,Balance):
        self.Ac_name=Ac_name
        self.Ac_no=Ac_no
        self.Balance=Balance
    def deposit(self):
        new_bal=int(input("Enter Amount to be deposited:"))
        self.Balance+=new_bal
        print("New Balance :",self.Balance)
    def 




























































