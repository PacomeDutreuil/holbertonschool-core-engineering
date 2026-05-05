#!/usr/bin/env python3

language = "Python"
version = 3

pi_value = 3.1415926535
pi_formatted = f"{pi_value:.2f}"

computation_valid = (round(pi_value, 2) == 3.14)

print(f"Language: {language}")
print(f"Version: {version}")
print(f"Pi approx: {pi_formatted}")
print(f"Computation valid: {computation_valid}")
