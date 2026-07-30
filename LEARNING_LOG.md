# Learning Log

## 30 July 2026

### Environment established

- Created a public GitHub repository named `engineering-foundations`
- Cloned the repository onto a second laptop
- Configured Python 3.12.10
- Created an isolated virtual environment
- Configured repository-specific Git identity
- Confirmed that the virtual environment is excluded from Git

---

## Current learning progress

### CS50P

- Completed Week 0
- Completed Week 1
- Completed Week 2

### Problem Sets

- Completed Problem Set 0
- Completed Problem Set 1
- Completed Problem Set 2

### Personal Projects

- Completed Project 0 – Operational Impact Calculator
- Completed Project 1 – Decision Policy Classifier
- Completed Project 2 – Batch Case Scanner

---

## Major concepts learned

### Project 0

- Functions
- Variables
- User input
- Numeric calculations
- Returning values
- Program decomposition

### Project 1

- Boolean expressions
- if / elif / else
- Business rule implementation
- Decision trees
- Basic input validation
- match-case

### Project 2

- while loops
- Loop control
- Counters
- Accumulators
- Current-record variables
- Tracking a running maximum
- Maintaining program state across loop iterations
- Separating algorithm design from implementation
- Manual debugging using execution tracing

---

## Key lessons from Project 2

- Every variable should have a single, well-defined responsibility.
- Variables that represent batch state should be initialized outside the loop.
- Current-record variables should only exist for one iteration.
- Counters, accumulators, and current-record variables solve different problems.
- Running totals should only be updated once per record.
- The original input should be preserved if it will be needed later.
- Reading the specification carefully prevents unnecessary engineering work.
- Debugging should follow a structured process:
  1. Fix syntax errors.
  2. Make the program execute.
  3. Verify correctness.
  4. Refactor only after correctness is established.

---

## Confidence Rating after Project 2

Functions .................. 8/10
Variables .................. 8/10
Conditionals ............... 8/10
Loops ...................... 7/10
Counters ................... 7/10
Accumulators ............... 7/10
Algorithm Design ........... 7/10
Debugging .................. 6/10
Git Basics ................. 6/10
Program Decomposition ...... 7/10

---

## Current capability assessment

Independent Python ability: approximately **1.0 / 5**

I can independently design and implement small console programs that use functions, conditionals, loops, counters, accumulators, and simple state management. I can usually translate a high-level algorithm into working Python code and debug straightforward syntax and logical errors with guidance.

I still rely on mentorship when designing cleaner program structures, reasoning about edge cases, identifying subtle logic bugs, and applying Python best practices. I have not yet learned collections, exception handling, file I/O, modules, testing, or object-oriented programming, so my ability is currently limited to small procedural programs.

The current objective remains unchanged: develop the ability to independently design, build, debug, test, explain, refactor, and maintain production-quality software systems with minimal AI assistance.

---

## Overall Progress

The focus is intentionally on building durable software engineering fundamentals rather than completing projects quickly. Every project is expected to reinforce algorithmic thinking, disciplined debugging, clean program structure, and incremental improvement before introducing more advanced concepts.