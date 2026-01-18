# AI Code Review Assignment (Python)

## Candidate

- Name: Eyerusalem Sahle
- Approximate time spent: 60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- Division by Zero: If the orders list is empty, the code crashes with a ZeroDivisionError because it attempts to divide by len(orders) (which is 0).
- Average Calculation Logic Error: The code divides the sum of non-cancelled orders by the total number of orders. This results in a wrong logic.
- KeyError Crash: If an order dictionary is missing the "status" or "amount" keys, the program crashes immediately.

### Edge cases & risks

-Input Validation: The code assumes the input is always a list of dictionaries. Passing None, a string, or a list containing non-dictionary items (like strings or integers) causes an AttributeError.
Data Type Sensitivity: If "amount" is passed as a string, the code crashes because it cannot add a string to an integer.

### Code quality / design issues

- Poor separation of concerns
  Validation, aggregation, and averaging are not clearly handled.

## 2) Proposed Fixes / Improvements

### Summary of changes

Added Input Guard: Checks if orders is actually a list and not empty before proceeding.
Corrected Denominator: Added valid_count variable to ensure we only divide by the number of orders actually added to the total.
Type Checking: Added isinstance(order, dict) and isinstance(amount, (int, float)) to prevent crashes from wrong data.
Safe Key Access: Used .get() instead of bracket notation to prevent KeyError.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

When testing the corrected calculate_average_order_value function, I would focus on "Empty or invalid inputs", "Orders with cancelled status",
"Orders with missing keys or invalid types", "Mixed valid and invalid orders", "All orders cancelled or invalid", "Normal valid input", to ensure robustness and correctness.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

1 The original explanation incorrectly implies that cancelled orders are fully excluded from the calculation. In reality, while their amounts are excluded from the total, they still count toward the divisor, which can lead to an inaccurate average.

2 It does not mention that the original code lacks safeguards against empty inputs, missing keys, or invalid data types, which could cause runtime errors.

3 The explanation assumes that all orders are valid dictionaries with numeric amount values, which is not enforced in the original code.

### Rewritten explanation

The original function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the total number of orders, including cancelled ones. While cancelled orders are excluded from the sum, they are still counted in the divisor, which can result in an inaccurate average. The function assumes that all orders are valid dictionaries containing "status" and "amount" keys and that the input list is non-empty, but it does not include safeguards for missing keys, invalid data types, or empty inputs, so it may raise runtime errors in such cases.

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject - Request Changes
- Justification: The implementation and its original explanation are inaccurate and unsafe. The function lacks proper input validation, produces incorrect averages in the presence of invalid values, and can crash on empty or mixed-type inputs.
- Confidence & unknowns: High confidence in the identified issues based on Python’s behavior.

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- Null Pointer Exception: If emails is None, the line for email in emails will cause a TypeError: 'NoneType' object is not iterable.
- Weak Validation: The check if "@" in email is extremely poor. It accepts strings that are clearly not emails, such as "@", "me@me", or "user@com".

### Edge cases & risks

- Non-String Items: If the list contains integers or other objects (e.g., [123, None]), the code will crash because you cannot check if "@" is "in" an integer.
- Empty/Whitespace Strings: A string containing just " @ " would be counted as valid despite being unusable.

### Code quality / design issues

- There is a design issue in the original code: it only checks if a character exists in the string rather than validating it as a proper email address.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added Type Guard: Included a check for isinstance(emails, list) to prevent crashes if the input is None or another data type.
- Implemented Regex Validation: Replaced the simple "@" check with a Regular Expression (r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
- Internal Item Validation: Added a check to ensure each element in the list is a string before processing to prevent errors.

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

When testing the Count Valid Emails function, I would focus on two main areas: crash prevention and pattern accuracy.

First, I’d test messy inputs by passing None, empty lists, or lists with numbers instead of strings. This confirms the "guards" work and the code won't crash on bad data. Second, I’d test the regex precision by using "fake" emails that a simple search would miss—like @@@ or name@com—to make sure only real, properly formatted addresses are counted. Finally, I’d include modern email styles, like those ending in .info or containing dots and underscores, to ensure the new rules aren't too strict.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- The original explanation is misleading because it claims the code is "safe" and "correct," when in reality, the function will crash if it receives a null input and will incorrectly count strings like "@@@" as valid emails. It fails to mention that the logic is too simple for real-world use and lacks the basic error handling needed to prevent the program from stopping when it hits bad data.

### Rewritten explanation

- The function counts the number of strings that contain "@" in the input list.

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject - Request Changes
- Justification: The original code was logically incorrect. It would crash on null data and provide highly inaccurate counts by accepting strings like "@@@" as valid emails.
- Confidence & unknowns: High confidence in the identified issues based on Python’s behavior.

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

ZeroDivisionError: If values is an empty list [], the code will crash on the final line because it tries to divide by 0.

NoneType Crash: If the function is called with None instead of a list (e.g., average_valid_measurements(None)), len(values) will throw a TypeError.

Type Casting ERROR: The line float(v) assumes every non-None value is convertible to a float.If v is: a dictionary, a list, a non-numeric string like "abc"
the function will crash with a ValueError or TypeError.

### Edge cases & risks

Booleans are treated as numbers
Since bool is a subclass of int, True and False are silently converted to 1.0 and 0.0, polluting the average.

Invalid values affect the divisor
count = len(values) counts all elements, including invalid ones, which results in an incorrect average when bad data is present.

NaN / Infinity values
Values like float("nan") or float("inf") are not filtered out and will corrupt the result.

### Code quality / design issues

- Poor separation of concerns
  Validation, aggregation, and averaging are not clearly handled.

## 2) Proposed Fixes / Improvements

### Summary of changes

Added Input Guard
Verifies that values is a list and not None before proceeding.

Added Zero Guard
Returns 0.0 when there are no valid values, preventing division by zero.

Added Numeric Type Check
Uses isinstance(v, (int, float)) to ensure only real numeric values are processed.

Excluded Boolean Values
Explicitly filters out bool to avoid silently counting True/False as numbers.

Counts Only Valid Values
The divisor reflects only the number of valid measurements, producing a correct average.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

When testing the Aggregate Valid Measurements function, I would focus on several key scenarios to ensure the corrected logic is robust. First, I’d check empty or null inputs to verify the "Input Guards" prevent a ZeroDivisionError or a NoneType crash. Next, I would test lists with missing values (None) to ensure the math is calculated only using valid numbers, meaning the divisor correctly ignores the empty slots.

I would also focus heavily on data type resilience, specifically testing how the function handles data like Booleans (True/False) and numeric strings (like "10.5"). Since Python treats Booleans as numbers, it's vital to confirm they are explicitly excluded so they don't skew the average. Finally, I’d test mixed valid and invalid entries—such as a list containing a float, a string, and a dictionary—to make sure the function skips the garbage data and returns an accurate average for the remaining numbers without crashing.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- The explanation overstates the function’s correctness. The code only skips None and does not validate input types, so non-numeric values will cause crashes. It divides by the full list length, producing incorrect averages when invalid values exist, fails on empty lists with a ZeroDivisionError, and unintentionally treats booleans as numbers.

### Rewritten explanation

- The function sums all non-None values in the input list and divides the result by the total number of elements. It assumes all non-None values are numeric and does not handle invalid types, empty lists, or boolean values safely, which can lead to incorrect results or runtime errors.

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject - Request Changes
- Justification: The implementation and its original explanation are inaccurate and unsafe. The function lacks proper input validation, produces incorrect averages in the presence of invalid values, and can crash on empty or mixed-type inputs.
- Confidence & unknowns: High confidence in the identified issues based on Python’s behavior.
