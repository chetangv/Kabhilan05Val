def parse_output(output):
    # Split the output into lines
    lines = output.splitlines()
    
    # Process each line (if there are multiple lines)
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            return value  # Return the value alone from the first valid line