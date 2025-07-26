#!/usr/bin/env python3.14
"""Unit tests for 07_html_example.py"""

import unittest
import subprocess
import sys
from pathlib import Path

class TestHTMLExample(unittest.TestCase):
    
    def setUp(self):
        self.example_path = Path(__file__).parent.parent / "src" / "07_html_example.py"
    
    def test_html_example_output(self):
        """Test that 07_html_example.py produces expected output"""
        result = subprocess.run(
            [sys.executable, str(self.example_path)],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0, f"Script failed with stderr: {result.stderr}")
        
        output = result.stdout
        
        # XSS prevention section
        self.assertIn("=== XSS Prevention with HTML Templates ===", output)
        self.assertIn("Malicious input: \"<script>alert('xss')</script>\"", output)
        
        # Dangerous f-string
        self.assertIn("❌ DANGEROUS - Using f-string:", output)
        self.assertIn("HTML: <h1><script>alert('xss')</script></h1>", output)
        self.assertIn("Result: XSS VULNERABILITY - Script would execute!", output)
        
        # Safe t-string
        self.assertIn("✅ SAFE - Using t-string with html():", output)
        # HTML escaping uses &#x27; for single quotes
        self.assertIn("HTML: <h1>&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;</h1>", output)
        self.assertIn("Result: Input safely escaped, XSS prevented!", output)
        
        # Various attack vectors
        self.assertIn("=== Various XSS Attack Vectors ===", output)
        self.assertIn("Image XSS:", output)
        self.assertIn("Input: \"<img src=x onerror='alert(1)'>\"", output)
        self.assertIn("Safe output:", output)
        self.assertIn("&lt;img src=x onerror=&#x27;alert(1)&#x27;&gt;", output)
        
        self.assertIn("JavaScript protocol:", output)
        self.assertIn("IFrame injection:", output)
        self.assertIn("Attribute breaking:", output)
        
        # Attribute handling
        self.assertIn("=== Attribute Handling ===", output)
        self.assertIn("Attributes dict:", output)
        self.assertIn("'alt': 'A \"nice\" image'", output)
        self.assertIn("Safe HTML: <img src=\"image.jpg\" alt=\"A &quot;nice&quot; image\" onclick=\"alert(&#x27;should be escaped&#x27;)\" />", output)
        
        # Complex HTML
        self.assertIn("=== Complex HTML Example ===", output)
        self.assertIn("Username: 'Alice <admin>'", output)
        self.assertIn("Bio: 'I like to use <strong>HTML</strong> & \"quotes\"'", output)
        self.assertIn("<h2>Alice &lt;admin&gt;</h2>", output)
        self.assertIn("<p class=\"bio\">I like to use &lt;strong&gt;HTML&lt;/strong&gt; &amp; &quot;quotes&quot;</p>", output)

if __name__ == '__main__':
    unittest.main()