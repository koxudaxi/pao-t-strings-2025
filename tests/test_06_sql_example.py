#!/usr/bin/env python3.14
"""Unit tests for 06_sql_example.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestSQLExample(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "06_sql_example.py"
    
    def test_sql_example_output(self):
        """Test that 06_sql_example.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # SQL injection prevention section
        self.assertIn("=== SQL Injection Prevention ===", output)
        self.assertIn("Malicious input: '1; DROP TABLE users; --'", output)
        
        # Dangerous f-string
        self.assertIn("❌ DANGEROUS - Using f-string:", output)
        self.assertIn("Query: SELECT * FROM users WHERE id = 1; DROP TABLE users; --", output)
        self.assertIn("Result: SQL INJECTION - Table could be dropped!", output)
        
        # Safe t-string
        self.assertIn("✅ SAFE - Using t-string with sql():", output)
        self.assertIn("Query: SELECT * FROM users WHERE id = ?", output)
        self.assertIn("Params: ['1; DROP TABLE users; --']", output)
        self.assertIn("Result: Input safely parameterized, injection prevented!", output)
        
        # Complex query
        self.assertIn("=== Complex Query Example ===", output)
        self.assertIn("Complex query with multiple parameters:", output)
        self.assertIn("WHERE u.username = ?", output)
        self.assertIn("AND u.age BETWEEN ? AND ?", output)
        self.assertIn("Parameters: ['alice', 18, 65, 'active']", output)
        
        # Advanced injections
        self.assertIn("=== Preventing Advanced Injections ===", output)
        self.assertIn("Input: \"'; DELETE FROM users; --\"", output)
        self.assertIn("Safe query: SELECT * FROM users WHERE username = ?", output)
        self.assertIn("Input: '1 OR 1=1'", output)
        self.assertIn("Input: \"admin'--\"", output)
        self.assertIn("Input: \"1; UPDATE users SET role='admin' WHERE username='hacker'; --\"", output)

if __name__ == '__main__':
    unittest.main()