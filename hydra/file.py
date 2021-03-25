import os


class File:
    def __init__(self, name=None, location=None):
        """
        Create and store information about name and location of file.

        Note:
            Do not pass the file name and location as parameters if
            you want to create a 'main.db' file in your directory.

        Examples:
            >>> file = File('name', 'directory')

        Args:
            name (str, optional): Get file name.
            location (str, optional): Get file location.

        Attributes:
            self.name (str): Store file name and if none is given,
                set it as 'main'. Also, it cannot be accessed from outside.

            self.location (str): Store file directory and if none is given,
                set to the current directory. Also, cannot be accessed from
                the outside of the class.

            self.__full_directory (str): Merge file location and name to create
                a full directory address of the SQLite file.
        """

        # store the name of the file, default to 'main'
        self.__name = name or 'main'

        # store the location of the file, default to current directory
        self.__location = location or self.current_directory()

        # store full directory address of the file
        self.__full_directory = f"{self.__location}/{self.__name}.db"

    def __str__(self):
        """
        String representation of the File class.

        Note:
            Use the class directly in a print statement or aggregate
            to get the full directory of the file as a string.

        Returns:
            Returns the full directory as a string.
        """

        return self.__full_directory

    @staticmethod
    def current_directory():
        """
        Get current project directory.

        Note:
            For windows users, it will change '\' to '/' automatically
            because python refers to directories using forward slash.

        Returns:
            :return: Returns the current working directory.
        """

        return str(os.getcwd().replace('\\', '/'))
