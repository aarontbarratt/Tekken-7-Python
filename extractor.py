# extractor class


class Extractor:
    def __init__(self):
        self.tables = []
        self.url = ''
        self.export_location = r'C:\temp'

    def get_tables(self, url):
        import pandas as pd

        self.url = url

        # read the url for all tables
        self.tables = pd.read_html(self.url)

        return self.tables

    def read_tables(self):
        for table in self.tables:
            print(table)

    def read_table(self, index):
        return self.tables[index]

    def export(self, table):
        import pandas as pd
        _table = table
        df = pd.DataFrame(_table, columns=['0', '1'])
        export_csv = df.to_csv(self.export_location + r'\something.csv', index=None, header=True)

        print(df)