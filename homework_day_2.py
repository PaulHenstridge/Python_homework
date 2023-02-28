def part_a():
    stops = [
        "Glasgow Queen Street",
        "Croy",
        "Cumbernauld",
        "Falkirk High",
        "Polmont",
        "Linlithgow",
        "Livingston",
        "Haymarket",
        "Edinburgh Waverly",
    ]

    # 1. Add "Edinburgh Waverley" to the end of the list
    # 2. Add "Glasgow Queen St" to the start of the list
    # 3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
    # 4. Print out the index position of "Linlithgow"

    print(stops.index("Linlithgow"))
    # 5. Remove "Livingston" from the list using its name
    stops.remove("Livingston")
    # 6. Delete "Cumbernauld" from the list by index
    stops.pop(2)
    # 7. Print the number of stops there are in the list
    print(len(stops))
    # 8. Sort the list alphabetically
    stops.sort()
    # 9. Reverse the positions of the stops in the list
    stops.reverse()
    # 10 Print out all the stops using a for loop
    for stop in stops:
        print(stop)


def part_b():
    users = {
        "Jonathan": {
            "twitter": "jonnyt",
            "lottery_numbers": [6, 12, 49, 33, 45, 20],
            "home_town": "Stirling",
            "pets": [
                {"name": "fluffy", "species": "cat"},
                {"name": "fido", "species": "dog"},
                {"name": "spike", "species": "dog"},
            ],
        },
        "Erik": {
            "twitter": "eriksf",
            "lottery_numbers": [18, 34, 8, 11, 24],
            "home_town": "Linlithgow",
            "pets": [
                {"name": "nemo", "species": "fish"},
                {"name": "kevin", "species": "fish"},
                {"name": "spike", "species": "dog"},
                {"name": "rupert", "species": "parrot"},
            ],
        },
        "Avril": {
            "twitter": "bridgpally",
            "lottery_numbers": [12, 14, 33, 38, 9, 25],
            "home_town": "Dunbar",
            "pets": [{"name": "monty", "species": "snake"}],
        },
    }

    # 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
    print(users["Jonathan"]["twitter"])
    # 2. Get Erik's hometown
    print(users["Erik"]["home_town"])

    # 3. Get the list of Erik's lottery numbers
    print(users["Erik"]["lottery_numbers"])

    # 4. Get the species of Avril's pet Monty
    print(users["Avril"]["pets"][0]["species"])

    # 5. Get the smallest of Erik's lottery numbers
    print(min(users["Erik"]["lottery_numbers"]))

    # 6. Return an list of Avril's lottery numbers that are even
    avrils_nums = []
    for num in users["Avril"]["lottery_numbers"]:
        if num % 2 == 0:
            avrils_nums.append(num)

    print(avrils_nums)

    # 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
    users["Erik"]["lottery_numbers"].append(7)
    print(users["Erik"]["lottery_numbers"])
    # 8. Change Erik's hometown to Edinburgh
    users["Erik"]["home_town"] = "Edinburgh"
    print(users["Erik"]["home_town"])
    # 9. Add a pet dog to Erik called "fluffy"

    users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
    print(users["Erik"]["pets"])
    # 10. Add another person to the users dictionary

    users["Bob"] = {
        "twitter": "bobby",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Aberdeen",
        "pets": [
            {"name": "fred", "species": "pig"},
        ],
    }

    print(users)


def part_c():
    united_kingdom = [
        {"name": "Scotland", "population": 5295000, "capital": "Edinburgh"},
        {"name": "Wales", "population": 3063000, "capital": "Swansea"},
        {"name": "England", "population": 53010000, "capital": "London"},
    ]

    # 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
    united_kingdom[1]["capital"] = "Cardiff"
    print(united_kingdom[1])
    # 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
    northern_ireland = {
        "name": "Northern Ireland",
        "population": 1811000,
        "capital": "Belfast",
    }
    united_kingdom.append(northern_ireland)
    print(united_kingdom)
    # 3. Use a loop to print the names of all the countries in the UK.
    for country in united_kingdom:
        print(country["name"])
    # 4. Use a loop to find the total population of the UK.

    total_pop = 0

    for country in united_kingdom:
        total_pop += country["population"]
    print(total_pop)


def part_d():
    # For the following list of numbers:

    numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

    # 1. Print out a list of the even integers:
    for num in numbers:
        if num % 2 == 0:
            print(num)

    # 2. Print the difference between the largest and smallest value:
    print(max(numbers) - min(numbers))

    # 3. Print True if the list contains a 2 next to a 2 somewhere.
    for i in range(len(numbers)):
        if numbers[i] == 2 and numbers[i + 1] == 2:
            print(True)

    # 4. Print the sum of the numbers,
    #    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
    #
    #    So [11, 6, 4, 99, 7, 11] would have sum of 22

    total = 0
    valid_num = True
    for i in range(len(numbers)):
        if numbers[i] == 6:
            valid_num = False
        if numbers[i - 1] == 7:
            valid_num = True
        if valid_num:
            print(numbers[i])
            total += numbers[i]

    print(sum(numbers))
    print(total)

    # 5. HARD! Print the sum of the numbers.
    #    Except the number 13 is very unlucky, so it does not count.
    #    And numbers that come immediately after a 13 also do not count.
    #    HINT - You will need to track the index throughout the loop.
    #
    #    So [5, 13, 2] would have sum of 5.

    unlucky = numbers.index(13)
    numbers.pop(unlucky + 1)
    numbers.pop(unlucky)
    print(sum(numbers))


part_a()
# part_b()
# part_c()
# part_d()
