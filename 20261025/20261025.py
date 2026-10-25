# REGRESSION CASES

import math
def classify_depth(raw_value):
    # Step 1: Handle missing values
    if raw_value is None:
        return "MISSING"
    if raw_value == "":
        return "MISSING"
    if isinstance(raw_value, bool):
        return "INVALID_TYPE"
    # Step 2: Attempt numeric conversion
    try:
        depth = float(raw_value)
    except (ValueError, TypeError):
        return "CONVERSION_FAILED"
    # Step 3: Your independent implementation
    # Check whether depth is finite.
    if not math.isfinite(depth):
      return "NON_FINITE"
    # Step 4: Reject negative depths.
    if depth < 0:
      return "INVALID_DEPTH"
    
    return "VALID_NUMERIC"


# TESTING
print("Running regression cases...")
test_cases = [
    (True, "INVALID_TYPE"),
    (False, "INVALID_TYPE"),
    (1, "VALID_NUMERIC"),
    (0, "VALID_NUMERIC"),
    (1.0, "VALID_NUMERIC"),
    (0.0, "VALID_NUMERIC"),
    ("1.0", "VALID_NUMERIC"),
    ("unknown", "CONVERSION_FAILED"),
]

for raw, expected in test_cases:
    actual = classify_depth(raw)
    assert actual == expected, (
        f"Input {raw!r}: expected {expected}, got {actual}"
    )

print("All regression cases passed")