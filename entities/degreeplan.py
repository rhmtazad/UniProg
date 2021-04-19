from repo.csv_file import CSVFile


class DegreePlan:
    __slots__ = [
        '__major',
        'file',
        '__year',
        '__conc',
        '__credits',
        '__courses',
        '__gen_credits',
        '__core_credits',
        '__conc_credits'
    ]

    def __init__(self, major):
        self.__major = major

        self.file = CSVFile(index=self.columns[0], file='degreeplan', columns=self.columns)

        self.__year = str(
            self.file.get(self.major, 'year')
        )

        self.__conc = str(
            self.file.get(self.major, 'conc')
        )

        self.__credits = str(
            self.file.get(self.major, 'credits')
        )

        self.__courses = str(
            self.file.get(self.major, 'courses')
        )

        self.__gen_credits = str(
            self.file.get(self.major, 'gen_credits')
        )

        self.__core_credits = str(
            self.file.get(self.major, 'core_credits')
        )

        self.__conc_credits = str(
            self.file.get(self.major, 'conc_credits')
        )

    @property
    def columns(self):
        return [
            'major',
            'year',
            'conc',
            'credits',
            'courses',
            'gen_credits',
            'core_credits',
            'conc_credits'
        ]

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, major):
        self.__major = major

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def conc(self):
        return self.__conc

    @conc.setter
    def conc(self, concentration):
        self.__conc = concentration

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credit):
        self.__credits = credit

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    @property
    def gen_credits(self):
        return self.__gen_credits

    @gen_credits.setter
    def gen_credits(self, credit):
        self.__gen_credits = credit

    @property
    def core_credits(self):
        return self.__core_credits

    @core_credits.setter
    def core_credits(self, credit):
        self.__core_credits = credit

    @property
    def conc_credits(self):
        return self.__conc_credits

    @conc_credits.setter
    def conc_credits(self, credit):
        self.__conc_credits = credit

    @property
    def gen_courses(self):
        return self.calc_courses(self.gen_credits)

    @property
    def core_courses(self):
        return self.calc_courses(self.core_credits)

    @property
    def conc_courses(self):
        return self.calc_courses(self.conc_credits)

    def save(self):
        self.file.update(
            self.major,
            [
                self.major,
                self.year,
                self.conc,
                self.credits,
                self.courses,
                self.gen_credits,
                self.core_credits,
                self.conc_credits
            ],
            self.major
        )

    @staticmethod
    def calc_courses(credit):
        return int(int(credit) / 3)
