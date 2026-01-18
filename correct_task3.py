# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math

import math

def average_valid_measurements(values):
    if not isinstance(values, list):
        return 0.0

    total = 0.0
    count = 0

    for v in values:
        if (
            v is not None
            and isinstance(v, (int, float))
            and not isinstance(v, bool)
            and math.isfinite(v)
        ):
            total += float(v)
            count += 1

    return total / count if count > 0 else 0.0



test_cases = [
    {
        "name": "Standard List",
        "data": [10, 20, 30],
        "expected": 20.0
    },
    {
        "name": "Mixed with None",
        "data": [10, None, 20],
        "expected": 15 
    },
    {
        "name": "Dirty Data (Strings/Booleans)",
        "data": [10, "20", True, 30], 
        "expected": 20 
    },
    {
        "name": "All None Values",
        "data": [None, None],
        "expected": 0.0
    },
    {
        "name": "Handling NaN/Inf",
        "data": [10, float('nan'), float('inf')],
        "expected": 10 
    }
]

print(f"{'Test Case':<30} | {'Status':<10}")
print("-" * 45)
for case in test_cases:
    res = average_valid_measurements(case["data"])
    status = "✅ PASS" if math.isclose(res, case["expected"]) else f"❌ FAIL (Got {res})"
    print(f"{case['name']:<30} | {status}")
