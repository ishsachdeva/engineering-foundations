# Project 0 — Operational Impact Calculator

## Background

Operational teams often perform repetitive activities manually.

Examples include:

- reviewing invoices,
- validating requests,
- preparing reports,
- updating records,
- checking documents,
- and following up on incomplete cases.

Before improving or automating a workflow, a consultant must estimate how much effort and money the current process consumes.

## Assignment

In a file called `impact_calculator.py`, implement a Python program that calculates the annual operational impact of a repetitive business activity.

The program must ask the user for:

1. Number of cases processed each week
2. Average minutes required to process one case
3. Hourly labour cost
4. Expected percentage reduction in manual effort

Assume that:

- the organisation operates for 52 weeks each year;
- the user enters valid numeric values;
- the reduction percentage is between 0 and 100.

## Required calculations

The program must calculate:

1. Total cases processed annually
2. Current annual labour hours
3. Current annual labour cost
4. Estimated annual hours saved
5. Estimated annual financial savings
6. Remaining annual labour hours
7. Remaining annual labour cost

## Required functions

Implement at least these functions:

```text
calculate_annual_cases
calculate_annual_hours
calculate_annual_cost
calculate_reduction
main