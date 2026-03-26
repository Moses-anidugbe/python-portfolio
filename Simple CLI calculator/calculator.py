def get_number(prompt, allow_back=False):
    """
    Prompts the user for a number.
    - If allow_back is True, user can enter 'back' to redo previous number.
    - User can always enter 'operation' to change the operation.
    Returns (value, command), where command can be 'operation' or 'back', or None.
    """
    while True:
        print("Note: You can enter 'operation' to select another operation.")
        if allow_back:
            print("Or enter 'back' to re-enter the first number.")
        entry = input(prompt).strip()
        if entry.lower() == 'operation':
            return None, 'operation'
        if allow_back and entry.lower() == 'back':
            return None, 'back'
        try:
            return float(entry), None
        except ValueError:
            print("Error: Please enter a valid number.")


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return None
        return num1 / num2


while True:
    # Get operation
    operation = input("Enter operation (+, -, *, /): ").strip()
    while operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Choose one of +, -, *, /.")
        operation = input("Enter operation (+, -, *, /): ").strip()

    # Get numbers
    while True:
        num1, cmd1 = get_number("Enter first number: ")
        if cmd1 == 'operation':
            break  # back to operation selection

        while True:
            num2, cmd2 = get_number("Enter second number: ", allow_back=True)
            if cmd2 == 'operation':
                break  # back to operation selection
            if cmd2 == 'back':
                break  # redo first number
            # Valid numbers collected
            result = calculate(num1, num2, operation)
            if result is not None:
                print(
                    f"The result of {num1} {operation} {num2} is: {result:.2f}")
            break  # exit second number loop

        if cmd2 == 'operation':
            break  # go back to outer operation input
        if cmd2 == 'back':
            continue  # redo first number
        break  # both numbers valid

    if cmd1 == 'operation':
        continue  # restart outer loop

    # Continue calculation?
    cont = input(
        "Do you want to perform another calculation? (yes/no): ").strip().lower()
    while cont not in ['yes', 'no']:
        cont = input("Invalid input. Enter 'yes' or 'no': ").strip().lower()
    if cont == 'no':
        print("Thank you for using the calculator. Goodbye!")
        break
