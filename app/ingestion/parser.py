import re

LOG_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR|WARN)\s+(.*)')

def parse_log(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    return {
        "timestamp": match.group(1),
        "level": match.group(2),
        "message": match.group(3)
    }