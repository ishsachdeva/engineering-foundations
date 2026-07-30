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
- Completed Problem Set 3

### Personal Projects

- Completed Project 0 – Operational Impact Calculator
- Completed Project 1 – Decision Policy Classifier
- Completed Project 2 – Batch Case Scanner
- Completed Project 3 – Resilient Intake Validator

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

### Project 3

- Exception handling with `try` / `except`
- Input validation using reusable helper functions
- Separating data conversion from business-rule validation
- Designing generic functions through parameters
- Early return (guard clause) patterns
- Input sanitization using `strip()`
- Building resilient console applications
- Recognizing common algorithms across different implementations
- API thinking: separating function behavior from caller-specific data
- Applying single responsibility at the function level

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

## Key lessons from Project 3

- Exception handling should only be used for operations that can genuinely fail during execution (such as type conversion), not for ordinary business-rule validation.
- Validation logic and conversion logic are separate responsibilities and should remain separate.
- Generic helper functions are more reusable than hard-coded implementations because they receive context through parameters.
- Function names form part of the software contract and should accurately describe the validation rule they enforce.
- Input should be sanitized before validation when appropriate (for example, using `strip()` to reject whitespace-only input).
- Early returns simplify control flow by eliminating unnecessary nesting.
- Multiple problems that appear different often share the same underlying algorithm.
- Clean software design begins by identifying common patterns before writing code.
- Good helper functions hide implementation details so that `main()` remains simple and expressive.

---

## Confidence Rating after Project 3

Functions .................. 9/10
Variables .................. 8/10
Conditionals ............... 9/10
Loops ...................... 8/10
Input Validation ........... 9/10
Exception Handling ......... 7/10
Algorithm Design ........... 8/10
Debugging .................. 7/10
Git Basics ................. 7/10
Program Decomposition ...... 9/10
Code Organization .......... 8/10

---

## Current capability assessment

Independent Python ability: approximately **1.5 / 5**

I can independently design and implement small console applications that use functions, parameters, conditionals, loops, exception handling, reusable validation routines, and procedural decomposition. I understand how to separate conversion from validation, write generic helper functions, recognize repeated implementation patterns, and explain the reasoning behind many design decisions instead of only producing working code.

I still require mentorship when identifying opportunities for abstraction, reducing duplication before implementation, designing larger program architectures, reasoning about more complex algorithms, testing systematically, and applying advanced Python idioms. I have not yet learned collections in depth, file I/O, modules, testing frameworks, decorators, generators, or object-oriented programming, so my experience remains focused on well-structured procedural programs.

The objective remains unchanged: develop the ability to independently design, build, debug, test, explain, refactor, and maintain production-quality software systems with minimal AI assistance while steadily developing the engineering judgment required for software architecture.

---

## Overall Progress

The focus remains intentionally on building durable software engineering fundamentals rather than completing projects quickly.

Each project is expected to strengthen:

- Algorithmic thinking before coding.
- Reading and interpreting specifications carefully.
- Clean functional decomposition.
- Defensive input validation.
- Structured debugging.
- Recognition of reusable patterns.
- Clear separation of responsibilities.
- Writing maintainable, readable, and reusable code.

Progress is measured by improvements in engineering judgment and independent problem-solving ability—not by the number of completed projects or lines of code written.

---

## Repository Milestones

| Date | Milestone | Commit | Key Engineering Learning |
|------|-----------|--------|--------------------------|
| 30 Jul 2026 | Repository Initialized | Initial repository | Established Python development environment, Git workflow, virtual environment, and repository structure. |
| 30 Jul 2026 | Project 0 – Operational Impact Calculator | `83ddf91` | Learned functional decomposition, variables, calculations, returning values, and separating work into small functions. |
| 30 Jul 2026 | Project 1 – Decision Policy Classifier | `<commit>` | Learned business-rule implementation, conditionals, decision trees, and translating requirements into executable logic. |
| 30 Jul 2026 | Project 2 – Batch Case Scanner | `<commit>` | Learned loops, counters, accumulators, current-record variables, state management, execution tracing, and structured debugging. |
| 30 Jul 2026 | Project 3 – Resilient Intake Validator | `<commit>` | Learned reusable validation functions, exception handling, separation of conversion from validation, input sanitization, API-oriented function design, and recognizing common algorithms across multiple implementations. |

---

## Overall Engineering Progress

| Stage | Python Rating | Focus |
|--------|:-------------:|-------|
| Repository Created | **0.5 / 5** | Learning basic Python syntax and procedural programming. |
| After Project 0 | **0.7 / 5** | Writing simple functions and decomposing problems into smaller tasks. |
| After Project 1 | **0.9 / 5** | Implementing business rules using conditionals and structured decision logic. |
| After Project 2 | **1.0 / 5** | Managing program state with loops, counters, accumulators, and disciplined debugging. |
| After Project 3 | **1.5 / 5** | Designing reusable helper functions, understanding exception handling, separating responsibilities, and beginning to think in terms of software engineering patterns instead of individual code snippets. |

---

## Long-Term Objective

The purpose of this repository is **not** to accumulate completed projects.

Its purpose is to document the gradual development from beginner to software engineer through deliberate practice, rigorous code reviews, disciplined debugging, incremental improvement, and continuous reflection.

Every project should leave behind evidence of improved engineering judgment, cleaner code organization, stronger problem decomposition, and greater independence than the previous one.

Success will be measured by the ability to independently design, build, explain, test, debug, refactor, and maintain production-quality software systems with minimal AI assistance.