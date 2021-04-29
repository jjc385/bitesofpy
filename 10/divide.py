def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError("Got a negative result")
        return result
    except ZeroDivisionError:
        return 0

