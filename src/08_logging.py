#!/usr/bin/env python3.14
"""Structured Logging Example - Using t-strings for better logging"""

from string import templatelib
import json
from datetime import datetime

class StructuredLogger:
    """Mock structured logger that uses templates for rich logging"""
    
    def __init__(self, name):
        self.name = name
    
    def _format_human(self, template):
        """Format template for human reading"""
        parts = []
        for item in template:
            if isinstance(item, str):
                parts.append(item)
            else:
                value = item.value
                if item.format_spec:
                    formatted = format(value, item.format_spec)
                else:
                    formatted = str(value)
                parts.append(formatted)
        return ''.join(parts)
    
    def _format_json(self, template, level, timestamp):
        """Format template as structured JSON"""
        # Extract all interpolated values with their expressions as keys
        data = {
            "timestamp": timestamp.isoformat(),
            "logger": self.name,
            "level": level,
            "message": self._format_human(template),
            "fields": {}
        }
        
        for interp in template.interpolations:
            # Use expression as field name (cleaned up)
            field_name = interp.expression.strip()
            if '.' in field_name:
                # Handle nested attributes like user.name
                field_name = field_name.replace('.', '_')
            data["fields"][field_name] = interp.value
        
        return json.dumps(data, default=str)
    
    def info(self, template):
        """Log at INFO level"""
        if not isinstance(template, templatelib.Template):
            raise TypeError("Logger requires template strings")
        
        timestamp = datetime.now()
        
        # Output both formats
        print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] INFO: {self._format_human(template)}")
        print(f"JSON: {self._format_json(template, 'INFO', timestamp)}")
        print()

# Create logger instance
logger = StructuredLogger("app.transactions")

# Basic logging example
print("=== Basic Structured Logging ===")
action = "purchase"
amount = 42.50
currency = "USD"

logger.info(t"User {action}: {amount:.2f} {currency}")

# More complex example with objects
print("=== Complex Structured Logging ===")
user = {
    "id": 12345,
    "name": "Alice Smith",
    "email": "alice@example.com"
}
order = {
    "id": "ORD-789",
    "items": 3,
    "total": 156.78
}
processing_time = 0.234

logger.info(t"Order {order['id']} processed for user {user['name']} in {processing_time:.3f}s")

# Error logging with context
print("=== Error Logging with Context ===")
error_code = "PAYMENT_FAILED"
error_message = "Card declined"
retry_count = 3

logger.info(t"Payment error: {error_code} - {error_message} (retry {retry_count}/3)")

# Performance metrics
print("=== Performance Metrics ===")
endpoint = "/api/v1/users"
method = "GET"
status_code = 200
response_time_ms = 45.7
request_id = "req-abc123"

logger.info(t"{method} {endpoint} returned {status_code} in {response_time_ms:.1f}ms [request_id={request_id}]")

# Demonstrate the benefit
print("=== Benefits of Template-based Logging ===")
print("1. Human-readable output for development")
print("2. Structured JSON for log aggregation systems")
print("3. Type preservation in JSON fields")
print("4. Automatic field extraction from expressions")
print("5. Format specifications still work")