import sys
import statistics
import uuid
from datetime import datetime

def main():
    args = []
    processed_args = process_arguments(sys.argv)
    
    identifier = uuid.uuid4()
    timestamp = datetime.now()
    count = len(processed_args)
    mean = statistics.mean(processed_args)
    median = statistics.median(processed_args)
    minimum = min(processed_args)
    maximum = max(processed_args) 
    rng = maximum - minimum

    print(f"Evidence ID: {identifier}")
    print(f"Created: {timestamp}")
    print(f"Observations: {count}")
    print(f"Mean: {mean:.2f} minutes")
    print(f"Median: {median:.2f} minutes")
    print(f"Minimum: {minimum:.2f} minutes") 
    print(f"Maximum: {maximum:.2f} minutes")
    print(f"Range: {rng:.2f} minutes")

def process_arguments(args):
    # Function to parse observations from input
    processed_args = []
    if len(args) <= 3:
        print("Too few arguments exiting min 3 required")
        sys.exit(1)
    for arg in args[1:]:
        try:
            processed_args.append(float(arg))
        except ValueError:
            print("Non numeric arguments exiting")
            sys.exit(1)
    return processed_args

if __name__ == "__main__":
    main()