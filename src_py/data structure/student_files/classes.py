"""Module containing classes for storing and comparing Keys."""
import doctest
from stats import StatCounter, KEY_COMPS

KEY_COMP_ERROR = 'Can only compare Keys with other Keys'


def list_of_keys(original_list):
    """ Takes an list/iterable of normal values and returns a list of Keys
    made out of those values.
    >>> keys = list_of_keys([1,2,3,4])
    >>> print(isinstance(keys[0], Key))
    True
    >>> print(keys)
    [1, 2, 3, 4]
    """
    return [Key(item) for item in original_list]


class Key:
    """A wrapped key value representing a value.
    Keys will count any comparisons against other Keys, via the StatCounter class in stats.py.
    >>> k1 = Key('a')
    >>> k2 = Key('b')
    >>> k3 = Key(1)
    >>> k4 = Key(2)
    >>> print(k1 < k2)
    True
    >>> print(k3 < k4)
    True
    >>> print(StatCounter.get_count(KEY_COMPS))
    2
    >>> print(k1 == k2)
    False
    >>> print(k1 > k2)
    False
    >>> print(k1 <= k2)
    True
    >>> print(k1 >= k2)
    False
    >>> print(k1 != k2)
    True
    """

    def __init__(self, value):
        self.__raw = value

    def __eq__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            StatCounter.increment(KEY_COMPS)
            return self.__raw == j.__raw

    def __le__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            StatCounter.increment(KEY_COMPS)
            return self.__raw <= j.__raw

    def __ne__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            return self.__raw != j.__raw

    def __lt__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            StatCounter.increment(KEY_COMPS)
            return self.__raw < j.__raw

    def __gt__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            StatCounter.increment(KEY_COMPS)
            return self.__raw > j.__raw

    def __ge__(self, j):
        if not isinstance(j, Key):
            raise TypeError(KEY_COMP_ERROR)
        else:
            StatCounter.increment(KEY_COMPS)
            return self.__raw >= j.__raw

    def __repr__(self):
        return repr(self.__raw)

    def __str__(self):
        return str(self.__raw)

    def __getattr__(self, attr):
        """All other behaviours use self.__raw's native methods.
        You probably shouldn't be using any other methods though...
        """
        return self.__raw.__getattribute__(attr)


if __name__ == '__main__':
    doctest.testmod()
    print('Some examples\n-------------')
    # make a Key from an int
    my_key = Key(1)
    print(my_key)

    # make a key from a str
    my_key = Key('a')
    print(my_key)

    # make a list of keys from a list of ints
    my_keys = list_of_keys([1, 2, 3, 4])
    my_keys = list_of_keys([1, 2, 3, 4])
    print(my_keys)

    # make a list of keys from a range
    my_keys = list_of_keys(range(0, 10))
    print(my_keys)
