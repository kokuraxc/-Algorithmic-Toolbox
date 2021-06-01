# Uses python3
import sys
from collections import namedtuple
from typing import List

Segment = namedtuple("Segment", "start end")


def containedInSegment(segment: Segment, pos: int) -> bool:
    return segment.start <= pos <= segment.end


def sortSegments(segments: List[Segment]) -> List[Segment]:
    return sorted(segments, key=lambda segment: segment.end)


def optimal_points(segments):
    points = []
    segments = sortSegments(segments)
    while len(segments) > 0:
        anchor = segments[0].end
        points.append(anchor)
        segments = [
            segment for segment in segments if not containedInSegment(segment, anchor)
        ]
    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # data = list(map(int, input().split()))
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
