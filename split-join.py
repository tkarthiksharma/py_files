def split_and_join(line):
    line=line.split(" ")
    line = "-".join(line)
    return (line)


def swapCase(line):
    line = line.swapcase()
    return (line)


if __name__ == '__main__':
    line=input(" give me a sentence : ")
    result=split_and_join(line)
    result1=swapCase((line))
    print(result)
    print(result1)


def print_full_name(a, b):
    print("Hello", a.capitalize(), b.capitalize(),"! You just delved into python.",sep=" ")
    print("")



if __name__ == '__main__':
    first_name = input("Enter the First name: ")
    last_name = input("Enter the second name: ")
    print_full_name(first_name, last_name)



