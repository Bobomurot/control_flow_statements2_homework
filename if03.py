def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > a and b < c) or (b > c and b < a):
        return b
    else:
        return c
