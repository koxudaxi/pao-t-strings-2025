#!/usr/bin/env python3.14
"""SQL Safety Example - Preventing SQL injection with t-strings"""

from string import templatelib

# Mock implementation of sql-tstring library
class SQLQuery:
    def __init__(self, query: str, params: list):
        self.query = query
        self.params = params
    
    def __repr__(self):
        return f"SQLQuery(query={self.query!r}, params={self.params!r})"

def sql(template):
    """
    Mock sql() function that demonstrates SQL parameterization.
    In real sql-tstring, this would return a proper query object.
    """
    if not isinstance(template, templatelib.Template):
        raise TypeError("sql() requires a template string")
    
    query_parts = []
    params = []
    
    for i, static in enumerate(template.strings[:-1]):
        query_parts.append(static)
        query_parts.append("?")  # Parameter placeholder
        params.append(template.interpolations[i].value)
    
    query_parts.append(template.strings[-1])
    
    return SQLQuery(''.join(query_parts), params)

# Demonstrate SQL injection prevention
print("=== SQL Injection Prevention ===")
print()

# Dangerous user input
user_id = "1; DROP TABLE users; --"
print(f"Malicious input: {user_id!r}")
print()

# Using f-string (DANGEROUS!)
print("❌ DANGEROUS - Using f-string:")
dangerous_query = f"SELECT * FROM users WHERE id = {user_id}"
print(f"Query: {dangerous_query}")
print("Result: SQL INJECTION - Table could be dropped!")
print()

# Using t-string with sql() function (SAFE!)
print("✅ SAFE - Using t-string with sql():")
safe_query = sql(t"SELECT * FROM users WHERE id = {user_id}")
print(f"Query: {safe_query.query}")
print(f"Params: {safe_query.params}")
print("Result: Input safely parameterized, injection prevented!")
print()

# More complex example
print("=== Complex Query Example ===")
username = "alice"
min_age = 18
max_age = 65
status = "active"

# Build a complex query safely
complex_query = sql(t"""
    SELECT u.id, u.name, u.email, COUNT(o.id) as order_count
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.username = {username}
      AND u.age BETWEEN {min_age} AND {max_age}
      AND u.status = {status}
    GROUP BY u.id, u.name, u.email
    ORDER BY order_count DESC
""")

print("Complex query with multiple parameters:")
print(f"Query: {complex_query.query}")
print(f"Parameters: {complex_query.params}")
print()

# Show how even tricky injections are prevented
print("=== Preventing Advanced Injections ===")
tricky_inputs = [
    "'; DELETE FROM users; --",
    "1 OR 1=1",
    "admin'--",
    "1; UPDATE users SET role='admin' WHERE username='hacker'; --"
]

for malicious in tricky_inputs:
    query = sql(t"SELECT * FROM users WHERE username = {malicious}")
    print(f"Input: {malicious!r}")
    print(f"Safe query: {query.query}")
    print(f"Param: {query.params}")
    print()