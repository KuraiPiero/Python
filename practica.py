def is_power_of(number, base):
    number = number / base
    # Base case: when number is smaller than base.
    if number % base == 1:
        return False
        # If number is equal to 1, it's a power (base**0).
    elif number % base == 0:
        return True
    else:
        return False

    # Recursive case: keep dividing number by base.


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

