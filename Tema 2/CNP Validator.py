import random as rd
from datetime import date


class Human:
    def __init__(self, cnp: str):
        self.region = regions.get(cnp[7] + cnp[8])
        self.day = int(cnp[5] + cnp[6])
        self.year = build_year(int(cnp[0]), int(cnp[1] + cnp[2]))
        self.cnp = cnp
        self.month = months.get(cnp[3] + cnp[4])[0]

    def show(self):
        print("""
            CNP = {}
            Region = {}
            Year::Month::Day = {}::{}::{}
            """.format(self.cnp, self.region, self.year, self.month, self.day))


def build_year(s: int, year_last_digits: int) -> int:
    """
    :param s: Sex and century of birth for a human
    :param year_last_digits: last two digits of the year of birth for a human
    :return: the year of birth
    """
    if s >= 7 or s <= 2:
        return 1900 + year_last_digits
    elif s == 3 or s == 4:
        return 1800 + year_last_digits
    return 2000 + year_last_digits


def validation(cnp: str) -> str:
    """
    :param cnp: the cnp of a person
    :return: the validity of the CNP or why it's wrong
    """

    if len(cnp) != 13:
        return "CNP not the right length"
    if len([i for i in cnp if 48 <= ord(i) <= 57]) == 0:
        return "Weird characters are present"

    if cnp[0] == '0':
        return 'Bad first character'

    # Year validation
    year = build_year(s=int(cnp[0]), year_last_digits=int(cnp[1] + cnp[2]))

    if year > date.today().year:
        return "Time traveler alert!"

    # Day validation
    if months.get(cnp[3] + cnp[4]) is None:
        return "Month is invalid"

    if int(cnp[5] + cnp[6]) > 31:
        return "Day error"

    if months.get(cnp[3] + cnp[4])[0] == 'February' and year % 4 == 0:
        if int(cnp[5] + cnp[6]) > 29:
            return 'Day error February style'

    if regions.get(cnp[7] + cnp[8]) is None:
        return 'Region not found'

    control_calculation = sum([(ord(i) - 48) * (ord(j) - 48) for i, j in zip(list(cnp[:-1]), control_string)]) % 11

    if control_calculation == 10:
        control_calculation = 1

    if control_calculation != int(cnp[12]):
        return "Wrong value for control character"

    return "Good CNP"


def create_cnp() -> str:
    """
    :return: a cnp made of random characters
    """
    return "".join([chr(rd.randrange(48, 58)) for _ in range(13)])


def stress_test(number: int) -> [str]:
    """
    :param number: Number of random dnp to create and verify
    :return: a list of good cnp
    """
    good_cnps = (Human(_) for _ in (create_cnp() for _ in range(number)) if validation(cnp=_) == "Good CNP")
    return good_cnps


if __name__ == "__main__":
    control_string = '279146358279'
    months = {'01': ['January', 31], '02': ['February', 28], "03": ['March', 31], '04': ['April', 30],
              '05': ['May', 31],
              '07': ['July', 31], '08': ['August', 30], '09': ['September', 31], '10': ['October', 30],
              '06': ['June', 30], '11': ['November', 31], '12': ['December', 30]}
    regions = {'01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita-Nasaud',
               '07': 'Botosani', '08': 'Brasov',
               '09': 'Braila', '10': 'Buzau', '11': 'Caras-Severin', '12': 'Cluj', '13': 'Constanta', '14': 'Covasna',
               '16': 'Dolj', '17': 'Galati', '18': 'Gorj', '19': 'Harghita', '20': 'Hunedoara', '21': 'Ialomita',
               '22': 'Iasi', '15': 'Dambovita', '29': 'Prahova', '36': 'Tulcea', '42': 'Bucuresti S.2',
               '23': 'Ilfov', '24': 'Maramures', '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt',
               '30': 'Satu Mare', '31': 'Salaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis',
               '37': 'Vaslui', '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti S.1',
               '43': 'Bucuresti S.3', '44': 'Bucuresti S.4', '45': 'Bucuresti S.5', '46': 'Bucuresti S.6',
               '51': 'Calarasi', '52': 'Giurgiu'}

    for x in stress_test(number=int(input("number of cnps to test\n"))):
        x.show()
    # CNP_to_Test = input("Introduce a CNP\n")
    # print(validation(CNP_to_Test))
    # Human(CNP_to_Test).show()
