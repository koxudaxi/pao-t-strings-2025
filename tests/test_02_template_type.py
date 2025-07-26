#!/usr/bin/env python3.14
"""Unit tests for 02_template_type.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestTemplateType(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "02_template_type.py"
    
    def test_template_type_output(self):
        """Test that 02_template_type.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Check key sections
        self.assertIn("=== Template Type Structure ===", output)
        self.assertIn("Template: t\"User {user} {action} at {timestamp}\"", output)
        
        # Check static parts
        self.assertIn("Static parts (.strings):", output)
        self.assertIn("[0]: 'User '", output)
        self.assertIn("[1]: ' '", output)
        self.assertIn("[2]: ' at '", output)
        self.assertIn("[3]: ''", output)
        
        # Check interpolations
        self.assertIn("Dynamic parts (.interpolations):", output)
        self.assertIn("value='Alice'", output)
        self.assertIn("expression='user'", output)
        self.assertIn("value='logged in'", output)
        self.assertIn("expression='action'", output)
        self.assertIn("value='2025-01-15 10:30:00'", output)
        self.assertIn("expression='timestamp'", output)
        
        # Check structure explanation
        self.assertIn("=== How they combine ===", output)
        self.assertIn("Pattern: string[0] + interp[0] + string[1] + interp[1] + ... + string[n]", output)
        self.assertIn("Structure:", output)
        self.assertIn("'User ' + <user='Alice'> + ' ' + <action='logged in'> + ' at ' + <timestamp='2025-01-15 10:30:00'> + ''", output)

if __name__ == '__main__':
    unittest.main()