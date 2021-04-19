from repo.csv_file import CSVFile


class Student:
    __slots__ = [
        '__user_id',
        'file',
        '__name',
        '__lastname',
        '__email',
        '__username',
        '__password',
        '__advisor',
        '__advisor_email'
    ]

    def __init__(self, user_id):
        self.__user_id = user_id

        self.file = CSVFile(index=self.columns[0], file='student', columns=self.columns)

        self.__name = str(
            self.file.get(self.user_id, 'name')
        )

        self.__lastname = str(
            self.file.get(self.user_id, 'lastname')
        )

        self.__email = str(
            self.file.get(self.user_id, 'email')
        )

        self.__username = str(
            self.file.get(self.user_id, 'username')
        )

        self.__password = str(
            self.file.get(self.user_id, 'password')
        )

        self.__advisor = str(
            self.file.get(self.user_id, 'advisor')
        )

        self.__advisor_email = str(
            self.file.get(self.user_id, 'advisor_email')
        )

    @property
    def columns(self):
        return [
            'id',
            'name',
            'lastname',
            'email',
            'username',
            'password',
            'advisor',
            'advisor_email'
        ]

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def advisor(self):
        return self.__advisor

    @advisor.setter
    def advisor(self, advisor):
        self.__advisor = advisor

    @property
    def advisor_email(self):
        return self.__advisor_email

    @advisor_email.setter
    def advisor_email(self, advisor_email):
        self.__advisor_email = advisor_email

    def save(self):
        self.file.update(
            self.user_id,
            [
                self.user_id,
                self.name,
                self.lastname,
                self.email,
                self.username,
                self.password,
                self.advisor,
                self.advisor_email
            ],
            self.user_id
        )
