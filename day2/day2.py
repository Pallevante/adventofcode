import re 


def read_file() -> list: 
    list_of_items = []
    with open("data.txt", "r") as file:
        for item in file.readlines():
            list_of_items.append(item)
    return list_of_items

def find_command(item : str) -> str:
    return re.search("(.+)? ", item).group(1)

def find_amount(item: str) -> int:
    result = re.findall("\d", item)
    return int(result[0])

def main():
    horizontal_pos = 0
    aim = 0
    depth = 0
    my_list = read_file()
    for item in my_list:
        command = find_command(item)
        amnt = find_amount(item)
        if command == 'forward':
            horizontal_pos += amnt
            depth += (aim * amnt)

        if command == 'up':
            aim -= amnt
        if command == 'down':
            aim += amnt
        print(horizontal_pos, aim)

    print(f"horizontal: {horizontal_pos} \t depth: {depth} ")
    print(f"Total: {horizontal_pos * depth}")


main()