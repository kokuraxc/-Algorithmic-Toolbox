# python3
import sys


# def compute_min_refills(distance, tank, stops: list):
#     # write your code here
#     stops.append(distance)
#     cur_pos = 0
#     total_stops = 0
#     tank_cap = tank
#     for stop in stops:
#         cur_distance = stop - cur_pos
#         if cur_distance <= tank_cap:
#             tank_cap -= cur_distance
#             cur_pos = stop
#         else:
#             if tank >= cur_distance:
#                 tank_cap = tank
#                 tank_cap -= cur_distance
#                 cur_pos = stop
#                 total_stops += 1
#             else:
#                 return -1
#     if tank_cap == 0:
#         total_stops += 1
#     return total_stops

def compute_min_refills(distance, tank, stops: list):
    stops.append(distance)
    return _inner(tank, tank, 0, stops)

def _inner(tankrem, tankcap, curstop, stops: list):
    if len(stops) == 0:
        return 0

    distance = stops[0] - curstop
    if tankrem > distance:
        return _inner(tankrem-distance, tankcap, stops[0], stops[1:])
    elif tankrem == distance:
        if len(stops) > 1:
            return 1 + _inner(tankcap, tankcap, stops[0], stops[1:])
        else:
            return 0
    else:
        if tankcap < distance:
            return -500
        else:
            return 1 + _inner(tankcap, tankcap, curstop, stops)

if __name__ == "__main__":
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    d, m, _, *stops = map(int, input().split())
    print(d, m, _, stops)
    total_stops = compute_min_refills(d, m, stops)
    if total_stops < 0:
        print(-1)
    else:
        print(total_stops)
