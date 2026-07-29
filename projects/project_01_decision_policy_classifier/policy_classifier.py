def main():
    case_identifier = input("Case ID: ")
    financial_exposure = float(input("Financial Exposure: "))    
    evidence_confidence = float(input("Evidence Confidence: "))
    customer_impact = input("Customer impact? (yes/no): ").strip().lower()
    if customer_impact == "yes" or customer_impact == "y":
        customer_impact = "Yes"

    elif customer_impact == "no" or customer_impact == "n":
        customer_impact = "No"

    else:        
        print("Invalid input for customer impact. Please enter 'yes' or 'no'.")
        return
    
    classification = classify_case(financial_exposure, evidence_confidence, customer_impact)
    explanation = explain_decision(classification)

    print(f"Case: {case_identifier}")
    print(f"Status: {classification}")
    print(f"Reason: {explanation}") 


def classify_case(financial_exposure, evidence_confidence, customer_impact):
    if customer_impact == "Yes" or financial_exposure >= 100000:
        return "CRITICAL"
    elif financial_exposure >=25000 and evidence_confidence >= 70:
        return "HIGH"
    elif evidence_confidence < 70:
        return "HUMAN REVIEW"
    else:
        return "STANDARD"

def explain_decision(classification):
    match classification:
        case "CRITICAL":
            explanation = f"The case is classified as {classification} because either financial exposure is atleast 100,000 or customer impact is Yes"
            return explanation
        case "HIGH":
            explanation = f"The case is classified as {classification}  because financial exposure is at least $25,000 and confidence is at least 70."
            return explanation
        case "HUMAN REVIEW":
            explanation = f"The case is classified as {classification}  because confidence is below 70 and the case is not CRITICAL."
            return explanation        
        case _:
            explanation = f"The case is classified as {classification}  because it's not CRITICAL, not HIGH, and doesn't require HUMAN REVIEW."
            return explanation

if __name__ == "__main__":
    main()