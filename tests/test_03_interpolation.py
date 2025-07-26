#!/usr/bin/env python3.14
"""Unit tests for 03_interpolation.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestInterpolation(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "03_interpolation.py"
    
    def test_interpolation_output(self):
        """Test that 03_interpolation.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Check main sections
        self.assertIn("=== Interpolation Type Details ===", output)
        
        # Simple interpolation
        self.assertIn("Simple interpolation:", output)
        self.assertIn(".value = 'world'", output)
        self.assertIn(".expression = 'name'", output)
        self.assertIn(".conversion = None", output)
        self.assertIn(".format_spec = ''", output)  # Empty string, not None
        
        # With format specification
        self.assertIn("With format specification:", output)
        self.assertIn(".value = 3.14159", output)
        self.assertIn(".expression = 'pi'", output)
        self.assertIn(".format_spec = '.2f'", output)
        
        # With conversion
        self.assertIn("With conversion (!r):", output)
        self.assertIn(".expression = 'debug_obj'", output)
        self.assertIn(".conversion = 'r'", output)
        
        # With alignment
        self.assertIn("With alignment (>10s):", output)
        self.assertIn(".format_spec = '>10s'", output)
        
        # Complex format
        self.assertIn("Complex format spec:", output)
        self.assertIn(".format_spec = '+010.4f'", output)
        
        # Conversion types section
        self.assertIn("=== Conversion Types ===", output)
        self.assertIn("None: conversion=None", output)
        self.assertIn("!s: conversion='s'", output)
        self.assertIn("!r: conversion='r'", output)
        self.assertIn("!a: conversion='a'", output)

if __name__ == '__main__':
    unittest.main()