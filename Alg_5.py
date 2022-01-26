from itertools import product


def calculator(program, value):
    acc = value
    for command in program:
        if command == "1":
            acc += 2
        elif command == "2":
            acc *= 3
    return acc


def build_program(start, finish, length):
    for i in range(1, length + 1):
        space = ["12"] * i
        for pt in product(*space):
            program = "".join(pt)
            result = calculator(program, start)
            if result == finish:
                return program
    return None


if __name__ == "__main__":
    program = build_program(1, 31, 5)
    if program is not None:
        print(program)
    else:
        print("Решений нет")
