# scripts/validate_employee.py
import sys
import yaml
import re
from datetime import datetime

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_employee_file(filepath):
    errors = []
    
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"[ERROR] Failed to parse YAML file: {e}")
        sys.exit(1)
        
    # Check required fields
    required_fields = ['first_name', 'last_name', 'email', 'department', 'role']
    employee = data.get('employee', {})
    
    for field in required_fields:
        if field not in employee or not employee[field]:
            errors.append(f"Missing required field: {field}")
            
    # Validate email format
    if 'email' in employee:
        if not validate_email(employee['email']):
            errors.append(f"Invalid email format: {employee['email']}")
            
    # Validate start date if present
    if 'start_date' in employee:
        if not validate_date(str(employee['start_date'])):
            errors.append(f"Invalid date format: {employee['start_date']} (user YYYY-MM-DD)")
            
    # Check groups list
    if 'groups' in employee:
        if not isinstance(employee['groups'], list) or len(employee['groups']) == 0:
            errors.append("Groups must be a non-empty list")
            
    # Print results
    if errors:
        print("VALIDATION FAILED:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    else:
        print("VALIDATION PASSED!")
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate_employee.py <employee_file.yml>")
        sys.exit(1)
        
    validate_employee_file(sys.argv[1])