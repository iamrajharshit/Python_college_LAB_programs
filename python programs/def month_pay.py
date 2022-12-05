emp_name=input("Enter the emp name")
hrs_worked=int(input("Enter the hrs worked"))
pay_rate=int(input("Enter the pay rate per hr"))
weeks=int(input("Enter the no of weeks in a month"))

def month_pay(hrs_worked,pay_rate,weeks):
    m_pay=(hrs_worked*pay_rate*weeks)
    return m_pay
print("Emp name:",emp_name)
print("monthly pay=",month_pay(hrs_worked,pay_rate,weeks))
