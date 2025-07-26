#!/usr/bin/env python3
"""
Test all code examples from the slides to ensure they work as shown.
Requires Python 3.14+ with t-string support.
"""

import sys
from string.templatelib import Template, Interpolation


def test_basic_syntax():
    """Test the basic syntax examples from slides."""
    print("\n=== Testing Basic Syntax ===")
    
    # f-string vs t-string comparison (slide: Basic Syntax)
    name = "world"
    
    # f-string returns a string
    text = f"Hello {name}"
    assert text == "Hello world"
    assert isinstance(text, str)
    print("✓ f-string returns string")
    
    # t-string returns a Template
    template = t"Hello {name}"
    assert isinstance(template, Template)
    print("✓ t-string returns Template object")


def test_dissecting_tstrings():
    """Test the template structure from 'Dissecting t-strings' slide."""
    print("\n=== Testing Dissecting t-strings ===")
    
    name = "world"
    template = t"Hello, {name}!"
    
    # Check the structure matches the slide
    assert template.strings == ('Hello, ', '!')
    assert len(template.interpolations) == 1
    assert template.interpolations[0].value == 'world'
    print("✓ Template structure matches slide example")


def test_template_type():
    """Test the Template type examples from slides."""
    print("\n=== Testing Template Type ===")
    
    name = "Alice"
    age = 30
    template = t"Name: {name}, Age: {age}"
    
    # Test the len(strings) = len(interpolations) + 1 rule
    assert len(template.strings) == len(template.interpolations) + 1
    print(f"✓ Rule verified: len(strings)={len(template.strings)}, len(interpolations)={len(template.interpolations)}")
    
    # Test pattern: str → interp → str → interp → ... → str
    assert template.strings == ('Name: ', ', Age: ', '')
    assert len(template.interpolations) == 2
    print("✓ Pattern confirmed: strings and interpolations alternate")


def test_interpolation_type():
    """Test the Interpolation type from slides."""
    print("\n=== Testing Interpolation Type ===")
    
    name = "world"
    template = t"Hello {name:>10s}!"
    
    interp = template.interpolations[0]
    assert interp.value == "world"
    assert interp.expression == "name"
    assert interp.conversion is None
    assert interp.format_spec == ">10s"
    print("✓ Interpolation attributes match slide example")
    
    # Important: format spec is NOT applied yet
    assert interp.value == "world"  # Not "     world"
    print("✓ Format spec stored but not applied")


def test_evaluation_model():
    """Test eager evaluation from slides."""
    print("\n=== Testing Evaluation Model ===")
    
    x = 42
    template = t"Result: {x * 2 + 1}"
    
    # Test immediate evaluation
    assert template.interpolations[0].value == 85
    print("✓ Expression evaluated immediately: 42 * 2 + 1 = 85")
    
    # Change x after template creation
    x = 100
    assert template.interpolations[0].value == 85  # Still 85!
    print("✓ Confirmed: NOT lazy evaluation")


def test_api_iteration():
    """Test the iteration API from slides."""
    print("\n=== Testing API: Iteration ===")
    
    name = "World"
    template = t"Hello {name}!"
    
    contents = list(template)
    assert len(contents) == 3
    assert contents[0] == "Hello "
    assert isinstance(contents[1], Interpolation)
    assert contents[1].value == "World"
    assert contents[2] == "!"
    print("✓ Iteration works as shown in slides")
    
    # Empty strings are omitted
    first = "Eat"
    second = "Red Leicester"
    template2 = t"{first}{second}"
    contents2 = list(template2)
    assert len(contents2) == 2  # Not 3, because empty string is omitted
    print("✓ Empty strings omitted in iteration")


def test_api_values():
    """Test the values property from slides."""
    print("\n=== Testing API: Values Property ===")
    
    name = "Alice"
    age = 30
    template = t"Name: {name}, Age: {age}"
    
    assert template.values == ("Alice", 30)
    print("✓ template.values returns tuple of interpolation values")


def test_concatenation():
    """Test concatenation examples from slides."""
    print("\n=== Testing Concatenation ===")
    
    name = "World"
    
    # Explicit concatenation
    result1 = t"Hello " + t"{name}"
    assert isinstance(result1, Template)
    assert result1.strings == ("Hello ", "")
    assert result1.values == ("World",)
    print("✓ Explicit concatenation works")
    
    # Implicit concatenation
    result2 = t"Hello " t"{name}"
    assert isinstance(result2, Template)
    assert result2.strings == ("Hello ", "")
    assert result2.values == ("World",)
    print("✓ Implicit concatenation works")
    
    # Template + str is prohibited
    try:
        invalid = t"Hello " + "world"
        assert False, "Should have raised TypeError"
    except TypeError:
        print("✓ Template + str raises TypeError as expected")


def test_debug_specifier():
    """Test debug specifier from slides."""
    print("\n=== Testing Debug Specifier ===")
    
    value = 42
    template1 = t"Result: {value=}"
    
    # Check it's treated as 'value={value!r}'
    assert template1.strings[0] == "Result: value="
    assert template1.interpolations[0].conversion == "r"
    print("✓ {value=} adds 'value=' and uses repr")
    
    # With format spec
    template2 = t"Result: {value=:.2f}"
    assert template2.strings[0] == "Result: value="
    # When using format spec with =, conversion is None
    assert template2.interpolations[0].conversion is None
    assert template2.interpolations[0].format_spec == ".2f"
    print("✓ {value=:.2f} works with format spec")


def test_pattern_matching_example():
    """Test the pattern matching example from slides."""
    print("\n=== Testing Pattern Matching Example ===")
    
    def process_template(template: Template) -> str:
        """Process a template using pattern matching - reimplementing f-string behavior."""
        result = []
        for part in template:
            match part:
                case str():
                    result.append(part)  # Static string part
                case Interpolation(value=val, conversion=conv, format_spec=spec):
                    # Apply conversion
                    if conv == "r": val = repr(val)
                    elif conv == "s": val = str(val)
                    elif conv == "a": val = ascii(val)
                    # Apply format spec
                    if spec: val = format(val, spec)
                    else: val = str(val)
                    result.append(val)
        return ''.join(result)
    
    # Test the example from slides
    name = "Alice"
    pi = 3.14159
    
    template1 = t"Hello, {name}!"
    assert process_template(template1) == "Hello, Alice!"
    print("✓ Basic template processing works")
    
    template2 = t"Pi is approximately {pi:.2f}"
    assert process_template(template2) == "Pi is approximately 3.14"
    print("✓ Format spec processing works")
    
    template3 = t"Debug: name={name!r}, age={30:>5d}"
    assert process_template(template3) == "Debug: name='Alice', age=   30"
    print("✓ Conversion and format spec work together")


def test_flexible_use_cases():
    """Test the flexible use cases from slides."""
    print("\n=== Testing Flexible Use Cases ===")
    
    # Email template example (matching slide exactly)
    user = type('User', (), {'name': 'Alice'})()
    order = type('Order', (), {'id': '12345'})()
    template = t"""Dear {user.name},
Your order #{order.id}
has been shipped!"""
    
    assert template.values == ('Alice', '12345')
    print("✓ Email template extracts values correctly")
    
    # Config file example
    db_host = "localhost"
    db_port = 5432
    config = t"""[database]
host = {db_host}
port = {db_port}"""
    
    assert config.values == ('localhost', 5432)
    print("✓ Config template extracts values correctly")


def test_sql_example():
    """Test the SQL example from slides (mocked)."""
    print("\n=== Testing SQL Example (Mocked) ===")
    
    # Mock sql function similar to slide
    def mock_sql(template):
        """Simplified sql function for testing."""
        query_parts = []
        params = []
        
        for i, static in enumerate(template.strings[:-1]):
            query_parts.append(static)
            query_parts.append("?")
            params.append(template.interpolations[i].value)
        
        query_parts.append(template.strings[-1])
        
        return {
            'query': ''.join(query_parts),
            'params': params
        }
    
    # Test the exact example from slides
    user_id = "1; DROP TABLE users;"
    query = mock_sql(t"SELECT * FROM users WHERE id = {user_id}")
    
    assert query['query'] == "SELECT * FROM users WHERE id = ?"
    assert query['params'] == ['1; DROP TABLE users;']
    print("✓ SQL injection prevented - matches slide example")


def test_html_example():
    """Test the HTML example from slides (mocked)."""
    print("\n=== Testing HTML Example (Mocked) ===")
    
    # Mock html function
    def mock_html(template):
        """Simplified html function for testing."""
        result = []
        for part in template:
            if isinstance(part, str):
                result.append(part)
            else:
                # HTML escape the value
                escaped = str(part.value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                result.append(escaped)
        return ''.join(result)
    
    # Test the exact example from slides
    user_input = "<script>alert('xss')</script>"
    safe_html = mock_html(t"<h1>{user_input}</h1>")
    
    assert safe_html == "<h1>&lt;script&gt;alert('xss')&lt;/script&gt;</h1>"
    print("✓ HTML auto-escaped - matches slide example")


def test_structured_logging():
    """Test structured logging example from slides."""
    print("\n=== Testing Structured Logging ===")
    
    # Mock structured logger
    class MockLogger:
        def __init__(self):
            self.last_log = None
            
        def info(self, template):
            # Extract message and context
            msg_parts = []
            context = {}
            
            for i, (static, interp) in enumerate(zip(template.strings, list(template.interpolations) + [None])):
                msg_parts.append(static)
                if interp:
                    msg_parts.append(str(interp.value))
                    # Use expression as key for context
                    context[interp.expression] = interp.value
            
            self.last_log = {
                'message': ''.join(msg_parts),
                'context': context
            }
    
    # Test example from slides
    logger = MockLogger()
    user_id = 42
    action = "login"
    logger.info(t"User {user_id} performed {action}")
    
    assert logger.last_log['message'] == "User 42 performed login"
    assert logger.last_log['context'] == {'user_id': 42, 'action': 'login'}
    print("✓ Structured logging captures context - matches slide concept")


def run_all_tests():
    """Run all test functions."""
    print("Testing all code examples from slides...")
    print("=" * 50)
    
    test_functions = [
        test_basic_syntax,
        test_dissecting_tstrings,
        test_template_type,
        test_interpolation_type,
        test_evaluation_model,
        test_api_iteration,
        test_api_values,
        test_concatenation,
        test_debug_specifier,
        test_pattern_matching_example,
        test_flexible_use_cases,
        test_sql_example,
        test_html_example,
        test_structured_logging,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"\n❌ {test_func.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"\nTest Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("\n✅ All slide examples work correctly!")
    else:
        print(f"\n⚠️  {failed} tests failed. Please check the examples.")
        sys.exit(1)


if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 14):
        print("Error: This script requires Python 3.14 or later for t-string support.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    run_all_tests()