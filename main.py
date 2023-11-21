import matplotlib.pyplot as plt
import copy
import matplotlib.animation as animation
class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        '''
        Initializes the class object with the specified dimensions.

        Parameters:
        x_dim: An integer, this represents the length of the x dimension in the games grid size.
        y_dim: An integer, this represents the length of the y dimension in the games grid size.

        Returns:
        A 2-d array of the specified size with zeros as values.
        '''
        # Given two integers return a matrix with dimensions using the two dimensions
        # with zeros in every element.

        self.life_grid = [[0 for i in range(x_dim)] for j in range(y_dim)]
        pass

    def get_grid(self):
        '''
        Returns the games current state.

        Parameters:


        Returns:
        The current life_grid.
        '''

        return self.life_grid

    def print_grid(self):
        '''
        Print the current iteration of the games life_grid in an intuitive format

        Parameters:


        Returns:
        Nothing, only print an output to the terminal.
        '''

        for row in self.life_grid:
            for col in row:
                print(col,end=' ')
                print('|',end=' ')
            print('\n')
            print(' - '*len(row))
        pass

    def populate_grid(self,coord):
        '''
        Populates the game grid with live cells at the specified coordinates.

        Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

        Returns:
        The updated life_grid with the new live cells.
        '''
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.

        for i in coord:
            self.life_grid[i[0]][i[1]] = 1
        return self
        pass

    def make_step(self):
        '''
        Generate the next state of the game from the current position of the live and dead cells.

        Parameters:


        Returns:
        Self.
        '''
        # Iterate through every cell in the life_grid and determine if it will be dead or
        # alive in the next iteration by using the rules of the game, update the values
        # of the life_grid.

        temp_grid = copy.deepcopy(self.life_grid)
        for row in range(len(self.life_grid)):
            for col in range(len(self.life_grid[row])):
                sum_grid = 0

                front_edge = col+1
                if front_edge > len(self.life_grid[row]):
                    front_edge = len(self.life_grid[row])

                back_edge = col-1
                if back_edge < 0:
                    back_edge = 0

                top = row-1
                if top<0:
                    top = 0

                bottom = row+1
                if bottom > len(self.life_grid):
                    bottom = len(self.life_grid)


                cube = []
                for row_1 in self.life_grid[top:bottom+1]:
                    cube.append(row_1[back_edge:front_edge+1])

                for row_2 in cube:
                    for cell_2 in row_2:
                        sum_grid += cell_2

                if self.life_grid[row][col] == 1:
                    sum_grid -= 1



                if self.life_grid[row][col] == 1:
                    if sum_grid < 2:
                        temp_grid[row][col] = 0
                        # self.life_grid[row][col] = 0
                    if sum_grid == 2 or sum_grid == 3:
                        temp_grid[row][col] = 1
                        # self.life_grid[row][col] = 1
                    if sum_grid > 3:
                        temp_grid[row][col] = 0
                        # self.life_grid[row][col] = 0
                if self.life_grid[row][col] == 0 and sum_grid == 3:
                    temp_grid[row][col] = 1
                    # self.life_grid[row][col] = 1
        self.life_grid = copy.deepcopy(temp_grid)
        return self

        pass

    def make_n_steps(self,frames):
        '''
        Step through multiple iterations of the games evolution by using the make_step method.

        Parameters:
        n: An integer that specifies how many iterations or evolutions the game should run through.

        Returns:
        Self.
        '''
        # Given an integer run the make_step method that many times to evolve the life_grid.
        i = 1
        while i < frames+1:
            self.make_step()
            i += 1
        return self
        pass

    def draw_grid(self,file_name):
        '''
        Give a good schematic of the games current state.

        Parameters:


        Returns:
        Nothing, it outputs an image using the matplotlib show() method.
        '''
        # Using the life_grid create two lists that contain the coordinates for all the cells
        # in the game, then incorporate the state of the cell to color them in on a scatter plot.

        x = []
        y = []
        for row in range(len(self.life_grid)):
            for col in range(len(self.life_grid[row])):
                x.append(col)
                y.append(row)
        global fig
        fig,ax = plt.subplots()
        plt.scatter(x,y,c=self.life_grid)
        plt.gca().invert_yaxis()
        plt.savefig(file_name)
        plt.show()
        return x,y
        pass


game = GameOfLife(30,30)
game.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])
game.draw_grid("conway_game_iter_1.png")
game.make_n_steps(3)
game.draw_grid("conway_game_iter_2.png")