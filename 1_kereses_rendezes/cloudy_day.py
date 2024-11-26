#!/bin/python3
import os

def maximumPeople(populations, town_locations, cloud_locations, cloud_ranges):
    events = []
    n = len(populations)

    for i in range(n):
        events.append((town_locations[i], 'town', populations[i], i))

    for j in range(len(cloud_locations)):
        left = cloud_locations[j] - cloud_ranges[j]
        right = cloud_locations[j] + cloud_ranges[j]
        events.append((left, 'cloud_start', j))
        events.append((right + 1, 'cloud_end', j))

    events.sort()

    active_clouds = set()
    cloud_population = [0] * len(cloud_locations)
    sunny_population = 0
    for event in events:
        pos, event_type, value, *extra = event
        if event_type == 'town':
            if len(active_clouds) == 0:
                sunny_population += value
            elif len(active_clouds) == 1:
                cloud_idx = next(iter(active_clouds))
                cloud_population[cloud_idx] += value
        elif event_type == 'cloud_start':
            active_clouds.add(value)
        elif event_type == 'cloud_end':
            active_clouds.remove(value)

    return sunny_population + max(cloud_population, default=0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
