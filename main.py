import os

import pandas as pd

from constant import CHARACTERS
from constant import EXPORT
from constant import EXPORT_FOLDER
from constant import TableType
from constant import WEBSITE


def make_directory():
    print(EXPORT_FOLDER)
    try:
        os.makedirs(EXPORT_FOLDER)
    except FileExistsError:
        pass


# some other comments
def main():
    for character in CHARACTERS:
        url = WEBSITE.format(character)
        print("Loading: " + url)
        tables = pd.read_html(url)

        for index, table, in enumerate(tables):
            if index == TableType.specials.value:
                table_part = '_specials'
            elif index == TableType.normals.value:
                table_part = '_normals'
            else:
                table_part = '_ERROR'

            export_file_name = EXPORT.format(character + table_part)
            table.to_csv(export_file_name, ',')
            print("Exported: " + export_file_name)
        print()


make_directory()
main()
