def solve_joltage_puzzle(battery_banks, num_batteries):
    """
    Calculates the total maximum joltage by finding the largest number 
    formed by selecting `num_batteries` digits from each bank.

    Args:
        battery_banks (list of str): A list where each string is a battery bank.
        num_batteries (int): The exact number of batteries to turn on in each bank.

    Returns:
        int: The sum of the maximum joltage (number) from all banks.
    """
    total_joltage = 0
    
    for bank in battery_banks:
        bank = bank.strip()
        n = len(bank)
        k = num_batteries
        num_deletions = n - k
        
        digits = list(bank)
        
        stack = []
        
        for digit in digits:
            while stack and num_deletions > 0 and digit > stack[-1]:
                stack.pop()
                num_deletions -= 1
            stack.append(digit)
            
        while num_deletions > 0:
            stack.pop()
            num_deletions -= 1

        max_joltage_str = "".join(stack)
        total_joltage += int(max_joltage_str)
        
    return total_joltage


puzzle_input = open("3/input.txt", "r")
battery_banks = puzzle_input.readlines()

result = solve_joltage_puzzle(battery_banks, num_batteries=12)

print(f"Total maximun output of joltage: {result}")