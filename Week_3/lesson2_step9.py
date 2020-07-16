from sys import stdin

full_string, substring = stdin.readline().split()
assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
