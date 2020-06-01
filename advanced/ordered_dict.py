#!usr/bin/env python3
from collections import OrderedDict


# the OrderedDict is a dictionary object that remembers the order in which
# items are inserted
def main():
    # list of sport teams with wins and losses records
    sport_teams = [
        ("Royals", (18, 12)), ("Rockets", (24, 6)),
        ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
        ("Kings", (15, 15)), ("Chargers", (20, 10)),
        ("Jets", (16, 14)), ("Warriors", (25, 5))
    ]

    # sort the teams by number of wins
    sorted_teams = sorted(sport_teams, key=lambda st: st[1][0], reverse=True)
    print(sorted_teams)

    # create an ordered dictionary of the teams.
    # the OrderedDict won't keep things sorted for me.
    # if I make changes by moving things around or changing the data, then
    # I'll need to resort it myself
    teams = OrderedDict(sorted_teams)
    print(teams)

    # Use popitem to remove the top item as if the dict was a stack
    # default arg for pop can be true or false. true will be for getting the
    # last item added, false will be for the 1st item added
    tm, wl = teams.popitem(False)
    print('(1st added) Top team:', tm, wl)
    tm, wl = teams.popitem()
    print('(last added) Last team:', tm, wl)

    # What are next the top 4 teams? we can just iterate normally
    for index, team in enumerate(teams, start=1):
        print(index, team)
        if index == 4:
            break

    # in ordered dicts the equality depends on the order of the values.
    # they have to be the same values and same order for 2 ordered dicts to
    # be equal
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    c = OrderedDict({"a": 1, "b": 1, "c": 2})
    d = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("Equality test: a == b", a == b)
    print("Equality test: a == c", a == c)
    print("Equality test: a == d", a == d)

    # when comparing an OrderedDict to a regular dict, the order doesn't matter
    x = OrderedDict({"a": 1, "b": 2, "c": 3})
    y = {"a": 1, "c": 2, "b": 3}
    z = {"a": 1, "c": 3, "b": 2}
    print("Equality test: x == y", x == y)
    print("Equality test: x == z", x == z)


if __name__ == "__main__":
    main()

# CONSOLE OUTPUT:
# [('Warriors', (25, 5)), ('Rockets', (24, 6)), ('Dragons', (22, 8)), ('Cardinals', (20, 10)), ('Chargers', (20, 10)), ('Royals', (18, 12)), ('Jets', (16, 14)), ('Kings', (15, 15))]
# OrderedDict([('Warriors', (25, 5)), ('Rockets', (24, 6)), ('Dragons', (22, 8)), ('Cardinals', (20, 10)), ('Chargers', (20, 10)), ('Royals', (18, 12)), ('Jets', (16, 14)), ('Kings', (15, 15))])
# (1st added) Top team: Warriors (25, 5)
# (last added) Last team: Kings (15, 15)
# 1 Rockets
# 2 Dragons
# 3 Cardinals
# 4 Chargers
# Equality test: a == b False
# Equality test: a == c False
# Equality test: a == d True
# Equality test: x == y False
# Equality test: x == z True
