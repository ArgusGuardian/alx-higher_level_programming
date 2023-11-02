#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv, exit
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    argv[1] = int(argv[1])
    argv[3] = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(argv[1], argv[3],
              calculator_1.add(argv[1], argv[3])))
    elif argv[2] == '-':
        print("{} - {} = {}".format(argv[1], argv[3],
              calculator_1.sub(argv[1], argv[3])))
    elif argv[2] == '*':
        print("{} * {} = {}".format(argv[1], argv[3],
              calculator_1.mul(argv[1], argv[3])))
    elif argv[2] == '/':
        print("{} / {} = {}".format(argv[1], argv[3],
              calculator_1.div(argv[1], argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
