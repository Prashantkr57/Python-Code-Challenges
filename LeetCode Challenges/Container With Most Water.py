def max_area(height):
    # Time limit exceeded
    area = 0

    """for i in range(len(height)):
        for j in range(1, len(height)):
            cal_area = min(height[i], height[j]) * (j - i)
            if cal_area > area:
                area = cal_area"""

    # No Time limit error
    i, j = 0, len(height) - 1
    while i < j:
        cal_area = min(height[i], height[j]) * (j - i)
        area = max(area, cal_area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
