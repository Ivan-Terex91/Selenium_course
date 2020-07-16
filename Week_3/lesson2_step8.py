from sys import stdin

expected_result, actual_result = stdin.readline().split()
assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
