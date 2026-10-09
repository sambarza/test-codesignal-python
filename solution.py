def digit_to_donate(house_number, step):

    if step > len(house_number):
        return None

    donated_digit = house_number[(step) * -1]

    return donated_digit

def donate_digit(house_number, step_number):

    if step_number > len(house_number):
        return house_number

    char_index_to_remove = len(house_number) - step_number

    return house_number[:char_index_to_remove] + house_number[char_index_to_remove + 1:]

def calculate_new_state(house_numbers, step_number):

    new_house_numbers = house_numbers[:]

    for index_of_donating_house in range(len(house_numbers) - 1, -1, -1):
        if index_of_donating_house == len(house_numbers) - 1:
            index_of_receiving_house = 0
        else:
            index_of_receiving_house = index_of_donating_house + 1

        donated_number = digit_to_donate(house_numbers[index_of_donating_house], step_number)

        if not donated_number:
            continue

        new_house_numbers[index_of_donating_house] = donate_digit(new_house_numbers[index_of_donating_house], step_number)
        new_house_numbers[index_of_receiving_house] = donated_number + new_house_numbers[index_of_receiving_house]

    return new_house_numbers


def house_game(house_numbers_int):

    house_numbers = [str(house_number) for house_number in house_numbers_int]
    step = 0

    while True:
        step += 1

        new_houses = calculate_new_state(house_numbers, step)
        print(house_numbers, " --> ", new_houses)

        if new_houses == house_numbers:
            break

        house_numbers = new_houses

    return [int(house_number) for house_number in new_houses]