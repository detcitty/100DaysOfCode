# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

def maze_runner(maze, directions):
    # Code Here
    pass
    
test.describe("Example tests")

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

test.it("Should return Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
test.assert_equals(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")
