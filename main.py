logs = """
2025-01-15 18:22:10 INFO Server started
2025-01-15 18:25:40 ERROR Database connection failed
2025-01-15 18:30:15 WARNING High memory usage
2025-01-15 18:35:05 ERROR Timeout while reading request
"""
errors = []
for line in logs.strip().split('\n'):
    parts = line.split(' ', 3) 
    if len(parts) == 4 and parts[2] == 'ERROR':
        timestamp = f"{parts[0]} {parts[1]}"  
        message = parts[3]                    
        errors.append((timestamp, message))
print(errors)