import sys
import csv
from pathlib import Path

def main():
    is_valid,output_path = validate_input(sys.argv)
    
    if is_valid == True:
        create_records(sys.argv[1], output_path)

def validate_input(args):
        
    if len(args) == 1:
        print("Too few arguments")
        sys.exit(1)
    if len(args) > 3:
        print("Too many arguments")
        sys.exit(1)

    if args[1].endswith(".csv") == False:
        print("Input file is not a .csv")
        sys.exit(1)

    input_path = Path(args[1])
    output_path = Path(args[2])

    if input_path.exists() == False:
        print ("Input File Doesn't Exist")
        sys.exit(1)

    if input_path.is_dir() == True:
        print ("Input File is a directory")
        sys.exit(1)

    if output_path.is_file() == True:
        print("The output refers to an existing file. Please provide a directory")
        sys.exit(1)

    if output_path.is_dir() == False:
        print(f"Entered directory {args[2]} doesn't exist")
        decison = input(f"Create the folder named {args[2]}(y/n): ")
        if decison.lower() == "y" or decison.lower() == "yes":
            output_path.mkdir()
        else:
            sys.exit(1)
    return True, output_path

def create_records(arg, output_path):
    findings_file = output_path/"findings.csv"
    rejected_file = output_path/"rejected_rows.csv"
    summary_file = output_path/"summary.txt"

    rows_processed, total_accepted, total_rejected = 0,0,0

    # Write headers to findings.csv
    with open(findings_file,"w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["case_id","exposure","confidence","customer_impact"])
        writer.writeheader()
    
    # Write headers to rejected_rows.csv
    with open(rejected_file,"w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["row_num","reject_reason"])
        writer.writeheader()

    # Read data from input file
    with open(arg) as file:
        # Define Reader
        reader = csv.DictReader(file)
        row_num = 1
        # Loop through reader for row data and row number
        for row_num, row in enumerate(reader, start=2):
            rejected = False
            reject_reason = ""

            # Validate data and save to variable
            if row["case_id"].strip() != "":
                case_id = row["case_id"]
            else:    
                rejected = True
                reject_reason = reject_reason + "Case ID Blank, "

            try:
                if float(row["exposure"].strip()) > 0:
                    exposure = row["exposure"]
                else:
                    raise ValueError
            except ValueError:
                rejected = True
                reject_reason = reject_reason + "Exposure is either less<0 or non numeric, "
            
            try:
                if float(row["confidence"].strip()) >= 0 and float(row["confidence"].strip()) <= 100:
                    confidence = row["confidence"]
                else:
                    raise ValueError
            except ValueError:
                rejected = True
                reject_reason = reject_reason + "Confidence is not a positive number between 0 & 100"

            if row["customer_impact"].lower() == "y"or row["customer_impact"].lower() == "yes" or row["customer_impact"].lower() == "n" or row["customer_impact"].lower() == "no" or row["customer_impact"].lower() == "true" or row["customer_impact"].lower() == "false":
                customer_impact = row["customer_impact"]
            else:
                rejected = True
                reject_reason = reject_reason + "Customer impact is not yes, no, True, False"

            # Write to findings
            if rejected == False:
                total_accepted = total_accepted + 1
                with open(findings_file,"a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["case_id","exposure","confidence","customer_impact"])
                    writer.writerow({"case_id" : case_id, "exposure" : exposure, "confidence" : confidence, "customer_impact" : customer_impact})

            # Write to rejected
            if rejected == True:
                total_rejected = total_rejected + 1
                with open(rejected_file, "a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["row_num","reject_reason"])
                    writer.writerow({"row_num" : row_num,"reject_reason" : reject_reason})

    with open(summary_file, "w") as file:
        file.write(f"Processed: {row_num-1} rows\nAccepted: {total_accepted}\nRejected:{total_rejected}\nFindings: {findings_file}\nRejected rows: {rejected_file}\nSummary: {summary_file}")

if __name__ == "__main__":
    main()
