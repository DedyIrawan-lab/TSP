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
        'A': {'A': 0, 'B': 10, 'C': 30, 'D': 31, 'E': 20, 'F': 28, 'G': 44, 'H': 43, 'I': 10, 'J': 21},
        'B': {'A': 10, 'B': 0, 'C': 22, 'D': 18, 'E': 40, 'F': 26, 'G': 37, 'H': 39, 'I': 19, 'J': 39},
        'C': {'A': 30, 'B': 22, 'C': 0, 'D': 18, 'E': 26, 'F': 23, 'G': 50, 'H': 18, 'I': 41, 'J': 41},
        'D': {'A': 31, 'B': 18, 'C': 18, 'D': 0, 'E': 15, 'F': 22, 'G': 42, 'H': 20, 'I': 12, 'J': 30},
		'E': {'A': 20, 'B': 40, 'C': 26, 'D': 15, 'E': 0, 'F': 12, 'G': 10, 'H': 15, 'I': 47, 'J': 34},
		'F': {'A': 28, 'B': 26, 'C': 23, 'D': 22, 'E': 12, 'F': 0, 'G': 16, 'H': 33, 'I': 28, 'J': 18},
		'G': {'A': 44, 'B': 37, 'C': 50, 'D': 42, 'E': 10, 'F': 16, 'G': 0, 'H': 31, 'I': 37, 'J': 48},
		'H': {'A': 43, 'B': 39, 'C': 18, 'D': 20, 'E': 15, 'F': 33, 'G': 31, 'H': 0, 'I': 34, 'J': 45},
		'I': {'A': 10, 'B': 19, 'C': 41, 'D': 12, 'E': 47, 'F': 28, 'G': 37, 'H': 34, 'I': 0, 'J': 28},
		'J': {'A': 21, 'B': 39, 'C': 41, 'D': 30, 'E': 34, 'F': 18, 'G': 48, 'H': 45, 'I': 28, 'J': 0}
    }

    print "Start: Node A"
    find_paths('A', cities, [], 0)
    print "\n"
    routes.sort()
    if len(routes) != 0:
        print "Shortest route: %s" % routes[0]
    else:
        print "FAIL!"
