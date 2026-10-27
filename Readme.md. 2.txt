# Python Fundamentals Assignment

## Project Description

This project contains a Simple Interest Calculator written in Python 3.
The program asks the user for a name, principal amount, annual interest
rate, and time in years. It validates the input, calculates simple
interest, and demonstrates basic string manipulation.

## Files

- `simple_interest.py`: Contains the calculator, input validation,
  error handling, and string manipulation.
- `README.md`: Explains the project, how to run it, and how to test it.

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   `python simple_interest.py`

   If your computer uses the `python3` command, run:

   `python3 simple_interest.py`

5. Follow the prompts and enter the requested information.

## Formula

Simple Interest = (Principal * Rate * Time) / 100

Example:

- Principal: $1,000
- Annual interest rate: 5%
- Time: 2 years

Calculation: (1000 * 5 * 2) / 100 = $100.00

## Input Validation and Error Handling

The program checks that the principal amount, interest rate, and time
are valid positive numbers. It handles non-numeric input using a
`try/except ValueError` block.

The program also rejects empty numeric input, zero, negative numbers,
and non-finite values. It continues prompting the user until a valid
number is entered.

The name cannot be empty. The program removes leading and trailing
spaces and converts the name to title case.

## String Manipulation

The program demonstrates several string operations:

- `strip()` removes leading and trailing whitespace.
- `title()` formats the user's name in title case.
- `lower()` converts text to lowercase for searching.
- `split()` separates a description into words.
- `len()` counts the words in the description.
- `count()` counts occurrences of the word "interest".

These operations demonstrate both text transformation and text analysis.

## Testing

Run the program and manually check the following cases. Record the
actual result after performing each test.

| Test | Input | Expected Result |
|---|---|---|
| Normal calculation | Principal 1000, rate 5, time 2 | Simple interest is $100.00 |
| Decimal values | Principal 500.50, rate 4, time 3 | Simple interest is $60.06 |
| Non-numeric input | Enter `abc` for the principal | An error message appears and the program asks again |
| Empty input | Press Enter without entering a principal | An error message appears and the program asks again |
| Negative number | Enter `-500` for the principal | An error message appears and the program asks again |
| Zero | Enter `0` for the time | An error message appears and the program asks again |
| Name formatting | Enter `  jANE DOE  ` | The name is displayed as `Jane Doe` |
| String analysis | Enter `Simple interest and interest` as the description | The word count is 4 and the occurrence count is 2 |

### Testing Evidence

After running the tests above, update this section with the tests
you completed and their actual results. Include any unexpected
results and explain how they were corrected.

## Assumptions

- The principal amount must be greater than zero.
- The annual interest rate must be greater than zero.
- The time period must be greater than zero.
- The interest rate is entered as a percentage, such as 5 for 5%.
- The calculation uses simple interest, so interest is not added back
  to the principal.
- The program uses Python 3 and the standard library only.