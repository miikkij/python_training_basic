if __name__ == '__main__':
    n = int(input())
    input_array = list()

    # read n lines of input
    for i in range(n):
        input_array.append(input())

    for input_values in input_array:
        value, divider = input_values.split(' ')
        try:
            result = int(value) // int(divider)
            print(result)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
