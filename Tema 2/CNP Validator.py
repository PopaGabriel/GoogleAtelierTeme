from datetime import date
from random import randrange


class Human:
    def __init__(self, cnp: str):
        self.region = regions.get(int(cnp[7] + cnp[8]))
        self.day = int(cnp[5] + cnp[6])
        self.year = build_year(int(cnp[0]), int(cnp[1] + cnp[2]))
        self.cnp = cnp
        self.month = months.get(int(cnp[3] + cnp[4]))[0]

    def show(self):
        print("""
            CNP = {}
            Region = {}
            Year::Month::Day = {}::{}::{}
            """.format(self.cnp, self.region, self.year, self.month, self.day))


def stress_test() -> [str]:
    return ["".join([chr(randrange(48, 58)) for _ in range(13)]) for _ in range(1000000)]


def build_year(s: int, year_last_digits: int) -> int:
    if s >= 7 or s <= 2:
        return 1900 + year_last_digits
    elif s == 3 or s == 4:
        return 1800 + year_last_digits
    else:
        return 2000 + year_last_digits


def validation(cnp: str) -> str:
    if len(cnp) != 13:
        return "CNP not the right length"

    if len([i for i in cnp if 48 <= ord(i) <= 57]) == 0:
        return "Weird characters are present"

    if cnp[0] == '0':
        return 'Bad first character'

    # Year validation
    year = build_year(int(cnp[0]), int(cnp[1] + cnp[2]))

    if year > date.today().year:
        return "Time traveler alert!"

    # Day validation
    if months.get(int(cnp[3] + cnp[4])) is None:
        return "Month is invalid"

    if int(cnp[5] + cnp[6]) > 31:
        return "Day error"

    if months.get(int(cnp[3] + cnp[4]))[0] == 'February':
        if year % 4 == 0:
            if int(cnp[5] + cnp[6]) > 29:
                return 'Day error February style'

    if regions.get(int(cnp[7] + cnp[8])) is None:
        return 'Region not found'

    control_calculation = (sum([(ord(i) - 48) * (ord(j) - 48) for i, j in zip(list(cnp[:-1]), control_string)])) % 11

    if control_calculation == 10:
        control_calculation = 1

    if control_calculation != int(cnp[12]):
        return "Wrong value for control character"

    return "Good CNP"


if __name__ == "__main__":
    control_string = '279146358279'
    months = {1: ['January', 31], 2: ['February', 28], 3: ['March', 31], 4: ['April', 30], 5: ['May', 31],
              6: ['June', 30],
              7: ['July', 31], 8: ['August', 30], 9: ['September', 31], 10: ['October', 30], 11: ['November', 31],
              12: ['December', 30]}
    regions = {1: 'Alba', 2: 'Arad', 3: 'Arges', 4: 'Bacau', 5: 'Bihor', 6: 'Bistrita-Nasaud', 7: 'Botosani',
               8: 'Brasov',
               9: 'Braila', 10: 'Buzau', 11: 'Caras-Severin', 12: 'Cluj', 13: 'Constanta', 14: 'Covasna',
               15: 'Dambovita',
               16: 'Dolj', 17: 'Galati', 18: 'Gorj', 19: 'Harghita', 20: 'Hunedoara', 21: 'Ialomita', 22: 'Iasi',
               23: 'Ilfov', 24: 'Maramures', 25: 'Mehedinti', 26: 'Mures', 27: 'Neamt', 28: 'Olt', 29: 'Prahova',
               30: 'Satu Mare', 31: 'Salaj', 32: 'Sibiu', 33: 'Suceava', 34: 'Teleorman', 35: 'Timis', 36: 'Tulcea',
               37: 'Vaslui', 38: 'Valcea', 39: 'Vrancea', 40: 'Bucuresti', 41: 'Bucuresti S.1', 42: 'Bucuresti S.2',
               43: 'Bucuresti S.3', 44: 'Bucuresti S.4', 45: 'Bucuresti S.5', 46: 'Bucuresti S.6', 51: 'Calarasi',
               52: 'Giurgiu'}
    random_cnps = stress_test()
    good_cnps = [x for x in random_cnps if validation(x) == "Good CNP"]
    list_of_objects = [Human(x) for x in good_cnps]

    for x in list_of_objects:
        x.show()
    # CNP_to_Test = input("Introduce a CNP\n")
    # print(validation(CNP_to_Test))
