from .column import Column
from .connection import Connection
from .database import Database
from .row import Row
from .table import Table


class Schema:
    def __init__(self, name=None, location=None):
        """
        Create a schema and provide easy access to operations.

        Note:
            Pass the file name in the first parameter and the
            file location in the second parameter. If name or location
            is not provided, it will apply the default values. This object
            is another layer of abstraction that uses the facade pattern to
            provide an easy access to the operations of each object.

        Examples:
            >>> schema = Schema('name', 'location') # with parameters
            >>> db = Schema() # empty parameter
            >>> db.add_table('tbl1', 'tbl2') # access to operations

        Args:
            name (str, optional): Create the database with this name.
                Defaults to 'main'.
            location (str, optional): Create the database in this location.
                Defaults to the current working directory.

        Attributes:
            self.__con(:obj:`Connection`): Aggregate Connection object.
            self.__db(:obj:`Database`): Aggregate Database object.
            self.__tbl(:obj:`Table`): Aggregate Table object.
            self.__col(:obj:`Column`): Aggregate Column object.
            self.__row(:obj:`Row`): Aggregate Row object.
        """

        # aggregate the Connection object
        self.__con = Connection(name, location)

        # aggregate the Row object
        self.__row = Row(self.__con)

        # aggregate the Column object
        self.__col = Column(self.__con)

        # aggregate the Table object
        self.__tbl = Table(self.__con, self.__row, self.__col)

        # aggregate the database object
        self.__db = Database(self.__con, self.__tbl)

    def execute(self, query):
        """
        Connect to the '.db' file and execute a query.

        Note:
            Pass the query to execute it. If parameters are empty,
            it will only connect to the file.

        Examples:
            >>> self.execute("")
            >>> self.execute('create table tbl_name')

        Args:
            query (str): Execute the given query.

        Returns:
            Returns nothing.
        """

        self.__con.execute(query)

    def fetch(self, query):
        """
        Execute a query and return the fetch result.

        Note:
            Use this function if you want the return
            value. Otherwise, use the execute() function.

        Examples:
            >>> print(self.fetch('select * from tbl'))

        Args:
            query (str): Fetch this query and return the result.

        Returns:
            Returns the fetch result after executing a query
        """

        return self.__con.fetch(query)

    def add_table(self, *tables):
        """
        Add a table in the database.

        Note:
            Add one or many tables at once. Make sure to separate
            their names while passing as a parameter.

        Examples:
            >>> self.add_table('tbl1', 'tbl2', 'tbl3')

        Args:
            *tables (:obj:`list`): Add the given tables.

        Returns: Returns nothing.
        """

        self.__tbl.add(*tables)

    def drop_table(self, *tables):
        """
        Drop a table from the database.

        Note:
            Pass one or many table names as parameters to drop them.

        Examples:
            >>> self.drop_table('tbl1', 'tbl2', 'tbl3')

        Args:
            *tables (:obj:`list`): Drop one or many tables.

        Returns:
            Returns nothing.
        """

        self.__tbl.drop(*tables)

    def rename_table(self, old_name, new_name):
        """
        Rename an existing table in the database.

        Note:
            Pass the name of an existing table in the
            first parameter and the new name in the
            second parameter.

        Examples:
            >>> self.rename_table('old_name', 'new_name')

        Args:
            old_name (str): Rename this table.
            new_name (str): New name for the given table.

        Returns:
            Returns nothing.
        """

        self.__tbl.rename(old_name, new_name)

    def form_table(self, table, **columns):
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
            >>> self.form_table('tbl', col1='text', col2='integer')

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

        self.__tbl.form(table, **columns)

    def copy_table(self, origin_tbl, new_tbl, **columns):
        """
        Copy an existing table into a new one.

        Note:
            Pass the name of the original table in the first
            parameter and the name of the new table in the second
            parameter. Also, pass the name of the columns that you want
            to copy along with their data types in the third parameter.

        Examples:
            >>> self.copy_table('tbl', 'new_tbl', col1='text', col2='integer')

        Args:
            origin_tbl (str): Copy this table.
            new_tbl (str): Copy the old table in this table.
            **columns (:obj:`kwargs`):

        Keyword Args:
            **columns (:obj:`kwargs`): Keep the given columns.
                The first part in key='val' represents the column name
                and the next part represents data type.

        Returns:
            Returns nothing.
        """

        self.__tbl.copy(origin_tbl, new_tbl, **columns)

    def fetch_table(self, table):
        """
        Fetch a table from the database.

        Note:
            Pass the table name as a parameter.

        Examples:
            >>> print(self.fetch_table('table_name'))

        Args:
            table (str): Fetch data from this table.

        Returns:
            Returns the fetch result after executing the query.
        """

        return self.__tbl.fetch(table)

    def add_column(self, table, **columns):
        """
        Add a column in a table.

        Note:
            Pass the table name in the first parameter
            and pass the columns and data types in the
            second parameter. Also, pass as many columns
            as you want.

        Examples:
            >>> self.add_column('tbl', col1='text', col2='integer')

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

        self.__col.add(table, **columns)

    def drop_column(self, table, **columns):
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
            >>> self.drop_column('tbl', name='text', age='integer')

        Args:
            table (str): Drop a column from this table.
            **columns (:obj:`kwargs`): Keep these columns and
                drop the ones that are not mentioned.

        Keyword Args:
            **columns (:obj:`kwargs`): Keep the given columns.
                The first part in key='val' represents the column name
                and the next part represents data type.

        Returns:
            Returns nothing.
        """

        self.__db.drop_col(table, **columns)

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

        self.__col.add_fk(table, column, reference_tbl, reference_col)

    def rename_column(self, tbl, current_name, new_name):
        """
        Rename a column in a table.

        Note:
            This function only works on non-primary-key
            columns because SQLite currently does not support
            renaming a primary key.

        Examples:
            >>> self.rename_column('tbl', 'col_name', 'new_col')

        Args:
            tbl (str): Rename a column from this table.
            current_name (str): Rename this column.
            new_name (str): New name for the column.

        Returns:
            Returns nothing.
        """

        self.__col.rename(tbl, current_name, new_name)

    def fetch_columns(self, table, *columns):
        """
        Fetch column(s) from a table.

        Note:
            Pass the table name in the first parameter
            and the column name(s) in the next parameters.

        Examples:
            >>> print(self.fetch_columns('tbl', 'col1', 'col2'))

        Args:
            table (str): Fetch column(s) from this table.
            *columns (:obj:`list`): Fetch these columns from a table.

        Returns:
            Returns the fetch result after executing the query.
        """

        return self.__col.fetch(table, *columns)

    def fetch_column_names(self, table):
        """
        Fetch column names from a table.

        Note:
            Pass the table name as a parameter to get the
            list of columns that exists within a table.

        Examples:
            >>> print(self.fetch_column_names('tbl1'))

        Args:
            table (str): Fetch column names from this table.

        Returns:
            Returns the columns names after executing the query.
        """

        return self.__col.fetch_names(table)

    def filter_column(self, table, **col_val):
        """
        Fetch and filter columns with the given values.

        Note:
            Pass the table name in the first parameter and the
            columns along with their values in the other parameters.
            The function return the rows based on the columns
            that have the given values.

        Examples:
            >>> print(self.filter_column('tbl', col1='val1', col2='val2'))

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

        return self.__col.filter(table, **col_val)

    def insert_row(self, table, **data):
        """
        Insert data in a table.

        Notes:
            Pass the table name in the first parameter and
            pass a **kwargs type in the second parameter.

        Examples:
            >>> self.insert_row('tbl', col1='text', col2='integer')

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

        self.__row.insert(table, **data)

    def delete_row(self, table, row_id):
        """
        Delete a row from a table.

        Note:
            Pass the table name in the first parameter and
            the primary key in the second parameter.

        Examples:
            >>> self.delete_row('tbl', 1)

        Args:
            table (str): Delete row from this table.
            row_id (int): Delete row with this primary key.

        Returns:
            Returns nothing.
        """

        self.__row.delete(table, row_id)

    def update_row(self, table, row_id, **data):
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
            >>> self.update_row('tbl', 1, name='R', age='25')

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

        self.__row.update(table, row_id, **data)

    def filter_row(self, table, row_id, *columns):
        """
        Fetch specific cells within a row

        Note:
            Pass the table name in the first parameter,
            and the primary key in the second parameter.
            Pass one or more column names in the third
            parameter.

        Examples:
            >>> print(self.filter_row('tbl', 1, 'col1', 'col2'))

        Args:
            table (str): Fetch cells from this table.
            row_id (int): Fetch cells with this primary key.
            *columns (str): Fetch cells from these columns.

        Returns:
            Returns the fetch result after executing the query.
        """

        # return the fetch result after executing the query
        return self.__row.filter(table, row_id, *columns)

    def count_rows(self, table, **col_val):
        """
        Count number of rows for columns with the given values.

        Note:
            Pass the table name in the first parameter and the
            columns along with their values in the other parameters.
            The function counts the number of rows based on the columns
            that have the given values.

        Examples:
            >>> print(self.count_rows('tbl', col1='val1', col2='val2'))

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

        # return the number of rows after executing the query
        return self.__row.count(table, **col_val)

    def fetch_cell(self, table, row_id, column):
        """
        Fetch a specific cell within a row from a table.

        Note:
            Pass the table name in the first parameter and the
            row_id in the second parameter. Also, pass the column
            name for the desired cell in the third parameter.

        Examples:
            >>> self.fetch_cell(table='tbl', row_id=1, column='col')

        Args:
            table (str): Fetch a cell from this table.
            row_id (int): Fetch a cell from this row.
            column (str): Fetch a cell from this column.

        Returns:
            Returns a cell from a table.
        """
        return self.__row.cell(table, row_id, column)

    def fetch_row(self, table, row_id):
        """
        Fetch a row from a table.

        Note:
            Pass the table name in the first parameter,
            and the primary key in the second parameter.

        Examples:
            >>> print(self.fetch_row('tbl', 1, 'col1', 'col2'))

        Args:
            table (str): Fetch cells from this table.
            row_id (int): Fetch cells with this primary key.

        Returns:
            Returns the fetch result after executing the query.
        """

        return self.__row.fetch(table, row_id)
