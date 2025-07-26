#!/usr/bin/env python3.14
"""Run all t-string examples in sequence"""

import subprocess
import sys
from pathlib import Path

# List of example files in order
examples = [
    "01_basics.py",
    "02_template_type.py", 
    "03_interpolation.py",
    "04_evaluation.py",
    "05_api_overview.py",
    "06_sql_example.py",
    "07_html_example.py",
    "08_logging.py",
    "09_use_cases.py",
    "10_sublanguages.py",
]

def run_example(filename):
    """Run a single example file"""
    print("=" * 70)
    print(f"Running: {filename}")
    print("=" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, filename],
            cwd=Path(__file__).parent,
            capture_output=False,
            text=True
        )
        
        if result.returncode != 0:
            print(f"\n❌ Error running {filename}")
            return False
            
    except Exception as e:
        print(f"\n❌ Failed to run {filename}: {e}")
        return False
    
    print()  # Empty line between examples
    return True

def main():
    """Run all examples"""
    print("T-STRINGS EXAMPLES - PEP 750")
    print("Python 3.14 Template Strings Demonstration")
    print()
    
    success_count = 0
    
    for example in examples:
        if run_example(example):
            success_count += 1
    
    print("=" * 70)
    print(f"Completed: {success_count}/{len(examples)} examples ran successfully")
    
    if success_count < len(examples):
        print("\n⚠️  Some examples failed. Make sure you're using Python 3.14+")
        print("Install with: uv python install 3.14")

if __name__ == "__main__":
    main()