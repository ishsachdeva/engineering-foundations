def main():
    #take user input
    monthly_cases = int(input("Cases processed per month: "))
    current_time_per_case = float(input("Current time per case (in minutes): "))
    revised_time_per_case = float(input("Revised time per case (in minutes): "))
    hourly_labor_cost = float(input("Labor cost per hour: "))
    
    #calculate and save values
    minutes_saved = minutes_saved_per_case(current_time_per_case, revised_time_per_case)
    monthly_hours = monthly_hours_saved(monthly_cases,minutes_saved)
    monthly_savings = monthly_labor_savings(hourly_labor_cost, monthly_hours)
    yearly_savings = monthly_savings * 12

    #print results
    print(f"Minutes saved per case: {minutes_saved:.2f}")
    print(f"Monthly hours saved: {monthly_hours:.2f}")
    print(f"Monthly labor savings: ${monthly_savings:.2f}")
    print(f"Annual labor savings: ${yearly_savings:.2f}")

def minutes_saved_per_case(current, revised):
    return current - revised


def monthly_hours_saved(cases, minutes_saved):
    return (cases * minutes_saved)/60


def monthly_labor_savings(hourly_rate, monthly_hours_saved):
    return hourly_rate * monthly_hours_saved


if __name__ == "__main__":
    main()