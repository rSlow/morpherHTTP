from enum import Enum

from pytrovich.enums import Case as PytrovichCase
from pytrovich.enums import NamePart as PytrovichNamePart

HTTPCase = {
    1: "nomn",
    2: "gent",
    3: "datv",
    4: "accs",
    5: "ablt",
    6: "loct",
}


class CommonCase(Enum):
    nomn = HTTPCase[1]
    gent = HTTPCase[2]
    datv = HTTPCase[3]
    accs = HTTPCase[4]
    ablt = HTTPCase[5]
    loct = HTTPCase[6]


class PytrovichAliasCase(Enum):
    gent = PytrovichCase.GENITIVE
    datv = PytrovichCase.DATIVE
    accs = PytrovichCase.ACCUSATIVE
    ablt = PytrovichCase.INSTRUMENTAL
    loct = PytrovichCase.PREPOSITIONAL


class NamePartAlias(Enum):
    f = PytrovichNamePart.LASTNAME
    i = PytrovichNamePart.FIRSTNAME
    o = PytrovichNamePart.MIDDLENAME
