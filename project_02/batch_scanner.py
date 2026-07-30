def main():
    #Input No. of Cases
    numbr_of_cases = int(input("Enter the number of cases: "))
    escalate, review, routine, total_exposure, largest_case_exposure, largest_case = calculate_cases(numbr_of_cases)

    print("\n--- Batch Summary ---")
    print(f"Escalate: {escalate}")
    print(f"Review: {review}")
    print(f"Routine: { routine}")
    print(f"Total exposure: {total_exposure:.2f}")
    print(f"Average exposure: {total_exposure/numbr_of_cases:.2f}")
    print(f"Largest case: {largest_case} ({largest_case_exposure:.2f})")


def calculate_cases(numbr_of_cases):
    largest_case_exposure = 0 
    largest_case = None
    total_exposure = 0 
    escalate = 0
    review = 0
    routine = 0
    i = numbr_of_cases
    j = 1

    while i != 0 :
        case_id = input("Enter the case ID: ") 
        while True :
            finincial_exposure = int(input("Enter Finincial Exposure: "))
            if finincial_exposure > 0: 
                break 
        
        while True :
            overdue_days = int(input("Enter Overdue Days: ")) 
            if overdue_days >= 0 : 
                break 
        
        if largest_case_exposure < finincial_exposure : 
            largest_case_exposure = finincial_exposure 
            largest_case = case_id 
        
        if finincial_exposure >= 50000 or overdue_days >= 30 : 
            status = "Escalate" 
            escalate = escalate + 1 
                
        elif finincial_exposure >= 10000 or overdue_days >= 10 :
            status = "Review" 
            review = review + 1
        
        else:
            status = "Routine" 
            routine = routine + 1 
            
        
        print (f"Case {j} Id: {case_id}")
        print (f"Exposure: {finincial_exposure}")  
        print (f"Days overdue: {overdue_days}") 
        print (f"Status: {status}") 
        
        i = i - 1
        j = j + 1
        
        total_exposure = total_exposure + finincial_exposure
    
    return escalate, review, routine, total_exposure, largest_case_exposure, largest_case

main()