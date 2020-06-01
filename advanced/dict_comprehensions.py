#!usr/bin/env python3


# we should limit ourselves to 2 expressions within a comprehension in order
# to keep your code nice and readable. more than 2 expressions in a
# comprehension should require creating a separate function.
def main():
    # define a list of temperature values
    c_temps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    # here the predicate condition is if t < 100
    temp_dict = {t: (t * 9 / 5) + 32 for t in c_temps if t < 100}
    print(temp_dict)
    print(temp_dict[12])

    # Merge two dictionaries with a comprehension
    team1 = {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7}
    team2 = {'White': 12, 'Macke': 88, 'Perce': 4}
    print((team1, team2))

    # using two expressions in the comprehension
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# {0: 32.0, 12: 53.6, 34: 93.2}
# 53.6
# ({'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7}, {'White': 12, 'Macke': 88, 'Perce': 4})
# {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7, 'White': 12, 'Macke': 88, 'Perce': 4}
