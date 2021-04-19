import pathlib
import pandas as pd


class CSVFile:
    __slots__ = ['index', 'file', 'columns']

    def __init__(self, index, file, columns):
        self.index = index
        self.file = file
        self.columns = columns
        self.create_file_if_not_exist()

    def create_file_if_not_exist(self):
        if pathlib.Path(f'{self.file}.csv').exists():
            pass
        else:
            self.save(self.columns_df)

    @property
    def columns_df(self):
        return pd.DataFrame(columns=self.columns).set_index(self.index)

    def read(self):
        return pd.read_csv(f'{self.file}.csv', index_col=self.index, dtype=str)

    def save(self, indexed_df):
        indexed_df.to_csv(f'{self.file}.csv')

    @property
    def index_values(self):
        return self.read().index.values.tolist()

    def insert(self, index, row):
        df = self.read()
        df.loc[f'{index}'] = pd.Series(row, self.columns, name=f'{row}')
        self.save(df)

    def drop(self, index):
        try:
            self.save(self.read().drop(index))
        except KeyError:
            pass

    def update(self, index, row, old_index):
        self.drop(old_index)
        self.insert(index, row)

    def get(self, index, column):
        return self.read().loc[index][column]
