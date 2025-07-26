#!/usr/bin/env python3.14
"""Unit tests for 09_use_cases.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestUseCases(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "09_use_cases.py"
    
    def test_use_cases_output(self):
        """Test that 09_use_cases.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Email templates
        self.assertIn("=== Email Templates ===", output)
        self.assertIn("Email content:", output)
        self.assertIn("Dear Alice Johnson,", output)
        self.assertIn("Your order #ORD-2025-001 has been shipped!", output)
        self.assertIn("Items in your order:", output)
        self.assertIn("- Python Book", output)
        self.assertIn("- Coffee Mug", output)
        self.assertIn("- Stickers", output)
        self.assertIn("Total: $67.99", output)
        self.assertIn("Expected delivery: January 20, 2025", output)
        self.assertIn("The Python Store Team", output)
        
        # Configuration files
        self.assertIn("=== Configuration Files ===", output)
        self.assertIn("Generated config file:", output)
        self.assertIn("[database]", output)
        self.assertIn("host = localhost", output)
        self.assertIn("port = 5432", output)
        self.assertIn("name = myapp", output)
        self.assertIn("user = appuser", output)
        self.assertIn("[cache]", output)
        self.assertIn("enabled = true", output)
        self.assertIn("ttl = 3600", output)
        self.assertIn("[api]", output)
        self.assertIn("key = secret-key-12345", output)
        self.assertIn("debug = false", output)
        
        # Simple use cases
        self.assertIn("=== Simple Use Cases ===", output)
        self.assertIn("1. Simple greeting: Hello World!", output)
        self.assertIn("2. Number formatting: Pi is approximately 3.14", output)
        self.assertIn("3. Temperature: Today is 25°C (77.0°F)", output)
        
        # Dynamic content
        self.assertIn("=== Dynamic Content Generation ===", output)
        self.assertIn("# API Documentation", output)
        self.assertIn("Generated on:", output)
        self.assertIn("## Available Endpoints", output)
        self.assertIn("5 endpoints available:", output)
        self.assertIn("- **GET** `/users` - List all users", output)
        self.assertIn("- **POST** `/users` - Create a new user", output)
        self.assertIn("- **GET** `/users/:id` - Get user by ID", output)
        self.assertIn("- **PUT** `/users/:id` - Update user", output)
        self.assertIn("- **DELETE** `/users/:id` - Delete user", output)
        
        # Benefits
        self.assertIn("=== Benefits of Templates for These Use Cases ===", output)
        self.assertIn("1. Separation of structure from data", output)
        self.assertIn("2. Easy to validate template structure", output)
        self.assertIn("3. Can be processed by different formatters", output)

if __name__ == '__main__':
    unittest.main()