class Column:
    def __init__(self, connection):
        """
        Add, drop, modify, or retrieve a column.

        Note:
            Aggregate or use composition while using this
            class in another object. Also, make sure to
            pass the connection object as a parameter.

        Examples:
            >>> self.col = Column('pass the connection obj')

        Args:
            connection (:obj:`Connection`): Connect to the database.

        Attributes:
            self.__con (:obj:`Connection`): Use composition for connection.
        """

        self.__con = connection

    def __str__(self):
        """
        String representation of the Column class.

        Note:
            Use this in a print statement to print the
            documentation of the constructor.

        Returns:
            Returns the constructor documentation as string.
        """

        return self.__init__.__doc__

    def add(self, table, **columns):
        """
        Add a column in a table.

        Note:
            Pass the table name in the first parameter
            and pass the columns and data types in the
            second parameter. Also, pass as many columns
            as you want.

        Examples:
            >>> self.add('tbl', col1='text', col2='integer')

        Args:
            table (str): Add columns to this table.
            **columns (:obj:`kwargs`): Add columns with data types.

        Keyword Args:
            **columns (:obj:`kwargs`): Create the given columns.
                The first part in key='val' represents the column name
                and the next part represents the data type.

        Returns:
            Returns nothing.
        """

        # iterate through **columns and execute the query
        for column, data_type in columns.items():
            # skip the already existing columns
            if column not in self.fetch_names(table):
                # query for adding column(s) in a table
                query = f'''
                    ALTER TABLE {table}
                    ADD COLUMN {column} {data_type}
                '''

                # execute the query
                self.__con.execute(query)

    def add_fk(self, table, column, reference_tbl, reference_col):
        """
        Add a column and set it as a foreign key.

        Note:
            This can only set a new column as a foreign key.
            To avoid problems, first, create other columns
            and then add a foreign key column using this function.

        Examples:
            >>> self.add_fk('tbl', 'fk_col', 'ref_tbl', 'ref_col')

        Args:
            table (str): Add a foreign key column to this table.
            column (str): Add this new column as a foreign key.
            reference_tbl (str): Refer the foreign key in this table.
            reference_col (str): Refer the foreign key in this column.

        Returns:
            Returns nothing.
        """

        # query for adding a foreign key column
        query = f'''
            ALTER TABLE {table}
            ADD COLUMN {column} INTEGER
            REFERENCES {reference_tbl}({reference_col})
        '''

        # execute the query
        self.__con.execute(query)

    def rename(self, table, current_name, new_name):
        """
        Rename a column in a table.

        Note:
            This function only works on non-primary-key
            columns because SQLite currently does not support
            renaming a primary key.

        Examples:
            >>> self.rename('tbl', 'col_name', 'new_col')

        Args:
            table (str): Rename a column from this table.
            current_name (str): Rename this column.
            new_name (str): New name for the column.

        Returns:
            Returns nothing.
        """

        # query for renaming a column
        query = f'''
            ALTER TABLE {table}
            RENAME COLUMN {current_name}
            TO {new_name}
        '''

        # execute the query
        self.__con.execute(query)

    def fetch(self, table, *columns):
        """
        Fetch column(s) from a table.

        Note:
            Pass the table name in the first parameter
            and the column name(s) in the next parameters.

        Examples:
            >>> print(self.fetch('tbl', 'col1', 'col2'))

        Args:
            table (str): Fetch column(s) from this table.
            *columns (:obj:`list`): Fetch these columns from a table.

        Returns:
            Returns the fetch result after executing the query.
        """

        # store column names to be fetched
        columns = ', '.join(columns)

        # query for fetching one or more columns
        query = f'SELECT {columns} FROM {table}'

        # return the fetch result after executing the query.
        return self.__con.fetch(query)

    def fetch_names(self, table):
        """
        Fetch column names from a table.

        Note:
            Pass the table name as a parameter to get the
            list of columns that exists within a table.

        Examples:
            >>> print(self.fetch_names('tbl1'))

        Args:
            table (str): Fetch column names from this table.

        Returns:
            Returns the columns names after executing the query.
        """

        # query for getting the column names
        query = f'''
            PRAGMA table_info({table})
        '''

        # return the column names after executing the query
        return [column['name'] for column in self.__con.fetch(query)]

    def filter(self, table, **col_val):
        """
        Fetch and filter columns with the given values.

        Note:
            Pass the table name in the first parameter and the
            columns along with their values in the other parameters.
            The function return the rows based on the columns
            that have the given values.

        Examples:
            >>> print(self.filter('tbl', col1='val1', col2='val2'))

        Args:
            table (str): Fetch from this table.
            **col_val (:obj:`kwargs`): Fetch based on columns and values


        Keyword Args:
            **col_val (:obj:`kwargs`): The first part in key=val represents
                the column name and the second part represents the value for
                that column.

        Returns:
            Returns the rows and columns after executing the query.
        """

        # store column in (val) conditions for query
        # join the columns along with their values and
        # remove the last extra 'AND' word by using .rsplit(' ', 2)[0]
        col_in_val = str(
            "".join(f"{col} IN ('{val}') AND " for (col, val) in col_val.items())
        ).rsplit(' ', 2)[0]

        # query for fetching rows based on column's value
        query = f'SELECT * FROM {table} WHERE {col_in_val}'

        # execute the query and return the result
        return self.__con.fetch(query)
