class Employee:
    def __init__(self):
        self.wage        = 0
        self.hoursWorked = 0

    def calculate_pay(anythingIWantInHere):
        wage        = 1
        hoursWorked = 2
        anythingIWantInHere.wage = anythingIWantInHere.wage * wage
        return anythingIWantInHere.wage * anythingIWantInHere.hoursWorked
    
alice = Employee()
alice.wage        = 9.25
alice.hoursWorked = 35
"""prints 9.25"""
print(alice.wage) 