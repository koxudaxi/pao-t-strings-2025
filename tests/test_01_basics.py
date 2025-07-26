#!/usr/bin/env python3.14
"""Unit tests for 01_basics.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestBasics(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "01_basics.py"
    
    def test_basics_output(self):
        """Test that 01_basics.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        # Check it ran successfully
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Check key output elements
        self.assertIn("=== Basic t-string ===", output)
        self.assertIn("Expression: t\"Hello {name}\"", output)
        self.assertIn("Result type:", output)
        self.assertIn("Template", output)  # Should show Template type
        
        self.assertIn("=== f-string comparison ===", output)
        self.assertIn("f-string: 'Hello world' (type: str)", output)
        self.assertIn("t-string:", output)
        self.assertIn("(type: Template)", output)
        
        self.assertIn("=== Template Structure ===", output)
        self.assertIn("template.strings = ('Hello ', '')", output)
        self.assertIn("template.interpolations =", output)
        
        self.assertIn("=== Greeting Example ===", output)
        self.assertIn("Template: t\"Hello, {name}!\"", output)
        self.assertIn("strings: ('Hello, ', '!')", output)
        self.assertIn("Number of static parts: 2", output)
        self.assertIn("Number of interpolations: 1", output)
        self.assertIn("Rule: len(strings) == len(interpolations) + 1", output)

if __name__ == '__main__':
    unittest.main()