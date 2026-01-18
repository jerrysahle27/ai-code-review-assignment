import re

def count_valid_emails(emails):
    if not isinstance(emails, list):
        print("Warning: Input was not a list!")
        return 0
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    count = 0

    for email in emails:
        if isinstance(email, str):
            if re.match(email_pattern, email.strip()):
                count += 1
                
    return count

test_cases = [
    {
        "name": "Standard Valid Emails",
        "data": ["test@example.com", "user.name@domain.org",22],
        "expected": 2
    },
    {
        "name": "Invalid Formats (Original Code would fail these)",
        "data": ["@", "admin@", "me@localhost", "@@@@", "test.com"],
        "expected": 0
    },
    {
        "name": "Null / Undefined Input",
        "data": None,
        "expected": 0
    },
    {
        "name": "Mixed Garbage Data",
        "data": ["valid@mail.com", 123, None, {"email": "test@test.com"}],
        "expected": 1
    },
    {
        "name": "Missing TLD (Top Level Domain)",
        "data": ["user@domain"], # Missing .com, .net, etc.
        "expected": 0
    }
]

print(f"{'Test Case':<35} | {'Result':<10}")
print("-" * 50)

for case in test_cases:
    result = count_valid_emails(case["data"])
    status = "✅ PASS" if result == case["expected"] else f"❌ FAIL (Got {result})"
    print(f"{case['name']:<35} | {status}")