# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kings", (15, 15)), ("Chargers", (20, 10)),
                  ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # TODO: create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)

    # TODO: Use popitem to remove the top item
    team, record = teams.popitem(False)
    print(team, record)
    print(teams)

    # TODO: What are next the top 4 teams?
    for i, item in enumerate(teams.items(), start=1):
        team, record = item
        print(i, team, record)
        if i == 4:
            break

    # TODO: test for equality
    a = OrderedDict({'a': 1, 'b': 2})
    b = OrderedDict({'a': 1, 'b': 2})
    print(a == b)
    a = OrderedDict({'a': 1, 'b': 2})
    b = OrderedDict({'b': 2, 'a': 1, })
    print(a == b)
    a = OrderedDict({'a': 1, 'b': 2})
    b = {'b': 2, 'a': 1, }
    print(a == b)


if __name__ == "__main__":
    main()
