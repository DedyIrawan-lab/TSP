"""
    Author: Simon Westphahl <westphahl@gmail.com>
    Description: Brute-force implementation for solving the TSP.
    http://en.wikipedia.org/wiki/Travelling_salesman_problem
"""

routes = []


def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (cities[path[-1]].has_key(path[0])):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print path, distance
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (cities[city].has_key(node)):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'A': {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 20, 'F': 28},
        'B': {'A': 0, 'B': 0, 'C': 22, 'D': 18, 'E': 40, 'F': 26},
        'C': {'A': 0, 'B': 0, 'C': 0, 'D': 18, 'E': 26, 'F': 23},
        'D': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 15, 'F': 22},
		'E': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 12},
		'F': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    }

    print "Start: Node A"
    find_paths('A', cities, [], 0)
    print "\n"
    routes.sort()
    if len(routes) != 0:
        print "Shortest route: %s" % routes[0]
    else:
        print "FAIL!"
