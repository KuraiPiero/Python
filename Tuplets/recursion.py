def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    m = n + sum_positive_numbers(n - 1)
    return m


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


##def recursive_function(parameters):
# if base_case_condition(parameters):
#   return base_case_value
#    recursive_function(modified_parameters)


def is_power_of(number, base):
    if number < base:
        return number
    while number % base == 0:
        number = number / base
    if number == 1:
        return True
    return False
