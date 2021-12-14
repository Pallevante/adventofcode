

def read_file() -> list: 
    list_of_items = []
    with open("data.txt", "r") as file:
        for item in file.readlines():
            list_of_items.append(item)
    return list_of_items

def main():
    gamma_rate = ''
    epsilon = ''
    my_list = read_file()

    for pos in range(0, 12):      
        ones = 0
        zeroes = 0
        for item in my_list:
            if (int(item[pos]) == 1):
                ones += 1 
            elif(int(item[pos]) == 0):
                zeroes += 1
        if(ones > zeroes):
            gamma_rate += '1'
            epsilon += '0'
        else:
            gamma_rate += '0'
            epsilon += '1'

    print(f"gamma: {gamma_rate} epsilon: {epsilon}")
    sum = int(gamma_rate, 2) * int(epsilon, 2)
    print(f"sum {sum}")
main()