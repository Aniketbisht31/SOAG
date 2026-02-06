import math

def solve_master(a, b, k):
    """
    Solves recurrence of form:
    T(n) = aT(n/b) + O(n^k)
    """

    log_val = math.log(a, b)

    if log_val > k:
        return f"Theta(n^{log_val:.2f})"
    elif log_val == k:
        return f"Theta(n^{k} log n)"
    else:
        return f"Theta(n^{k})"
