name = input()


def normalize(name_):
    # put your code here
    return (
        name_.replace('á', 'a').replace('å', 'a').replace('é', 'e').replace('ë', 'e').replace('æ', 'ae').replace('œ',
                                                                                                                 'oe'))


print(normalize(name))
