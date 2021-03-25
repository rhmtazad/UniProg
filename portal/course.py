class Course:
    def __init__(self, database):
        """
        Add, update, or remove a course.

        Note:
            To use this object, pass the hydraDB database as
            a parameter for the initializer of this object.
            If you want to use another database, use an adapter
            pattern and first create an adapter for the database.

        Examples:
            >>> # database can be Schema() or anything compatible
            >>> course = Course('database here...')

        Args:
            database (:obj:`Schema`): Create the database using this object.

        Attributes:
            self.__db (:obj:`Schema`): Use composition for the database.
            self.__table (str): Store the name of the table in the database.
        """

        # use composition for the database
        self.__db = database

        # store the table name for this object
        self.__table = 'course'

        # create the table and columns if not exist
        self.form_table()

    def __str__(self):
        """
        String representation of the Course object

        Returns:
            Returns the taken and the remaining courses
        """

        return f'Taken: {self.count(taken=1)}, Remaining: {self.count(taken=0)}'

    def form_table(self):
        """
        Create the table with columns for this object.

        Note:
            Use this function anywhere or inside the initializer
            of the object.

        Examples:
            >>> self.form_table()

        Returns:
            Returns nothing.
        """

        # create the table and columns using the database API
        self.__db.form_table(
            table=self.__table,
            name='text',
            major='text',
            category='text',
            credit='integer',
            taken='integer',
            grade='text'
        )

    def add(self, **data):
        """
        Add a course to the database.

        Note:
            Pass the course name, degree, category, credit amount,
            taken status, and grade as parameters. Taken status requires
            0 or 1 integer values.

        Examples:
            >>> self.add(name='ITC 315', major='ITCS', category='Core', taken=1)
            >>> self.add(name='ITC 210', major='ITCS', category='Core')

        Args:
            **data (:obj:`kwargs`): Add a course with the given data.

        Keyword Args:
            **data (:obj:`kwargs`): Pass the column name as key and
                the column value as value.

        Returns:
            Returns nothing.
        """

        # use the database API to add a new course
        self.__db.insert_row(self.__table, **data)

    def get(self, course_id, *info):
        """
        Fetch one or more columns from the course table.

        Note:
            Pass the course ID in the first parameter and
            the course info as column names in the database in the
            second parameter.

        Examples:
            >>> print(self.get(1, 'name', 'credit'))

        Args:
            course_id (int): Get the information for this course.
            *info (:obj:`list`): Get these information from a course.

        Returns:
            Returns the information as a list.
        """

        # use database API to fetch the specific cells
        return self.__db.fetch_cells(self.__table, course_id, *info)

    def filter(self, **col_val):
        """
        Filter courses based on their column values.

        Note:
            Pass the column name as a filter in the first
            parameter and the value as the filter condition.
            The first part in key=val represents the column
            and the second part represents that value.

        Examples:
            >>> print(self.filter(major='ITCS', category='Core'))

        Args:
            **col_val (:obj:`kwargs`): Filter the rows based on
                column and their values. Pass the column name as
                key and the value as value in the keword arguments.

        Keyword Args:
            **col_val (:obj:`kwargs`): The first part in key=val
                represents the column name and the second part
                represents the value. Pass as many filters as your
                want.

        Returns:
            Returns the fetch result after executing the query.
        """

        # fetch rows based on the given conditions using database API
        return self.__db.fetch_row(self.__table, **col_val)

    def update(self, course_id, **data):
        """
        Update a course information from the database.

        Note:
            Pass the course ID in the first parameter and
            the course information in the second parameter as
            Keyword Args or key='val'. For the second parameter,
            pass only the name of the columns along with their new
            values that you want to modify.

        Examples:
            >>> self.update(1, name='ITC 115', taken=1)

        Args:
            course_id (int): Update information of a course with this ID.
            **data (:obj:`kwargs`): Update a course with these information.

        Keyword Args:
            The first part in the key=val represents the column name and the second
            part represents the new value for that column. Number of columns are not
            limited.

        Returns:
            Returns nothing.
        """

        # update the course information using database API
        self.__db.update_row(self.__table, course_id, **data)

    def remove(self, course_id):
        """
        Remove a course from the database.

        Note:
            Pass the course ID (primary key) as a parameter.

        Examples:
            >>> self.remove(course_id=1)

        Args:
            course_id (int): Remove a course with this primary key.

        Returns:
            Returns nothing.
        """

        # remove a course using the database API
        self.__db.delete_row(self.__table, course_id)

    def count(self, **column_value):
        """
        Count the number of courses based on a column's value

        Note:
            Pass the column names and the column values as
            key=val parameters in which the key represents the
            column and the value represents the value.

        Examples:
            >>> self.count('major', 'ITCS')

        Args:
            **column_value (:obj:`kwargs`): Count the courses based on these column.

        Keyword Args:
            **column_value (:obj:`kwargs`): The first part in key=val represents the
                column name and the second part represents the column value.

        Returns:
            Returns the number of courses.
        """

        # return the number of courses after executing the query
        return self.__db.count_rows(self.__table, **column_value)
