class Row:
    def __init__(self, connection):
        """
        Insert, delete, modify, or retrieve a row.

        Note:
            Aggregate or use composition while using
            this class in another object. Also, make sure to
            pass the connection object as a parameter.

        Examples:
            >>> self.row = Row('pass connection obj')

        Args:
            connection (:obj:`Connection`): Connect to the database.

        Attributes:
            self.__con (:obj:`Connection`): Use composition for connection.
        """

        self.__con = connection

    def __str__(self):
        """
        String representation of the Row class.

        Note:
            Use this in a print statement to print the
            documentation of the constructor.

        Returns:
            Returns the constructor documentation as string.
        """

        return self.__init__.__doc__

    def insert(self, table, **data):
        """
        Insert data in a table.

        Notes:
            Pass the table name in the first parameter and
            pass a **kwargs type in the second parameter.

        Examples:
            >>> self.insert('tbl', col1='text', col2='integer')

        Args:
            table (str): Insert given data in this table.
            **data (:obj:`kwargs`): Insert this data in the given table.

        Keyword Args:
            **data (:obj:`kwargs`): Add the given data.
                The first part in key='val' represents the column
                name and the next part represents data type.

        Returns:
            Returns nothing.
        """

        # get column names join them using comma
        columns = ', '.join(data.keys())

        # get the values for columns as string
        values = str(list(data.values()))[1:-1]

        # query for inserting data in a table
        query = f'''
           INSERT INTO {table} ({columns})
           VALUES ({values})
        '''

        # execute the query
        self.__con.execute(query)

    def delete(self, table, row_id):
        """
        Delete a row from a table.

        Note:
            Pass the table name in the first parameter and
            the primary key in the second parameter.

        Examples:
            >>> self.delete('tbl', 1)

        Args:
            table (str): Delete row from this table.
            row_id (int): Delete row with this primary key.

        Returns:
            Returns nothing.
        """

        # structure of the primary key
        primary_key = f"{table}_id"

        # query for deleting a row from a table
        query = f'''
           DELETE FROM {table}
           WHERE {primary_key} = {row_id}
        '''

        # execute the query
        self.__con.execute(query)

    def update(self, table, row_id, **data):
        """
        Update a row in a table.

        Note:
            Pass the table name in the first parameter and
            pass the primary key in the second one. Also,
            the datatype for the third parameter is '**kwargs'.
            The first pair in the third parameter represents
            the column name and the second pair represents the
            value for that column.

        Examples:
            >>> self.update('tbl', 1, name='R', age='25')

        Args:
            table (str): Update a row from this table.
            row_id (int): Update a row with this id.
            **data (:obj:`kwargs`): Update a row with this data.

        Keyword Args:
            **data (:obj:`kwargs`): Update with the given data.
                First part in key='val' represents the column name
                and the next part represents data.

        Returns:
            Returns nothing.
        """

        # store columns and their values
        columns_values = "".join(
            f"{col}='{val}'," for (col, val) in data.items()
        )[0:-1]

        # structure for primary key
        primary_key = f"{table}_id"

        # query for updating row(s) in a table
        query = f'''
            UPDATE {table}
            SET {columns_values}
            WHERE {primary_key} = {row_id}
        '''

        # execute the query
        self.__con.execute(query)

    def filter(self, table, row_id, *columns):
        """
        Fetch specific cells within a row

        Note:
            Pass the table name in the first parameter,
            and the primary key in the second parameter.
            Pass one or more column names in the third
            parameter.

        Examples:
            >>> print(self.filter('tbl', 1, 'col1', 'col2'))

        Args:
            table (str): Fetch cells from this table.
            row_id (int): Fetch cells with this primary key.
            *columns (str): Fetch cells from these columns.

        Returns:
            Returns the fetch result after executing the query.
        """

        # store column names to be fetched
        columns = ', '.join(columns)

        # structure for the primary key
        primary_key = f'{table}_id'

        # query for fetching one or more cells from a table
        query = f'''
            SELECT {columns}
            FROM {table}
            WHERE {primary_key} = {row_id}
        '''

        # return the fetch result after executing the query
        return self.__con.fetch(query)[0]

    def fetch(self, table, row_id):
        """
        Fetch a row from a table.

        Note:
            Pass the table name in the first parameter,
            and the primary key in the second parameter.

        Examples:
            >>> print(self.fetch('tbl', 1, 'col1', 'col2'))

        Args:
            table (str): Fetch cells from this table.
            row_id (int): Fetch cells with this primary key.

        Returns:
            Returns the fetch result after executing the query.
        """

        # structure for the primary key
        primary_key = f'{table}_id'

        # query for fetching a row from a table
        query = f'''
            SELECT *
            FROM {table}
            WHERE {primary_key} = {row_id}
        '''

        # return the fetch result after executing the query
        return self.__con.fetch(query)[0]

    def cell(self, table, row_id, column):
        """
        Fetch a specific cell within a row from a table.

        Note:
            Pass the table name in the first parameter and the
            row_id in the second parameter. Also, pass the column
            name for the desired cell in the third parameter.

        Examples:
            >>> self.cell(table='tbl', row_id=1, column='col')

        Args:
            table (str): Fetch a cell from this table.
            row_id (int): Fetch a cell from this row.
            column (str): Fetch a cell from this column.

        Returns:
            Returns a cell from a table.
        """
        return self.filter(table, row_id, column)[column]

    def count(self, table, **col_val):
        """
        Count number of rows for columns with the given values.

        Note:
            Pass the table name in the first parameter and the
            columns along with their values in the other parameters.
            The function counts the number of rows based on the columns
            that have the given values.

        Examples:
            >>> print(self.count('tbl', col1='val1', col2='val2'))

        Args:
            table (str): Count rows from this table.
            **col_val (:obj:`kwargs`): Count rows based on columns and values


        Keyword Args:
            **col_val (:obj:`kwargs`): The first part in key=val represents
                the column name and the second part represents the value for
                that column.

        Returns:
            Returns the number of rows after executing the query.
        """

        # store column in (val) conditions for query
        # join the columns along with their values and
        # remove the last extra 'AND' word by using .rsplit(' ', 2)[0]
        col_in_val = str(
            "".join(f"{col} IN ('{val}') AND " for (col, val) in col_val.items())
        ).rsplit(' ', 2)[0]

        # query for counting number of rows based on a column's value
        query = f'SELECT COUNT(*) FROM {table} WHERE {col_in_val}'

        # return the number of rows after executing the query
        return self.__con.fetch(query)[0]['COUNT(*)']
