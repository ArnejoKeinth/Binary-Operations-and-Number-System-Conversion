def twos_complement(binary):
    complement = ''.join('1' if bit == '0' else '0' if bit == '1' else bit for bit in binary)
    carry = 1
    result = ''
    for bit in complement[::-1]:      
        if bit == '1' and carry == 1:
            result += '0'
        elif bit == '0' and carry == 1:
            result += '1'
            carry = 0
        else:
            result += bit
    return result[::-1]


# Binary WITHOUT decimal to Integers
def binary_to_integer(binary):
    if binary[0] == '1':
        integer_value = int(binary, 2) - 2 ** len(binary)
    else:
        integer_value = int(binary, 2)
    return integer_value


# Integers to Binary WITHOUT decimal
def integer_to_binary(integer):
    num_bits = integer.bit_length()
    num_bits = max(num_bits, 8)

    if integer >= 0:
        binary_value = bin(integer)[2:].zfill(num_bits)
        binary_value = ('0' * 4) + binary_value
        binary_value = ' '.join(binary_value[max(0, i - 4):i][::-1] for i in range(len(binary_value), 0, -4))
        return binary_value[::-1]
    elif 0 > integer >= -128:
        binary_value = bin((1 << num_bits) + integer & ((1 << num_bits) - 1))[2:].zfill(num_bits)
        binary_value = ('1' * 4) + binary_value
        binary_value = ' '.join(binary_value[max(0, i - 4):i][::-1] for i in range(len(binary_value), 0, -4))
        return binary_value[::-1]
    elif integer <= -129:
        binary_value = bin(integer)[3:].zfill(num_bits)
        binary_value = ('1' * 4) + twos_complement(binary_value)
        binary_value = ' '.join(binary_value[max(0, i - 4):i][::-1] for i in range(len(binary_value), 0, -4))
        return binary_value[::-1]


# Integers WITH decimal to Binary
def mixed_to_binary(mixed):
    integer_part, fraction_part = str(mixed).split('.')
    binary_integer_part = integer_to_binary(int(integer_part))

    binary_fraction_part = ''
    if fraction_part != '0':
        fraction_part = '0.' + fraction_part
        fraction = float(fraction_part)
        while fraction != 0:
            fraction *= 2
            binary_fraction_part += str(int(fraction))
            fraction -= int(fraction)

    result = binary_integer_part + '.' + binary_fraction_part
    return result


# Binary WITH decimal to Integer
def binary_fraction_to_integer(binary):
    integer_part, fraction_part = binary.split('.')
    integer_value = binary_to_integer(integer_part)

    fraction_value = 0
    for i in range(len(fraction_part)):
        fraction_value += int(fraction_part[i]) * (1 / (2 ** (i + 1)))
    result = integer_value + fraction_value

    return result


def add_binary(binary1, binary2):
    if '.' in binary1 or '.' in binary2:
        if '.' in binary1:
            int1 = binary_fraction_to_integer(binary1)
        else:
            int1 = binary_to_integer(binary1)

        if '.' in binary2:
            int2 = binary_fraction_to_integer(binary2)
        else:
            int2 = binary_to_integer(binary2)
        result = int1 + int2
        result = mixed_to_binary(result)

    else:
        int1 = binary_to_integer(binary1)
        int2 = binary_to_integer(binary2)
        result = int1 + int2
        result = integer_to_binary(result)

    return result


def subtract_binary(minuend, subtrahend):
    if '.' in minuend or '.' in subtrahend:
        if '.' in minuend:
            int1 = binary_fraction_to_integer(minuend)
        else:
            int1 = binary_to_integer(minuend)

        if '.' in subtrahend:
            int2 = binary_fraction_to_integer(subtrahend)
        else:
            int2 = binary_to_integer(subtrahend)
        result = int1 - int2
        result = mixed_to_binary(result)

    else:
        int1 = binary_to_integer(minuend)
        int2 = binary_to_integer(subtrahend)
        result = int1 - int2
        result = integer_to_binary(result)

    return result


def multiply_binary(multiplicand, multiplier):
    if '.' in multiplicand or '.' in multiplier:
        if '.' in multiplicand:
            int1 = binary_fraction_to_integer(multiplicand)
        else:
            int1 = binary_to_integer(multiplicand)

        if '.' in multiplier:
            int2 = binary_fraction_to_integer(multiplier)
        else:
            int2 = binary_to_integer(multiplier)
        result = int1 * int2
        result = mixed_to_binary(result)

    else:
        int1 = binary_to_integer(multiplicand)
        int2 = binary_to_integer(multiplier)
        result = int1 * int2
        result = integer_to_binary(result)

    return result


def divide_binary(dividend, divisor):
    if '.' in dividend or '.' in divisor:
        if '.' in dividend:
            int1 = binary_fraction_to_integer(dividend)
        else:
            int1 = binary_to_integer(dividend)

        if '.' in divisor:
            int2 = binary_fraction_to_integer(divisor)
        else:
            int2 = binary_to_integer(divisor)
        result = int1 / int2
        result = mixed_to_binary(result)

    else:
        int1 = binary_to_integer(dividend)
        int2 = binary_to_integer(divisor)
        result = int1 // int2
        result = integer_to_binary(result)

    return result


def binary_operations():
    print("Binary Operations Menu:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] 2's Complement")
    choice = int(input("Enter the operators: "))

    if choice == 1:
        addend1 = input("Enter the first addends in binary number: ").replace(" ", "")
        addend2 = input("Enter the second addends in binary number: ").replace(" ", "")

        result = add_binary(addend1, addend2)
        print("Sum:", result)

    elif choice == 2:
        minuend = input("Enter the minuend in binary: ").replace(" ", "")
        subtrahend = input("Enter the subtrahend in binary: ").replace(" ", "")

        result = subtract_binary(minuend, subtrahend)
        print("Result:", result)

    elif choice == 3:
        multiplicand = input("Enter the multiplicand in binary: ").replace(" ", "")
        multiplier = input("Enter the multiplier in binary: ").replace(" ", "")

        product = multiply_binary(multiplicand, multiplier)
        print("Product:", product)

    elif choice == 4:
        dividend = input("Enter the dividend in binary: ").replace(" ", "")
        divisor = input("Enter the divisor in binary: ").replace(" ", "")

        quotient = divide_binary(dividend, divisor)
        print("Quotient:", quotient)

    elif choice == 5:
        binary = input("Enter a binary number: ").replace(" ", "")
        complement = twos_complement(binary)
        complement = ' '.join(complement[::-1][i:i + 4] for i in range(0, len(complement), 4))[::-1]
        print("2's complement:", complement)


def number_conversion():
    pass


def main():
    while True:
        try:
            print("\nMain Menu:")
            print("[1] Binary Operations")
            print("[2] Number System Conversion")
            print("[3] Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                binary_operations()
            elif choice == 2:
                number_conversion()
            elif choice == 3:
                break

        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main()
