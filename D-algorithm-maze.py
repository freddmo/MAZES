from pyamaze import maze, agent,COLOR,textLabel

# print(m.maze_map) #(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},

def dijkstra(m, *h):

    hurdles = [(i.position, i.cost) for i in h]
    unvisited = {n:float('inf') for n in m.grid} # put all the values to be visited into infinity
    unvisited[m.rows, m.cols] = 0 #we are currently in the node so the distance to it is zero
    visited = {}
    parents = {}

    while unvisited:
        Current_cell = min(unvisited, key=unvisited.get)
        visited[Current_cell] = unvisited[Current_cell]
        if Current_cell == (1,1):
            break
        for x in 'EWNS':
            if m.maze_map[Current_cell][x] == True:
                if x == 'E':
                    neighbor = (Current_cell[0], Current_cell[1]+1)
                elif x == 'W':
                    neighbor = (Current_cell[0], Current_cell[1]-1)
                elif x == 'S':
                    neighbor = (Current_cell[0]+1, Current_cell[1])
                elif x == 'N':
                    neighbor = (Current_cell[0]-1, Current_cell[1])
                if neighbor in visited:
                    continue

                Distance = unvisited[Current_cell]+1
                for hurdle in hurdles:
                    if hurdle[0] == Current_cell:
                        Distance+=hurdle[1]



                if Distance < unvisited[neighbor]:
                    unvisited[neighbor] = Distance
                    parents[neighbor] = Current_cell

        unvisited.pop(Current_cell)

    the_path = {}
    current_node = (1,1)
    while current_node != (m.rows,m.cols):
        the_path[parents[current_node]] = current_node
        current_node = parents[current_node]

    return the_path,visited[(1,1)]



if __name__=='__main__':

    m = maze(6,6)
    m.CreateMaze(loopPercent=50) #we can generate a maze with multiple paths by setting the optional argument loopPercent to some positive number. loopPercent set to highest value 100 means the maze generation algorithm will maximize the number of multiple paths 

    spy1 = agent(m,5,5,color=COLOR.red)

    spy2 = agent(m,4,4,color=COLOR.blue)

    spy3 = agent(m,3,2,color=COLOR.green)

    spy4 = agent(m,2,2,color=COLOR.cyan)

    spy1.cost = 100
    spy2.cost = 100
    spy3.cost = 100
    spy4.cost = 100

    path,c = dijkstra(m,spy1,spy2,spy3,spy4)
    textLabel(m,'Total Cost', c)

    a = agent(m, color=COLOR.cyan, filled=True, footprints=True)
    m.tracePath({a:path})

    m.run()


