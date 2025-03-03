routes = [[-20,-15],[-14,-5],[-18,-13],[-5,-3]]
routes.sort()
camera = routes[0]
answer = 1
for i in routes[1:]:
    if i[0] <= camera[1]:
        camera = [i[0],min(i[1],camera[1])]
    else:
        camera = i
        answer += 1