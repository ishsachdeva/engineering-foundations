def main():
    while True:
        try:
            exposure = float(input("Exposure: ").strip())
            confidence = int(input("Confidence: ").strip())
            
            while True:
                try:
                    customer_impact = input("Customer Impact: ".strip())
                    if customer_impact.strip().lower() == "yes" or customer_impact.strip().lower() == "y":
                        customer_impact = True
                        break
                    elif customer_impact.strip().lower() == "no" or customer_impact.strip().lower() == "n":
                        customer_impact = False
                        break
                    else:
                        raise ValueError
                except ValueError:
                    pass

            validate_case(exposure, confidence)
            break
        except ValueError:
            pass 
    
    classification = classify_case(exposure, confidence, customer_impact)
    print (f"Exposure: {exposure} Confidence: {confidence} Classification: {classification}")

def validate_case(exposure, confidence):
        
        if exposure < 0:
            raise ValueError
        if confidence <0 or confidence >100:
            raise ValueError

def classify_case(exposure, confidence, impact):
    if impact == True or exposure >= 100000:
        return "CRITICAL"
    elif exposure >=25000 and confidence >= 70:
        return "HIGH"
    elif confidence < 70:
        return "HUMAN REVIEW"
    else:
        return "STANDARD"

if __name__ == "__main__":
    main()