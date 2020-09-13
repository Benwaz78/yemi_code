
class Employee():
    pay_raise = 0.20

    # def __init__(self):
    #     print('This is an init method')

    def __init__(self, first_name, last_name, pay):
        self.fname = first_name
        self.lname = last_name
        self.p = pay
        self.em = self.fname+'.'+self.lname+'@alabiansolutions.com'
        self.email = self.em.lower()

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def salary(self):
        increase = self.pay_raise * self.p
        salary = increase + self.p
        return salary


class Developer(Employee):
    
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog = prog_lang

    def details(self):
        print('Here is your details:')
        print(f'{self.fname} {self.lname} {self.email} {self.salary()}')
    

d1 = Developer('Alabi', 'Adebayo', 2000, 'PHP')
d2 = Developer('Ope', 'Oyekunle', 2500, 'JS')
d3 = Developer('Anu', 'Oluwakpo', 1000, 'JAVA')
d4 = Developer('Jonathan', 'Ikwu', 700, 'Ruby')


class Manager(Developer):

    def __init__(self, first_name, last_name, pay, prog_lang, employee):
        super().__init__(first_name, last_name, pay, prog_lang)
        if employee is not None:
            self.employee = []
        else:
            self.employee = employee

    
    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    
    def list_emp(self):
        print('Here are list of Employee')
        for emp in self.employee:
            print(emp.full_name())

# var1 = None

# if var1 is not None:
#     print(var1)
# print(var1)

m1 = Manager('Bose', 'Lekpa', 4000, 'Mongo', [])

m1.add_emp(d1)
m1.add_emp(d2)
m1.add_emp(d3)
m1.add_emp(d4)
m1.remove_emp(d4)
print(len(m1.employee))
m1.list_emp()

