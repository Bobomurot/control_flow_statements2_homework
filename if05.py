def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n = abs(n)
    d1 = n // 10000
    d2 = (n // 1000) % 10
    d3 = (n // 100) % 10
    d4 = (n // 10) % 10
    d5 = n % 10
    
    maxdigit = d1
    if d2 > maxdigit:
        max_digit = d2
    if d3 > maxdigit:
        maxdigit = d3
    if d4 > maxdigit:
        maxdigit = d4
    if d5 > maxdigit:
        maxdigit = d5

    return maxdigit