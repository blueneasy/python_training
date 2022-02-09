
class Unpacking:

    @staticmethod
    def unpack(*args):
        joined = ''
        for a in args:
            joined += a
        return joined

    @staticmethod
    def unpack_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f'{key}={value}')

    @staticmethod
    def calculate_sum_via_args(*args):
        result = 0
        for number in args:
            result += number
        return result


if __name__ == '__main__':
    lista = [0, 5, 3, 2, 7]
    # listb = ['t', 'a', 't', 'a', 'r']
    listc = [4, 6, 9]
    # result = Unpacking.calculate_sum_via_args(*lista)
    # print(result)
    # print(Unpacking.unpack(*listb))
    dicta = {
        'name': 'Michal',
        'age': 27,
        'job': 'python dev',
    }
    dictb = {
        'name2': 'Magda',
        'age2': 26,
        'job2': 'front end dev',
    }

    # print(Unpacking.unpack_kwargs(**dicta))
    # listd = [*lista, *listc]
    # print(listd)

    dictc = {**dicta, **dictb}
    print(dictc)