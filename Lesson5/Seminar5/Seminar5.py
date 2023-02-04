from math import pi
import os

# S=pi*a*b
print("задача про орбиты")
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit(list_of_orbits):
    s_max = 0
    index = 0
    list_s = []

    def sqare(a, b):
        return pi * a * b

    for i in range(len(list_of_orbits)):
        x = list_of_orbits[i][0]
        y = list_of_orbits[i][1]
        if x != y:
            if sqare(x, y) > s_max:
                s_max = sqare(x, y)
                index = i
    list_s.append(pi * list_of_orbits[i][0] * list_of_orbits[i][1])

    return [list_of_orbits[index], s_max]
def find_farthest_orbit_plus(list_of_orbits):
	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
	list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
	max_area_index = list_of_areas.index(max(list_of_areas))
	return list_of_elliptical_orbits[max_area_index]
print(orbits)
print(find_farthest_orbit(orbits))
print('farthest orbit: ',find_farthest_orbit_plus(orbits), '\n')
print("задача про 'same_by(characteristic, objects)'")
values = [0, 2, 10, 6]

def same_by(f, list_num):
    # return set(map(f, list_num))
    return True if len(set(map(f, list_num))) == 1 else False

print(values)
print(same_by(lambda x: x % 1, values))
input()
