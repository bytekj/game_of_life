!#/usr/bin/python3

class SparseMatrix:
    """
    This class implements functions over sparse matrix.
    """
    def __init__(self):
        self.matrix = dict()
    def add_element(self, xy_coordinates, value):
        """
        Set value to the co-ordinates
        Parameters
        ----------
        xy_coordinates: tuple
            (x,y) of matrix
        value: int
            0 or 1
        Retuns
        ------
        None
        """
        self.matrix.update({xy_coordinates:value})
    
    def add_new_elements(self, new_matrix):
        self.matrix.update(new_matrix.get_iterable())

    def check_surrounding(self, xy_coordinates):
        """
        Checks the surrounding squares of the xy_coordinates(x,y) and returns 
        number of live squares
        Parameters
       -----------
        xy_coordinates: tuple
            (x,y) of matrix
        Returns
        -------
        int
            number of live squares surrounding
        """
        x, y = xy_coordinates
        surrounding = self.get_value_at((x-1, y-1)) + self.get_value_at((x, y-1)) 
                    + self.get_value_at((x+1, y-1)) + self.get_value_at((x-1, y))
                    + self.get_value_at((x+1, y)) + self.get_value_at((x-1, y+1))
                    + self.get_value_at((x, y+1)) + self.get_value_at((x+1, y+1))
        return surrounding

    def get_value_at(self, xy_coordinates):
        """
        Get the value set at xy_coordinates(x,y)
        """
        try:
            return self.matrix[xy_coordinates]
        except KeyError:
            return 0

    def get_iterable(self):
        return self.matrix
