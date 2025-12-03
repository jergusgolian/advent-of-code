file = open("3/test.txt", "r")
instructions = file.readlines()

def biggest(bank, n):
    n_highest = ""
    for repeat in range(n):
        highiest = 0
        bank = str(bank).strip()
        for battery in range(0, len(bank) - repeat + 1):
            if int(bank[battery]) > int(highiest):
                highiest = bank[battery]
        n_highest += str(highiest)
    return(n_highest)

for bank in instructions:
    print(biggest(bank, 12))
