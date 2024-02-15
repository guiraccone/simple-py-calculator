repetition = int(input("How many numbers do you wish to operate with\n"))
numbers = []

for i in range(repetition):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)



operator = int(
    input("Type the operator: \n1 - Add \n2 - Subtract\n3 - Divide\n4 - Multiply\n"))

match operator:
    case 1:
        print("Result:", sum(numbers))
    case 2:
        result = 1
        for number in numbers:
            result -= number
        print("Result:", result)
    case 3:
        result = 1
        for number in numbers:
            result /= number
        print("Result:", result)
    case 4:
        result = 1
        for number in numbers:
            result *= number
        print("Result:", result)
        

    case _:
        print("Undefined operator.")
