def format_vnd(x: int) -> str:
    """Format integer VND amount to string with thousand separators."""
    return f"{x:,} ₫".replace(",", ".")

def validate_income_input(value: str) -> int:
    """Validate and convert income input string to integer."""
    if not value.strip():
        return 0
    try:
        # Remove any non-digit characters except minus sign
        cleaned = ''.join(c for c in value if c.isdigit() or c == '-')
        return int(cleaned)
    except ValueError:
        return 0

def print_header(title: str):
    """Print a formatted header with underline."""
    print("\n" + title)
    print("-" * len(title))