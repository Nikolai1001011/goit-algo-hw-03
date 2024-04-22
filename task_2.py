import random
def get_numbers_ticket(minimum:int, maximum:int, quantity:int)->int:
    # Checking the correctness of input parameters
    if not (1 <= minimum <= maximum <= 1000) or quantity <= 0:
        return []
    # Generate unique numbers in a given range
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(minimum, maximum))
    # Return a sorted list of unique numbers
    return sorted(list(numbers))
# example
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
