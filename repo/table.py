class Table:
    def __init__(self, connection, row, column):
        """
        Add, drop, copy, or modify a table.

        Note:
            Use aggregation or composition for using this
            class in another object. The reason is that
            table has a 'has a' relationship with columns and rows.
            Make sure to pass the connection object as its parameter.

        Examples:
            >>> self.tbl = Table('pass connection obj')

        Args:
            connection (:obj:`Connection`): Connect to the file.

        Attributes:
              self.__con (:obj:`Connection`): Connect using composition.
              self.col(:obj:`Column`): Use composition for Column class.
              self.row(:obj:`Row`): Use composition for Row class.
        """

        # use composition for connection
        self.__con = connection

        # Use composition for column and row
        self.col = column
        self.row = row

    def __str__(self):
        """
        String representation of the Table class.

        Note:
            Use this in a print statement to print the
            documentation of the constructor.

        Returns:
            Returns the constructor documentation as string.
        """

        return self.__init__.__doc__

    def add(self, *tables):
        """
        Add a table in the database.

        Note:
            Add one or many tables at once. Make sure to separate
            their names while passing as a parameter.

        Examples:
            >>> self.add('tbl1', 'tbl2', 'tbl3')

        Args:
            *tables (:obj:`list`): Add the given tables.

        Returns: Returns nothing.
        """

        # iterate through **tables and execute the query
        for table in tables:
            # structure of the primary key
            primary_key = f"{table}_id"

            # query for creating table(s)
            query = f'''
                CREATE TABLE IF NOT EXISTS {table} (
                {primary_key} INTEGER PRIMARY KEY AUTOINCREMENT
            )'''

            # execute the query
            self.__con.execute(query)

    def drop(self, *tables):
        """
        Drop a table from the database.

        Note:
            Pass one or many table names as parameters to drop them.

        Examples:
            >>> self.drop('tbl1', 'tbl2', 'tbl3')

        Args:
            *tables (:obj:`list`): Drop one or many tables.

        Returns:
            Returns nothing.
        """

        # iterate through **tables parameter and execute the query
        for table in tables:
            # query for dropping a table
            query = f"DROP TABLE IF EXISTS {table}"

            # execute the query
            self.__con.execute(query)

    def rename(self, old_name, new_name):
        """
        Rename an existing table in the database.

        Note:
            Pass the name of an existing table in the
            first parameter and the new name in the
            second parameter.

        Examples:
            >>> self.rename('old_name', 'new_name')

        Args:
            old_name (str): Rename this table.
            new_name (str): New name for the given table.

        Returns:
            Returns nothing.
        """

        # query for renaming a table
        query = f"ALTER TABLE {old_name} RENAME TO {new_name}"

        # execute the query
        self.__con.execute(query)

    def form(self, table, **columns):
        """
        Create a table with the given column names and data types.

        Note:
            Pass the table name in the first parameter and the column
            names along with their data types in the second parameter.
            If you want to add a foreign key column, do not include
            the column name here. Instead, create the table with normal
            columns and then use 'add_fk()' function from the Column
            class to add a new column with a foreign key constraint.

        Examples:
            >>> self.form('tbl', col1='text', col2='integer')

        Args:
            table (str): Create this table.
            **columns (:obj:`kwargs`): Add these columns to the table.

        Keyword Args:
            **columns (:obj:`kwargs`): Form table using the given
                columns. The first part in key='val' represents column name
                and the next part represents data type.

        Returns:
            Returns nothing.
        """

        # create the table
        self.add(table)

        # add columns to the table
        self.col.add(table, **columns)

    def copy(self, origin_tbl, new_tbl, **columns):
        """
        Copy an existing table into a new one.

        Note:
            Pass the name of the original table in the first
            parameter and the name of the new table in the second
            parameter. Also, pass the name of the columns that you want
            to copy along with their data types in the third parameter.

        Examples:
            >>> self.copy('tbl', 'new_tbl', col1='text', col2='integer')

        Args:
            origin_tbl (str): Copy this table.
            new_tbl (str): Copy the old table in this table.
            **columns (:obj:`kwargs`): Keep these columns.

        Keyword Args:
            **columns (:obj:`kwargs`): Keep the given columns.
                The first part in key='val' represents the column name
                and the next part represents data type.

        Returns:
            Returns nothing.
        """

        # store the column names by joining them using comma
        col = ', '.join(columns.keys())

        # form the table using given columns
        self.form(new_tbl, **columns)

        # query for inserting selected column from one table to another
        query = f'''
            INSERT INTO {new_tbl}({col}) SELECT {col} FROM {origin_tbl}
        '''

        # execute the query
        self.__con.execute(query)

    def fetch(self, table):
        """
        Fetch a table from the database.

        Note:
            Pass the table name as a parameter
        
        Examples:
            >>> print(self.fetch('table_name'))
        
        Args:
            table (str): Fetch data from this table.

        Returns:
            Returns the fetch result after executing the query.
        """

        # query for getting data from a table
        query = f'SELECT * FROM {table}'

        # return the fetch result after executing the query
        return self.__con.fetch(query)
