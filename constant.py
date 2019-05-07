# consts

from enum import Enum
from sys import platform


class TableType(Enum):
    normals = 1
    specials = 0


CHARACTERS = ['akuma', 'alisa', 'armor-king', 'asuka', 'bob', 'bryan', 'claudio', 'devil-jin', 'dragunov', 'eddy',
              'eliza', 'feng', 'geese', 'gigas', 'heihachi', 'hwoarang', 'jack7', 'jin', 'josie', 'julia', 'katarina',
              'kazumi', 'kazuya', 'king', 'kuma', 'lars', 'lei', 'law', 'lee', 'leo', 'lili', 'lucky-chloe', 'marduk',
              'master-raven', 'miguel', 'negan', 'nina', 'noctis', 'paul', 'shaheen', 'steve', 'xiaoyu', 'yoshimitsu']

WEBSITE = r'http://rbnorway.org/{}-t7-frames/'

# if mac then create mac file path
if platform == 'darwin':
    EXPORT_FOLDER = '/Users/aaronb/Desktop/FrameData'
    EXPORT = EXPORT_FOLDER + r'/{}.csv'
# if anything else then try create windows path
else:
    EXPORT_FOLDER = r'C:\FrameData'
    EXPORT = EXPORT_FOLDER + r'\{}.csv'
