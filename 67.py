string = open('./resources/p067_triangle.txt').read()

triangle = []
lists = string.split("\n")
lists = lists[:-1]

for row in lists:
    triangle.append(list(map(int, row.split(" "))))

# Work backwards through the triangle, stopping at each node to find the most optimal path
for x in range(len(triangle) - 1, -1, -1):
    for y in range(0, x):
        triangle[x-1][y] += max(triangle[x][y],triangle[x][y+1])

print(triangle[0][0])