def calculate_polygon_area(vertices: list[tuple[float, float]]) -> float:
    """
    Calculates the area of a non-self-intersecting polygon using the Shoelace formula.
    Supports both convex and concave polygons.

    >>> calculate_polygon_area([(0, 0), (4, 0), (4, 3), (0, 3)])
    12.0
    >>> calculate_polygon_area([(0, 0), (3, 0), (3, 4)])
    6.0
    """
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        # Gauss's shoelace formula core logic
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()