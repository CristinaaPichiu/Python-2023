from Math_Ops.operations import add, subtract, multiply, divide

if __name__ == '__main__':
    int_result_add = add(5, 3)
    int_result_subtract = subtract(8, 2)
    int_result_multiply = multiply(4, 6)
    int_result_divide = divide(10, 2)

    # Floating-point operations
    float_result_add = add(3.5, 2.5)
    float_result_subtract = subtract(7.8, 2.2)
    float_result_multiply = multiply(2.5, 4.5)
    float_result_divide = divide(9.0, 3.0)

    # Display results
    print(f"Integer Addition: {int_result_add}")
    print(f"Integer Subtraction: {int_result_subtract}")
    print(f"Integer Multiplication: {int_result_multiply}")
    print(f"Integer Division: {int_result_divide}")

    print(f"Floating-point Addition: {float_result_add}")
    print(f"Floating-point Subtraction: {float_result_subtract}")
    print(f"Floating-point Multiplication: {float_result_multiply}")
    print(f"Floating-point Division: {float_result_divide}")

