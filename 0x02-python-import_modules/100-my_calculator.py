#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":

    args = sys.argv
    args_len = len(args)

    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oand1 = int(args[1])
    op = args[2]
    oand2 = int(args[3])

    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(oand1, op, oand2,
                                             calculator_1.add(oand1, oand2)))
        sys.exit(0)

    if op == '-':
        print("{:d} {:s} {:d} = {:d}".format(oand1, op, oand2,
                                             calculator_1.sub(oand1, oand2)))
        sys.exit(0)

    if op == '*':
        print("{:d} {:s} {:d} = {:d}".format(oand1, op, oand2,
                                             calculator_1.mul(oand1, oand2)))
        sys.exit(0)

    if op == '/':
        print("{:d} {:s} {:d} = {:d}".format(oand1, op, oand2,
                                             calculator_1.div(oand1, oand2)))
        sys.exit(0)
