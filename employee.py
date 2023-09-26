"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    salary = ''
    hourlywage = ''
    commission = ''
    total = 0

    def __init__(self, name: str):
        self.name = name
        self.salary = ''
        self.hourlywage = ''
        self.commission = ''
        self.total = 0

    def get_pay(self) -> int:
        return self.total

    def setSalary(self, contractValue: int):
        self.salary = 'monthly salary of {contractValue}'.format(contractValue = contractValue)
        self.total+=contractValue

    def setHourly(self,wage: int,  hours: int):
        self.salary = 'contract of {hours} hours at {wage}/hour'.format(hours = hours, wage = wage)
        self.total+=hours * wage

    def setBonusCommission(self,commissionValue: int):
        self.commission = 'and receives a bonus commission of {commissionValue}.'.format(commissionValue = commissionValue)
        self.total +=commissionValue

    def setContractCommission(self, commissionValue: int, number_of_contracts: int):
        self.commission = f'and receives a commission for {number_of_contracts} contract(s) at {commissionValue}/contract.'.format(number_of_contracts = number_of_contracts, commissionValue = commissionValue)
        self.total+= commissionValue * number_of_contracts

    def __str__(self):
        if (self.commission == ''):
            return '{name} works on a {salary}.  Their total pay is {total}.'.format(name = self.name, salary = self.salary, total = self.total)
        return '{name} works on a {salary} {commission}  Their total pay is {total}.'.format(name = self.name, salary = self.salary, commission = self.commission, total = self.total)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.setSalary(4000)
print(billie.get_pay())
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.setHourly(25, 100)
print(charlie.get_pay())
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.setSalary(3000)
renee.setContractCommission(200, 4)
print(renee.get_pay())
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.setHourly(25, 150)
jan.setContractCommission(220, 3)
print(jan.get_pay())
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.setSalary(2000)
robbie.setBonusCommission(1500)
print(robbie.get_pay())
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.setHourly(30, 120)
ariel.setBonusCommission(600)
print(ariel.get_pay())
print(str(ariel))
