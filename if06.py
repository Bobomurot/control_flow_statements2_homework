def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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

    max_digit = d1
    max_index = 1

    if d2 > max_digit:
        max_digit = d2
        max_index = 2
    if d3 > max_digit:
        max_digit = d3
        max_index = 3
    if d4 > max_digit:
        max_digit = d4
        max_index = 4
    if d5 > max_digit:
        max_digit = d5
        max_index = 5

    return max_index