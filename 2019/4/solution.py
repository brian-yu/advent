




LO = 145852
HI = 616942


def part_1():
    def is_valid(num):
        has_double = False
        num_str = str(num)

        for i in range(1, len(num_str)):
            if int(num_str[i-1]) > int(num_str[i]):
                return False
            if num_str[i-1] == num_str[i]:
                has_double = True

        return has_double

    valid_passwords = 0

    for num in range(LO, HI + 1):
        if is_valid(num):
            valid_passwords += 1

    print(valid_passwords)



def part_2():
    def is_valid(num):
        has_double = False
        num_str = str(num)

        for i in range(1, len(num_str)):
            if int(num_str[i-1]) > int(num_str[i]):
                return False
            if num_str[i-1] == num_str[i]:
                before = None if i-2 < 0 else num_str[i-2]
                after = None if i+1 == len(num_str) else num_str[i+1]
                if before != num_str[i] and after != num_str[i]:
                    has_double = True

        return has_double

    valid_passwords = 0

    for num in range(LO, HI + 1):
        if is_valid(num):
            valid_passwords += 1

    print(valid_passwords)

part_1()


part_2()
