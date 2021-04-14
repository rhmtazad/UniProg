class Database:
    def __init__(self, connection, table):
        """
        Create a database with a given name and location.

        Note:
            the proper way to use this API is to create
            an instance of the Schema object. However, if you
            want to make an instance of this class, pass the name
            and location. If you want to create the database in your
            working directory, you can leave the second parameter empty.
            Also, if the name is left empty, the database will be
            created with 'main' name.

        Examples:
            >>> self.__db = Database('name', 'directory...')
            >>> self.__db = Database() # or empty parameters

        Args:
            connection (:obj:`Connection`): Create the database using this
                connection.

        Attributes:
            self.__con (:obj:`Connection`): Use composition for Connection.
            self.__tbl (:obj:`Table`): Use composition for the Table class.
        """

        # use composition for Connection class
        self.con = connection

        # use composition for Table class
        self.tbl = table

    def __str__(self):
        """
        String representation of the Database class.

        Note:
            Use this in a print statement to print the
            documentation of the constructor.

        Returns:
            Returns the constructor documentation as string.
        """

        return self.__init__.__doc__

    def drop_col(self, tbl, **columns):
        """
        Drop a column from the database.

        Note:
            Pass the table name in the first parameter and
            name of the columns that you want to keep, along with
            their data types, in the second parameter. SQLite does not
            support dropping a column. To make this work, a temporary
            copy of the table with the desired columns will be created.
            After copying the data, the temporary table will be deleted.

        Examples:
            >>> self.drop_col('tbl', name='text', age='integer')

        Args:
            tbl (str): Drop a column from this table.
            **columns (:obj:`kwargs`): Keep these columns and
                drop the ones that are not mentioned.

        Keyword Args:
            **columns (:obj:`kwargs`): Keep the given columns.
                The first part in key='val' represents the column name
                and the next part represents data type.

        Returns:
            Returns nothing.
        """

        # name of the temporary table
        temp = "temp"

        # copy the old table in the temp table
        self.tbl.copy(tbl, temp, **columns)

        # drop the old table
        self.tbl.drop(tbl)

        # copy the temp table in a new table
        # the new table has the same name as the old one
        self.tbl.copy(temp, tbl, **columns)

        # drop the temp table
        self.tbl.drop(temp)
