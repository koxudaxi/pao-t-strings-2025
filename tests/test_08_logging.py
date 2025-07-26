#!/usr/bin/env python3.14
"""Unit tests for 08_logging.py"""

import unittest
import subprocess
import sys
import json
from pathlib import Path

class TestLogging(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "08_logging.py"
    
    def test_logging_output(self):
        """Test that 08_logging.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # Basic logging
        self.assertIn("=== Basic Structured Logging ===", output)
        self.assertIn("INFO: User purchase: 42.50 USD", output)
        
        # Check JSON output contains expected fields
        self.assertIn('"logger": "app.transactions"', output)
        self.assertIn('"level": "INFO"', output)
        self.assertIn('"message": "User purchase: 42.50 USD"', output)
        self.assertIn('"fields": {', output)
        self.assertIn('"action": "purchase"', output)
        self.assertIn('"amount": 42.5', output)
        self.assertIn('"currency": "USD"', output)
        
        # Complex logging
        self.assertIn("=== Complex Structured Logging ===", output)
        self.assertIn("Order ORD-789 processed for user Alice Smith in 0.234s", output)
        self.assertIn('"order[\'id\']": "ORD-789"', output)
        self.assertIn('"user[\'name\']": "Alice Smith"', output)
        self.assertIn('"processing_time": 0.234', output)
        
        # Error logging
        self.assertIn("=== Error Logging with Context ===", output)
        self.assertIn("Payment error: PAYMENT_FAILED - Card declined (retry 3/3)", output)
        self.assertIn('"error_code": "PAYMENT_FAILED"', output)
        self.assertIn('"error_message": "Card declined"', output)
        self.assertIn('"retry_count": 3', output)
        
        # Performance metrics
        self.assertIn("=== Performance Metrics ===", output)
        self.assertIn("GET /api/v1/users returned 200 in 45.7ms [request_id=req-abc123]", output)
        self.assertIn('"endpoint": "/api/v1/users"', output)
        self.assertIn('"method": "GET"', output)
        self.assertIn('"status_code": 200', output)
        self.assertIn('"response_time_ms": 45.7', output)
        
        # Benefits section
        self.assertIn("=== Benefits of Template-based Logging ===", output)
        self.assertIn("1. Human-readable output for development", output)
        self.assertIn("2. Structured JSON for log aggregation systems", output)
        self.assertIn("3. Type preservation in JSON fields", output)

if __name__ == '__main__':
    unittest.main()