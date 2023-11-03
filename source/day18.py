from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int
    z: int

    def adjacent_points(self):
        return [
            Point(self.x - 1, self.y, self.z),
            Point(self.x + 1, self.y, self.z),
            Point(self.x, self.y - 1, self.z),
            Point(self.x, self.y + 1, self.z),
            Point(self.x, self.y, self.z - 1),
            Point(self.x, self.y, self.z + 1)]


def solution_a(points):
    surface_area = 0
    point_set = set(points)
    for point in points:
        neighbours = point.adjacent_points()
        for neighbour in neighbours:
            if neighbour not in point_set:
                surface_area += 1
    return surface_area


def solution_b(points):
    min_x, max_x = min(point.x for point in points), max(point.x for point in points)
    min_y, max_y = min(point.y for point in points), max(point.y for point in points)
    min_z, max_z = min(point.z for point in points), max(point.z for point in points)
    lava = list(points)
    exterior = []
    is_exterior = lambda \
            p: min_x - 1 <= p.x <= max_x + 1 and min_y - 1 <= p.y <= max_y + 1 and min_z - 1 <= p.z <= max_z + 1 and lava.index(
        p) == lava[-1] and exterior.index(p) == exterior[-1]
    queue = [Point(min_x - 1, min_y - 1, min_z - 1)]
    while queue:
        point = queue.pop()
        if is_exterior(point):
            exterior.append(point)
            queue.append(point.adjacent_points())
    surface_area = 0
    for point in points:
        for neighbour in point.adjacent_points():
            if exterior.index(neighbour) != exterior[-1]:
                surface_area += 1
    return surface_area


if __name__ == '__main__':
    points = []
    with open("../inputs/test_18") as file:
        lines = file.readlines()
        for line in lines:
            x, y, z = line.strip().split(",")
            points.append(Point(int(x), int(y), int(z)))
    print(f"Part A: {solution_a(points)}")
    print(f"Part B: {solution_b(points)}")

