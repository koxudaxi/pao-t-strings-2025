#!/usr/bin/env python3.14
"""Run all unit tests for t-strings examples"""

import unittest
import sys
from pathlib import Path

# Import all test modules
from test_01_basics import TestBasics
from test_02_template_type import TestTemplateType
from test_03_interpolation import TestInterpolation
from test_04_evaluation import TestEvaluation
from test_05_api_overview import TestAPIOverview
from test_06_sql_example import TestSQLExample
from test_07_html_example import TestHTMLExample
from test_08_logging import TestLogging
from test_09_use_cases import TestUseCases
from test_10_sublanguages import TestSublanguages

def run_all_tests():
    """Create test suite and run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestBasics,
        TestTemplateType,
        TestInterpolation,
        TestEvaluation,
        TestAPIOverview,
        TestSQLExample,
        TestHTMLExample,
        TestLogging,
        TestUseCases,
        TestSublanguages
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests with verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on results
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_all_tests())