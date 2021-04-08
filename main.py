# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main
import os

os.system('cls')
print('\nStarting Time Calculator...\n')
print(add_time("11:06 PM", "2:02"))

print('\nExecuting Unit Tests...')
# Run unit tests automatically
main(module='test_module', exit=False)