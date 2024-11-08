def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...

    pay=0
    count=0
    for hour in range(hours_worked):
        count+=1
        if count <= standard_hours:
            pay+=regular_rate
        else:
            pay+=overtime_rate
    
    return pay


    
# # Code Example
# overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
# print(overtime_pay)
