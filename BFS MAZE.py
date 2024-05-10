#nota del desarrollador: "import could not be resolved vscode" se puede referir a que no esta
#abierta la carpeta donde se trabajara el archivo entonces tienes que ir a file, open folder y seleccionar tu carpeta.

from pyamaze.pyamaze import maze,agent

def BFS(m):
    start = (m.rows, m.cols)                                                       #-------------- This variable is a tuple.Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created. This makes them ideal for storing data that should not be modified, such as database records.
    Q_toexplore = [start]                                                          #-------------- queue to hold the cells to be epxlored
    Q_explored = [start]                                                           #-------------- Cells already explored
    bfs_path = {}                                                                  #-------------- This variable is a dictionary used to store the path discovered during the traversal.In Python, a dictionary is a built-in data structure that stores key-value pairs. It's a very versatile data structure and is commonly used for various purposes, including mapping keys to values
    while len(Q_toexplore)>0:
        current_cell = Q_toexplore.pop(0)
        if current_cell ==(1,1):                                                   #-------------- we always confirm first if we already find the target
            break
        for x in 'ESNW':                                                           #-------------- For each letter in the string we check if there is value 1
            if m.maze_map[current_cell][x]==True:                                  #-------------- maze_map = {(1, 1): {‘E’: 1, ‘W’: 0, ’N’: 0, ‘S’: 0}
                                                                                   #-------------- This line make sure there is a cell(x,y) to go to and not a wall.

                if x == 'E':
                    nextcell = (current_cell[0],current_cell[1]+1)
                elif x == 'W':
                    nextcell = (current_cell[0],current_cell[1]-1)
                elif x == 'N':
                    nextcell = (current_cell[0]-1,current_cell[1])
                elif x == 'S':
                    nextcell = (current_cell[0]+1,current_cell[1])
                if nextcell in Q_explored:
                    continue
                Q_toexplore.append(nextcell)                                       
                Q_explored.append(nextcell)
                bfs_path[nextcell] = current_cell                                  #--------------- The purpose of this line of code is to record that nextcell was reached from current_cell during the BFS traversal. 

    correctedPath = {}
    cell = (1,1)
    while cell != start:
        correctedPath[bfs_path[cell]] = cell                                        #-------------- This line saves ,in a variable cell, the parent of the current cell in a new dictionary
        cell = bfs_path[cell]                                                      #-------------- the line cell = bfs_path[cell] updates the cell variable to become its parent cell, allowing the while loop to continue tracing back the path until it reaches the start cell
    return correctedPath

m=maze(10,10)
m.CreateMaze()
path = BFS(m)

a = agent(m, footprints=True)                                                      #----------------what is an agent? An agent can be thought of as a physical agent like a robot or it can simply be used to highlight or point a cell in the maze.
m.tracePath({a:path})
m.run()

