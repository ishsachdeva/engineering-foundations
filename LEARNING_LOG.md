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
- Completed Week 3
- Completed Week 4
- Completed Week 5
- Completed Week 6

### Problem Sets

- Completed Problem Set 0
- Completed Problem Set 1
- Completed Problem Set 2
- Completed Problem Set 3
- Completed Problem Set 4
- Completed Problem Set 5
- Completed Problem Set 6

### Personal Projects

- Completed Project 0 – Operational Impact Calculator
- Completed Project 1 – Decision Policy Classifier
- Completed Project 2 – Batch Case Scanner
- Completed Project 3 – Resilient Intake Validator
- Completed Project 4 – Evidence Enricher
- Completed Project 5 – Decision Engine Test Harness
- Completed Project 6 – Evidence Processing Pipeline
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

### Project 4

- Reading command-line arguments using `sys.argv`
- Procedural data-processing pipelines
- Using Python standard library modules (`statistics`, `uuid`, `datetime`)
- Converting external string input into typed data
- Reusable preprocessing functions
- Exception-driven type conversion
- Guard clauses for argument validation
- Computing summary statistics using the standard library
- Reusing computed values instead of unnecessary recalculation
- Beginning to reason about API naming and function contracts

### Project 5

- Unit testing using `pytest`
- Behaviour-driven testing
- Specification-first test design
- Boundary value analysis
- Equivalence class thinking
- Regression testing
- Exception testing using `pytest.raises`
- Designing pure functions
- Separating business logic from user interaction
- Understanding software behaviour through automated tests
- Viewing tests as executable specifications
- Beginning to design software for testability rather than adding tests afterwards

### Project 6

- Reading and writing CSV files using `csv.DictReader` and `csv.DictWriter`
- Working with filesystem paths using `pathlib.Path`
- Command-line validation for files and directories
- Distinguishing filesystem state from API contracts
- Designing explicit validation pipelines
- Processing datasets record-by-record
- Producing multiple output artifacts from a single processing pass
- Recording multiple validation failures for a single record
- Preserving source row numbers using `enumerate()`
- Applying exceptions for business-rule validation
- Beginning to reason about filesystem APIs instead of memorizing functions

### Project 7

- Reading and writing JSON using the `json` module
- Extracting structured information using regular expressions
- Using `re.finditer()` to preserve match positions
- Building structured JSON documents from extracted data
- Working with timestamps using `datetime`
- Distinguishing extraction from validation
- Removing duplicate records while preserving first occurrence order
- Beginning to reason about token boundaries instead of only matching patterns
- Introduction to lookbehind assertions for context-sensitive matching

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

## Key lessons from Project 4

- Command-line arguments are external input and should always be treated as untrusted data.
- Parsing, validation, conversion, and computation are separate responsibilities.
- Python exceptions should replace manual type checking when performing type conversions.
- Standard library functions should be preferred over custom implementations whenever appropriate.
- Good software engineering often means composing reliable building blocks instead of writing everything manually.
- Function names communicate intent and should be chosen deliberately.
- Refactoring requires verifying every use of renamed variables to avoid introducing defects.
- Code reviews frequently involve trade-offs rather than absolute right or wrong answers.
- Good engineering discussions focus on reasoning and maintainability rather than personal preference.

---

## Key lessons from Project 5

- Tests should be derived directly from the specification rather than from arbitrary examples.
- Behaviour is the software contract; implementation details are free to change.
- A function either returns a value or raises an exception—it never returns an exception.
- Automated tests protect against future regressions rather than simply proving today's implementation works.
- Boundary values deserve explicit attention because defects frequently occur at decision thresholds.
- Designing pure functions naturally improves software testability.
- Separating business logic from user interaction produces cleaner and more maintainable software.
- Passing tests increase confidence but never prove software is completely correct.
- Testing is not a separate activity—it influences software design itself.
- Well-designed software becomes easier to explain, modify, and verify.

## Key lessons from Project 6

- Filesystem APIs only describe the current state of the filesystem; they cannot infer user intent.
- API contracts should be explicit instead of relying on heuristics whenever possible.
- Validation should establish assumptions before accessing dependent data.
- Exceptions can represent business-rule violations in addition to conversion failures.
- Traceability is an engineering feature; preserving original row numbers simplifies debugging.
- A solution can be correct while still containing maintainability problems.
- Repeated patterns should first be recognized before deciding whether they deserve abstraction.
- Resource lifetime matters; repeatedly opening and closing files works but does not scale well.

## Key lessons from Project 7

- Parsing and validation are different responsibilities and should remain separate whenever practical.
- Regular expressions are effective at identifying candidate tokens but are often the wrong place to enforce complex business rules.
- Structured data extraction is easier to maintain when processing follows distinct stages: extraction, validation, deduplication, and serialization.
- Context matters in parsing; token boundaries are just as important as the token pattern itself.
- Lookaround assertions allow surrounding context to be validated without becoming part of the matched result.
- Building reliable regular expressions requires adversarial testing using invalid, boundary, and malformed inputs rather than only successful examples.
- Correct software should still be challenged with additional edge cases because passing initial tests does not imply robustness.
- JSON is a serialization format with a limited set of supported data types; Python objects often require conversion before serialization.
- Good engineering discussions increasingly involve deciding which responsibility belongs in regex and which belongs in program logic.

---

## Biggest mindset shifts (Project 5)

- I now begin by understanding the specification before thinking about implementation.
- I increasingly think in terms of behavioural categories instead of isolated examples.
- I have started viewing tests as executable specifications rather than verification scripts.
- I understand that software should be designed to be testable instead of forcing tests around poor designs.
- I now separate user interaction from business logic almost instinctively.

## Biggest mindset shifts (Project 6)

- I now begin by understanding the specification before thinking about implementation.
- I increasingly think in terms of behavioural contracts instead of isolated examples.
- I now question what an API actually guarantees instead of assuming what I want it to do.
- I distinguish between implementation decisions and software contracts.
- I increasingly separate filesystem state from user intent.
- I now spend more time reasoning about program behaviour before modifying code.
- I have become more comfortable discussing engineering trade-offs instead of searching for a single "correct" implementation.

## Biggest mindset shifts (Project 7)

- I increasingly distinguish between identifying candidate data and validating business rules.
- I now think of parsing as a sequence of processing stages rather than as a single regular expression.
- I have become more deliberate about deciding which responsibilities belong in regex and which belong in Python code.
- I increasingly design small processing pipelines instead of writing one continuous procedural solution.
- I now challenge my own implementations by intentionally constructing invalid and boundary test cases instead of assuming successful examples are sufficient.
- I have started thinking about token boundaries and parsing context instead of only matching text patterns.
---

## Recurring Mistakes

Current recurring patterns observed:

- Initially attempting to manually verify conditions already guaranteed by Python instead of trusting language features.
- Occasionally optimizing before fully understanding the data flow.
- Spending excessive time searching for the "perfect" name instead of selecting a clear, defensible one.
- Sometimes beginning implementation before validating every assumption against the specification.
- Occasionally overlooking small defects introduced during refactoring (for example, renamed variables in return statements).
- Occasionally focusing on individual examples before identifying every behavioural category required by the specification.
- Sometimes reasoning about boundary values before reasoning about the expected business behaviour.
- Sometimes combining multiple validation concerns into a single conditional instead of validating one assumption at a time.
- Frequently recognizing duplicated implementation patterns only after they have already been written.
- Occasionally focusing on making the current implementation work before considering long-term maintainability.
- Sometimes attempts to solve parsing problems entirely within regular expressions before considering whether simpler validation logic would produce a clearer design.
- Occasionally focuses on making individual patterns work before stepping back to define the overall parsing strategy.
- Still tends to discover reusable abstractions after implementation rather than recognizing them during design.
- Occasionally spends excessive time perfecting individual implementation details before confirming that the overall architecture is sound.
- Still developing intuition for token boundaries, parser context, and where responsibility should be divided between extraction and validation.

---

## Emerging Strengths

- Reads feedback carefully instead of blindly applying suggestions.
- Challenges design decisions using logical reasoning.
- Increasingly reasons about program execution before writing code.
- Comfortable decomposing procedural programs into small helper functions.
- Makes good use of Python's standard library instead of reinventing existing functionality.
- Shows growing curiosity about software engineering decisions instead of focusing only on syntax.
- Increasingly reasons from specifications instead of implementations.
- Better at predicting program behaviour before execution.
- Beginning to defend engineering decisions using trade-offs rather than searching for one "correct" answer.
- Treats testing as part of software design rather than post-development verification.
- Increasingly reasons about API contracts instead of only Python syntax.
- Frequently challenges assumptions instead of immediately implementing solutions.
- Better at tracing program execution before changing code.
- Increasingly considers edge cases before implementation.
- Growing ability to explain *why* an implementation works instead of only *how* it works.
- Beginning to think in terms of pipeline architecture rather than sequential scripts.
  - Increasingly separates software into distinct processing stages instead of solving everything in a single block of logic.
- Begins challenging whether a responsibility belongs in parsing, validation, or serialization before implementing it.
- More willing to question proposed solutions when they do not align with the intended design.
- Increasingly builds adversarial test cases to expose defects instead of relying only on successful examples.
- Growing understanding that software design decisions often involve responsibility allocation rather than algorithm selection.
- Becoming more comfortable reasoning about parser behaviour by tracing how the matching engine evaluates input.

---

## Confidence Rating after Project 6

Functions .................. 8/10
Variables .................. 7/10
Conditionals ............... 8/10
Loops ...................... 8/10
Input Validation ........... 9/10
Exception Handling ......... 8/10
Command-line Arguments ..... 8/10
Standard Library Usage ..... 7/10
Program Decomposition ...... 8/10
Debugging .................. 8/10
Code Organization .......... 8/10
Engineering Reasoning ...... 9/10
Testing .................... 7/10
Behavioural Testing ........ 7/10
Specification Reading ...... 9/10
Regression Thinking ........ 7/10

---

## Current capability assessment

### Python

Independent Python ability: **2.0 / 5**

Project 7 demonstrated growing confidence using Python's standard library, regular expressions, JSON serialization, and structured data processing.

I increasingly distinguish between parsing, validation, deduplication, and serialization as separate responsibilities rather than combining them into one implementation.

I still require mentorship when recognizing reusable abstractions early, designing reusable modules, writing object-oriented software, organizing larger codebases, and using more advanced Python language features naturally without experimentation.

### Software Engineering

Current Software Engineering ability: **2.3 / 5**

Project 7 reinforced improvements in engineering reasoning rather than Python syntax.

I increasingly reason about responsibility allocation, processing stages, parsing strategy, validation boundaries, and data representation before implementation.

I still require mentorship when identifying abstractions before implementation, designing cohesive components, evaluating long-term maintainability, and making architectural trade-offs across larger systems.

### Software Architecture

No rating increase.

Project 7 showed early evidence of thinking in terms of processing pipelines and responsibility separation.

However, I have not yet demonstrated sustained architectural reasoning involving modular boundaries, interfaces, dependency management, extensibility, coupling, cohesion, or system-level design decisions.

The long-term objective remains unchanged: independently design, build, debug, explain, refactor, test, and maintain production-quality software systems while steadily developing software architecture judgement.
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
- Designing software for testability.
- Engineering judgment through deliberate code reviews and design discussions.

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
| 31 Jul 2026 | Project 4 – Evidence Enricher | `<commit>` | Learned command-line argument processing, standard library usage (`statistics`, `uuid`, `datetime`), procedural data pipelines, exception-driven conversion, and iterative API design through code reviews. |
| 1 Aug 2026 | Project 5 – Decision Engine Test Harness | `<commit>` | Learned specification-first testing, behavioural reasoning, regression prevention, boundary-value analysis, exception testing, pure-function design, and designing software around testability.
| 2 Aug 2026 | Project 6 – Evidence Processing Pipeline | `<commit>` | Learned CSV processing, `pathlib`, filesystem validation, API contracts, traceability, pipeline-oriented processing, and disciplined debugging through iterative engineering reviews. |
| 4 Aug 2026 | Project 7 – Signal Extractor | `<commit>` | Learned JSON serialization, regular-expression based extraction, parser pipeline design, token boundaries, lookaround assertions, duplicate elimination, and separating extraction from validation. |
---

## Overall Engineering Progress

| Stage | Python Rating | Software Engineering | Architecture | Focus |
|--------|:-------------:|:--------------------:|:------------:|-------|
| Repository Created | **0.5 / 5** | **0.5 / 5** | **0.5 / 5** | Learning Python syntax and procedural programming fundamentals. |
| After Project 0 | **0.7 / 5** | **0.7 / 5** | **0.6 / 5** | Functional decomposition, variables, calculations, and simple procedural design. |
| After Project 1 | **0.9 / 5** | **1.0 / 5** | **0.7 / 5** | Translating specifications into business rules and structured decision logic. |
| After Project 2 | **1.0 / 5** | **1.3 / 5** | **0.9 / 5** | Managing state, structured debugging, and recognizing algorithmic patterns. |
| After Project 3 | **1.5 / 5** | **1.6 / 5** | **1.0 / 5** | Reusable validation routines, exception handling, and cleaner procedural decomposition. |
| After Project 4 | **1.5 / 5** | **1.8 / 5** | **1.2 / 5** | Standard library usage, command-line processing, API reasoning, and stronger engineering discussions. |
| After Project 5 | **1.8 / 5** | **2.1 / 5** | **1.2 / 5** | Specification-first development, behavioural testing, regression prevention, pure functions, and stronger engineering reasoning.
| After Project 6 | **2.0 / 5** | **2.3 / 5** | **1.2 / 5** | CSV processing, filesystem reasoning, API contracts, structured validation, pipeline-oriented design, and stronger debugging discipline. |
| After Project 7 | **2.0 / 5** | **2.3 / 5** | **1.2 / 5** | JSON serialization, regular-expression based parsing, token-boundary reasoning, separation of extraction from validation, parser pipeline thinking, and more disciplined engineering discussions around responsibility allocation. |
---

## Long-Term Objective

The purpose of this repository is **not** to accumulate completed projects.

Its purpose is to document the gradual development from beginner to software engineer through deliberate practice, rigorous code reviews, disciplined debugging, incremental improvement, and continuous reflection.

Every project should leave behind evidence of improved engineering judgment, cleaner code organization, stronger problem decomposition, greater architectural thinking, increased software quality, and increased independence compared to the previous project.

Success will be measured by the ability to independently design, build, explain, test, debug, refactor, and maintain production-quality software systems with minimal AI assistance.

The long-term target is not merely becoming a Python developer.

It is becoming a highly sought-after Software Engineer, Technical Consultant, and Software Architect capable of designing and reasoning about complex software systems with confidence, clarity, sound engineering judgment, and deep technical understanding.