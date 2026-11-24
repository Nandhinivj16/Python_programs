
import subprocess
from datetime import datetime


try:
    compile_result = subprocess.run(
        ["gcc", "stats.c", "-o", "stats.exe"],
        capture_output=True,
        text=True
    )
   

    if compile_result.returncode == 0:
        print("C Compilation: SUCCESS")
    else:
        print("C Compilation: FAILED")
        print(compile_result.stderr)

except FileNotFoundError:
    print("ERROR: GCC compiler not found!")

test_cases = [
    {
        "input": ["10", "20", "30"],
        "expected": {"Minimum": 10, "Maximum": 30, "Mean": 20, "Median": 20}
    },
    {
        "input": ["25"],
        "expected": {"Minimum": 25, "Maximum": 25, "Mean": 25, "Median": 25}
    },
    {
        "input": ["0", "255"],
        "expected": {"Minimum": 0, "Maximum": 255, "Mean": 127, "Median": 127}
    },
    {
        "input": ["-5", "10"],
        "expected": "Invalid input: -5"
    }
]

try:
    pass_count = 0
    fail_count = 0

    test_results = []
    for test in test_cases:
       result = subprocess.run(
        [".\\stats.exe"] + test["input"],
        capture_output=True,
        text=True
    )

       print("Input:", test["input"])
       print("C Output:")
       print(result.stdout)
       if isinstance(test["expected"], dict):
          for name, expected in test["expected"].items():
             if f"{name}: {expected}" in result.stdout:
                print(f"{name} Test: PASS")
                pass_count += 1
                test_results.append(f"{name}: PASS")
             else:
                print(f"{name} Test: FAIL")
                fail_count += 1
                test_results.append(f"{name}: FAIL")

       else:
           if test["expected"] in result.stdout:
             print("Negative Input Test: PASS")
             pass_count += 1
             test_results.append("Negative Input Test: PASS")
           else:
              print("Negative Input Test: FAIL")
              fail_count += 1
              test_results.append("Negative Input Test: FAIL")

    print("--------------------")
  
    
  

except FileNotFoundError:
    print("ERROR: stats.exe not found!")






print("\n----- TEST SUMMARY -----")
print(f"Total Tests: {pass_count + fail_count}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")

with open("test_report.txt", "w") as file:
    file.write("C APPLICATION TEST REPORT\n")
    file.write("-------------------------\n")
    file.write(f"Date and Time: {datetime.now()}\n\n")
    file.write("Individual Test Results:\n")

    for test in test_results:
        file.write(test + "\n")

    file.write("\nTEST SUMMARY\n")
    file.write(f"Total Tests: {pass_count + fail_count}\n")
    file.write(f"Passed: {pass_count}\n")
    file.write(f"Failed: {fail_count}\n")

print("Test report generated successfully!")




