# Project 1 — Decision Policy Classifier

## Background

Business workflows frequently use policies to decide how a case should be handled.

Examples include:

- whether an invoice requires approval,
- whether a risk requires escalation,
- whether an incident is critical,
- whether a transaction requires review,
- and whether a request may be processed automatically.

These decisions can be represented through explicit conditional rules.

## Assignment

In a file called `policy_classifier.py`, implement a Python program that classifies an operational case according to its risk score and estimated financial impact.

The program must ask the user for:

1. Case name
2. Risk score from 0 to 100
3. Estimated financial impact in dollars
4. Whether sensitive data is involved

For the sensitive-data question, assume the user enters either:

```text
yes