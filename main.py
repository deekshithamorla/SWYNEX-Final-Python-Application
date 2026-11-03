def calculate_total(numbers):
    try:
        if not numbers:
            raise ValueError("Input list cannot be empty")

        return sum(numbers)

    except TypeError:
        print("Invalid input! Please enter numbers.")
        return None


def main():
    print("SWYNEX Python Application")

    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(x) for x in user_input.split()]

        result = calculate_total(numbers)

        if result is not None:
            print("Total:", result)

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()