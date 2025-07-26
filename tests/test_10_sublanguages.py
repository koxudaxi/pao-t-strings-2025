#!/usr/bin/env python3.14
"""Unit tests for 10_sublanguages.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestSublanguages(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "10_sublanguages.py"
    
    def test_sublanguages_output(self):
        """Test that 10_sublanguages.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Multi-line SQL
        self.assertIn("=== Multi-line SQL Sub-language ===", output)
        self.assertIn("Multi-line SQL template:", output)
        self.assertIn("Template literal:", output)
        self.assertIn("SELECT", output)
        self.assertIn("u.name,", output)
        self.assertIn("COUNT(o.id) as order_count,", output)
        self.assertIn("WHERE u.created_at > ?", output)
        self.assertIn("AND u.status = ?", output)
        self.assertIn("HAVING COUNT(o.id) >= ?", output)
        self.assertIn("Parameterized query:", output)
        self.assertIn("Parameters:", output)
        
        # Multi-line HTML
        self.assertIn("=== Multi-line HTML Templates ===", output)
        self.assertIn("HTML template structure:", output)
        self.assertIn("Number of interpolations:", output)
        self.assertIn("Interpolated expressions:", output)
        self.assertIn("products[0]['image'] = python-tee.jpg", output)
        self.assertIn("products[0]['name'] = Python T-Shirt", output)
        self.assertIn("products[0]['price'] = 25.99", output)
        
        # GraphQL
        self.assertIn("=== GraphQL Query Templates ===", output)
        self.assertIn("GraphQL query template:", output)
        self.assertIn("Shows how conditional logic can be embedded", output)
        self.assertIn("Include orders: True", output)
        self.assertIn("Result would include orders section: Yes", output)
        
        # Shell commands
        self.assertIn("=== Shell Command Templates ===", output)
        self.assertIn("Generated shell script:", output)
        self.assertIn("Key parameters:", output)
        self.assertIn("Database: production", output)
        self.assertIn("Backup location: /var/backups", output)
        self.assertIn("Retention: 7 days", output)
        
        # Why challenging
        self.assertIn("=== Why Sub-languages are Challenging ===", output)
        self.assertIn("1. Multiple syntaxes in one file", output)
        self.assertIn("2. Hard to validate visually", output)
        self.assertIn("3. Easy to make syntax errors", output)
        self.assertIn("4. Context switching between languages", output)
        self.assertIn("5. Different escaping rules", output)
        self.assertIn("This is why tools like t-linter are valuable!", output)
        self.assertIn("- Syntax highlighting for each sub-language", output)
        self.assertIn("- Validation of SQL, HTML, etc. within templates", output)

if __name__ == '__main__':
    unittest.main()