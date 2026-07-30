def main():
    case_id = get_nonempty_text("CaseId: ")
    amount = get_positive_float("Amount: ")
    age = get_nonnegative_integer("Age in days: ")
    priority = get_priority("Priority: ")

    print(f"Accepted: {case_id} | ${amount:.2f} | {age} days | {priority.upper()}")


def get_nonempty_text(prompt) :
    while True :
        text = input(prompt)
        if text.strip() != "":
            return text
        else:
            print("Please enter a non-empty string.")

def get_positive_float(prompt) :
    while True :
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
        
            print("Please enter number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

def get_nonnegative_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number

            print("Please enter a non-negative integer.")
        
        except ValueError:
            print("Please enter a valid integer.")

def get_priority(prompt):
    while True:
        priority = input(prompt).strip().lower()
        if priority in ["high", "medium", "low"]:
            return priority
        else:
            print("Please enter 'high', 'medium', or 'low'.")

main()