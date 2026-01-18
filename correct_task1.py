# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    if not isinstance(orders, list) or not orders:
        return 0.0
    total = 0.0
    valid_count = 0  
    for order in orders:
        if not isinstance(order, dict):
            continue
        status = order.get("status")
        amount = order.get("amount")
        
        if status != "cancelled" and isinstance(amount, (int, float)):
            total += amount
            valid_count += 1 

    if valid_count == 0:
        return 0.0

    return total / valid_count

test_cases = [
   {
        "name": "Zero Amount Orders",
        "data": [{"amount": 0, "status": "completed"}, {"amount": 0, "status": "completed"}],
        "expected": 0.0 
    },
    {
        "name": "Extreme Values (Floats)",
        "data": [{"amount": 10.55, "status": "completed"}, {"amount": 20.45, "status": "completed"}],
        "expected": 15.5
    },
    {
        "name": "Invalid Amount Type (String)",
        "data": [
            {"amount": "100", "status": "completed"}, 
            {"amount": 50, "status": "completed"}
        ],
        "expected": 50.0
    },
    {
        "name": "Malformed Dictionary",
        "data": ["not a dict", {"amount": 100}], 
        "expected": 100.0 
    }
]

for case in test_cases:
    result = calculate_average_order_value(case["data"])
    status = "✅ PASS" if result == case["expected"] else f"❌ FAIL (Got {result})"
    print(f"{case['name']}: {status}")