def computepay(hours,rate):
        
        hours = float(hours)
        rate = float(rate)

        if hours <= 40:
            pay = hours * rate
        else:
            pay_regular = 40 * rate
            overtime_hour = hours - 40
            pay_overtime = overtime_hour * 1.5 * rate
            pay = pay_regular + pay_overtime

        return pay
        
try:
    hours = input("Enter the numbers of hours worked: ")
    rate = input("Enter rate: ")
    salary = computepay(hours,rate)
    print("Your salary is:",salary)
except ValueError:
     print("Error, please enter numeric input")