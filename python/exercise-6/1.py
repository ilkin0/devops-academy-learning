examResults = {'fizika': [80, 88, 93, 78, 65, 99, 30, 45],
               'kimya': [23, 76, 88, 79, 56, 96, 85, 83],
               'riyaziyyat': [93, 87, 91, 69, 74, 88, 81, 99]}


def custom_sort(e):
    return examResults.values()


sortedResults = sorted(examResults.items(), key=custom_sort())

print(sortedResults)
