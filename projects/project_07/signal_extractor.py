import re
import sys
from pathlib import Path
from datetime import datetime
import json

def main():
    
    input_path, output_path = validate(sys.argv)
    extract_signals(input_path, output_path)

def validate(input_arguments):
    
    if len(input_arguments)<3:
        print("ERROR: Too few arguments")
        sys.exit(1)

    if len(input_arguments)>3:
        print("ERROR: Too many arguments")
        sys.exit(1)

    input_path = Path(input_arguments[1])
    output_path = Path(input_arguments[2])
    
    if not input_path.exists():
        print("ERROR:Input file doesn't exist") 
        sys.exit(1)

    if input_path.is_dir():
        print("ERROR:Input file is a directory. Plz enter a valid filename")
        sys.exit(1)

    if output_path.is_file():
        print("ERROR:Output path is a file. Plz enter a valid directory")
        sys.exit(1)

    if not output_path.is_dir():
        print(f"Entered directory {input_arguments[2]} doesn't exist")
        decison = input(f"Create the folder named {input_arguments[2]} (y/n): ")
        if decison.lower() == "y" or decison.lower() == "yes":
            output_path.mkdir()
        else:
            sys.exit(1)
    
    return input_path, output_path

def extract_signals(input_file, output_dir):
    contract_references = []
    invoice_references = []
    amounts = []
    percents = []
    dates = []
    
    with open(input_file) as file:
        text = file.read()
    
    if matches := re.finditer(r"(\bCTR\b-\d{4,4})-\d{4,4}",text): 
        for match in matches:
            contract_references.append({"value": match.group(), "start_position": match.start()})
    
    if matches := re.finditer(r"(\bINV\b-\d{7,7})",text):
        for match in matches:
            invoice_references.append({"value": match.group(), "start_position": match.start()})

    if matches := re.finditer(r"(\$((?:(?:\d{1,3}(?:,\d{3})+)|\d+)(?:\.\d{2,})?))",text):
        for match in matches:
            amounts.append({"value": match.group(), "start_position": match.start()})

    if matches := re.finditer(r"(?<![\d\.])\d{1,2}\.?\d{1,2}%",text):
        for match in matches:
            num = match.group().rstrip("%")
            if float(num) > 0 and float(num) <=100:
                percents.append({"value": match.group(), "start_position": match.start()})

    if matches := re.finditer(r"\d{4}-\d{1,2}-\d{1,2}",text):     
        for match in matches:
            y,m,d = match.group().split("-")
            if int(m) > 0 and int(m) < 13 and int(d) > 0 and int(d) <= 31 and int(y) > 0:
                dates.append({"value": match.group(), "start_position": match.start()})

    contract_references = remove_duplicate_keys(contract_references, "value")
    invoice_references =  remove_duplicate_keys(invoice_references, "value")
    amount = remove_duplicate_keys(amounts, "value")
    percent = remove_duplicate_keys(percents, "value")
    date = remove_duplicate_keys(dates, "value")

    now = datetime.now()
    final_json = {
        "source_file": str(input_file),
        "extracted_at": now.isoformat(),
        "contracts": contract_references,
        "invoices": invoice_references,
        "amounts": amount,
        "percentages": percent,
        "dates": date
    }

    output_file = output_dir/"output.json"

    with open(output_file, "w") as file:
        json.dump(final_json, file, indent=4)

def remove_duplicate_keys(list_to_check, key):
    seen = set()
    unique_list = []

    for item in list_to_check:
        value = item[key]
        if value not in seen:
            seen.add(value)
            unique_list.append(item)

    return unique_list

if __name__ == "__main__":
    main()