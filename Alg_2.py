def calculator(program, value):
    acc = value
    for command in program:
        if command == "1":
            acc *= acc
        elif command == "2":
            acc -= 1
    return acc


def build_program(start, end):
    for i in "*12":
        for j in "*12":
            for k in "*12":
                for n in "*12":
                    for m in "*12":
                        program = "".join([i, j, k, n, m])
                        result = calculator(program, start)
                        if result == end:
                            return program.replace("*", "")
    return None


if __name__ == "__main__":
    program = build_program(5, 8)
    if program is not None:
        print(program)
    else:
        print("Решений нет")
