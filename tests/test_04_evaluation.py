#!/usr/bin/env python3.14
"""Unit tests for 04_evaluation.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestEvaluation(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "04_evaluation.py"
    
    def test_evaluation_output(self):
        """Test that 04_evaluation.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Eager evaluation section
        self.assertIn("=== Eager Evaluation ===", output)
        self.assertIn("x = 42", output)
        self.assertIn("Template: t\"Result: {x * 2 + 1}\"", output)
        self.assertIn("Interpolation value: 85", output)
        self.assertIn("Interpolation expression: 'x * 2 + 1'", output)
        self.assertIn("After changing x to 100:", output)
        self.assertIn("Interpolation value still: 85", output)
        self.assertIn("(Eager evaluation - value captured at creation time)", output)
        
        # Lexical scoping
        self.assertIn("=== Lexical Scoping ===", output)
        self.assertIn("Template created inside function:", output)
        self.assertIn('global_var = "I\'m global"', output)
        self.assertIn('local_var = "I\'m local"', output)
        
        # Full Python expressions
        self.assertIn("=== Full Python Expressions ===", output)
        self.assertIn("Complex expressions in templates:", output)
        self.assertIn("math.sqrt(16)", output)
        self.assertIn("=> 4.0", output)
        self.assertIn("[x**2 for x in numbers if x % 2 == 0]", output)
        self.assertIn("=> [4, 16]", output)
        self.assertIn("(lambda x: x.upper())(\"hello\")", output)
        self.assertIn("=> HELLO", output)
        
        # Proof of eager evaluation
        self.assertIn("=== Proof of Eager Evaluation ===", output)
        self.assertIn("Counter after creating 3 templates: 3", output)
        self.assertIn("t1 value: 1", output)
        self.assertIn("t2 value: 2", output)
        self.assertIn("t3 value: 3", output)

if __name__ == '__main__':
    unittest.main()