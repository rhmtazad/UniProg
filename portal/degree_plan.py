class DegreePlan:
    def __init__(self, name, year, database, course):
        """
        Manage courses that belongs a specific degree plan

        Note:
            Pass the name and year in the first and second
            parameter and the database object with course
            object in the third and fourth parameter.

        Examples:
            >>> degree_plan = DegreePlan('ITCS', 2021, 'DB Obj', 'Course Obj')

        Args:
            name (str): Create the degree plan with this name
            year (int): Create the degree plan with this year
            database (:obj:`Schema`): Use composition for database object
            course (:obj:`Course`): Use composition for course object

        Attributes:
            self.__name (str): Store the name of the degree plan
            self.__year (int): Store the year of the degree plan
            self.__db (:obj:`Schema`): Use composition for the database.
            self.__course (:obj:`Course`): Use composition for the course.
        """

        # store the name and year for the degree plan
        self.__name = name
        self.__year = year

        # use composition for database and course objects
        self.__db = database
        self.__course = course

    def __str__(self):
        """
        String representation of the DegreePlan object

        Returns:
            Returns the name, year, and remaining courses in a degree plan
        """

        return f'Name: {self.name}, Year: {self.year}, Remaining: {self.count(taken=0)}'

    @property
    def name(self):
        """
        Get the name of the degree plan

        Examples:
            >>> print(self.name)

        Returns:
            Returns the name of the degree plan
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the name of the degree plan

        Examples:
            >>> self.name = 'MBA'

        Args:
            name (str): Set the name of the degree plan

        Returns:
            Returns nothing
        """

        self.__name = name

    @property
    def year(self):
        """
        Get the year of the degree plan

        Examples:
            >>> print(self.year)

        Returns:
            Returns the year of the degree plan
        """

        return self.__year

    @year.setter
    def year(self, year):
        """
        Set the year of the degree plan

        Examples:
            >>> self.year = 2021

        Args:
            year (int): Set the year of the degree plan

        Returns:
            Returns nothing
        """
        self.__year = year

    def count(self, **col_val):
        """
        Count the number of courses in a degree plan

        Note:
            Pass the columns and values as keyword arguments.
            The first part in key=val represents the column and
            the second part represents the value for that column.
            This function return the count of courses based on the
            columns and values that are passed on as parameters.

        Examples:
            >>> print(self.count(major='ITCS', credit='3'))

        Args:
            **col_val (:obj:`kwargs`): Count based on these columns and values.

        Keyword Args:
            **col_val (:obj:`kwargs`): The first part in key=val represents the
                column name and the second part represents the column value.

        Returns:
            Returns the count of courses.
        """

        return self.__course.count(major=self.name, **col_val)

    def filter(self, **col_val):
        """
        Filter the courses in a degree plan

        Note:
            Pass the columns and values as keyword arguments.
            The first part in key=val represents the column and
            the second part represents the value for that column.
            This function return the courses based on the columns
            and values that are passed on as parameters.

        Examples:
            >>> print(self.filter(major='ITCS', credit='3'))

        Args:
            **col_val (:obj:`kwargs`): Filter based on these columns and values.

        Keyword Args:
            **col_val (:obj:`kwargs`): The first part in key=val represents the
                column name and the second part represents the column value.

        Returns:
            Returns the filtered courses based on the column and values.
        """

        return self.__course.filter(major=self.name, **col_val)
