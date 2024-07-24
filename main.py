# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main


try:
    print(mean_var_std.calculate([0,1,2,3,4,5,6,7]))
    print("All elements in the 9 elements of the array are numbers.")
except ValueError as e:
    print(f"Array check failed: {e}")

# Run unit tests automatically
main(module='test_module', exit=False)