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

    def check_surrounding(self, xy_coordinates):
        """
        Checks the surrounding squares of the xy_coordinates(x,y) and returns 
        number of live squares
        Parameters
        ----------
        xy_coordinates: tuple
            (x,y) of matrix
        Returns
        -------
        int
            number of live squares surrounding
        """
        pass

    def get_value_at(self, xy_coordinates):
        """
        Get the value set at xy_coordinates(x,y)
        """
        try:
            return self.matrix[xy_coordinates]
        except KeyError:
            return 0
