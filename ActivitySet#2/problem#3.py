

'''def get_cs():
    """get string input"""


def cs_to_lot(cs):
    """convert connected string to list of strings"""


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()'''

def get_cs():
    Pepet=input("Enter the string")
    return Pepet


def cs_to_lot(cs):
    Pep=list(cs)
    return Pep


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()