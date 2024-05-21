
from swap import swap_numbers
from extras.desc import print_descending

if __name__ == "__main__":
    a = int(input("Please enter the first number to swap (0-3): "))
    b = int(input("Please enter the second number to swap (0-3): "))
    swapped_a, swapped_b = swap_numbers(a, b)
    print(f"The swapped numbers are: {swapped_a} and {swapped_b}")

    n = int(input("Please enter a number to print in descending order: "))
    print(f"Natural descending order of {n} is: ", end="")
    print_descending(n)