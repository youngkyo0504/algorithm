def minAreaRmect( points):
    min_area = 0
    hash_map = {}
    for i in range(len(points)):
        point = points[i]
        x = point[0]
        y = point[1]
        if not x in hash_map:
            hash_map[x] = {y: i}
        else:  # 있다면
            hash_map[x][y] = i

    for i in range(len(points) - 1):
        point1 = points[i]
        x1, y1 = point1[0], point1[1]
        for j in range(i, len(points)):
            point2 = points[j]
            x2, y2 = point2[0], point2[1]

            if x1 == x2 or y1 == y2:
                continue
            area = 0
            # 둘다 x,y다를 때
            print(x1,y1,x2,y2)
            if x2 in hash_map and x1 in hash_map:
                if y1 in hash_map[x2] and y2 in hash_map[x1]:
                    area = abs((x2 - x1) * (y2 - y1))
                    if min_area == 0 or min_area > area:
                        min_area = area
    return min_area

print(minAreaRmect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))