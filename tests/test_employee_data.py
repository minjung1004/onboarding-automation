# tests/test_employee_data.py
import pytest 
import yaml
import os
from scripts.validate_employee import validate_email, validate_date

def test_validate_email():
    assert validate_email("jane.doe@company.com") == True
    assert validate_email("invalid-email") == False
    assert validate_email("@company.com") == False

def test_validate_date():
    assert validate_date("2025-10-22") == True
    assert validate_date("2024-13-01") == False
    assert validate_date("invalid-date") == False

def test_employee_yaml_structure():
    # Create a test employee file
    test_data = {
        'employee': {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test.user@company.com',
            'department': 'IT',
            'role': 'Developer',
            'groups': ['developers']
        }
    }
    
    with open('/tmp/test_employee.yml', 'w') as f:
        yaml.dump(test_data, f)
    
    # Validate structure
    with open('/tmp/test_employee.yml', 'r') as f:
        data = yaml.safe_load(f)
    
    assert 'employee' in data
    assert 'first_name' in data['employee']
    assert 'email' in data['employee']
    
    # Cleanup
    os.remove('/tmp/test_employee.yml')
