#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """
    return type(ez_list)



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
    """
    Return the very first member of `ez_list`
    """
    return ez_list[0]


def foo_b():
    """
    Return the sum of the 2nd and 4th members of
      `ezlist`
    """
    return ez_list[1] + ez_list[3]


def foo_c():
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """
    return ez_list[8]


def foo_cx():
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """
    return type(ez_list[7])


def foo_d():
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """
    return ez_list[7][1]


def foo_e():
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """
    return len(ez_list)

def foo_f():
    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """
    string1 = str(ez_list[5][0])
    string2 = str(ez_list[5][1])
    string3 = str(ez_list[5][2])
    return (string1 + ';' + string2 + ';' + string3)

def foo_g():
    """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """
    myList = [ez_list[1],ez_list[2],ez_list[3],ez_list[4]]
    return myList

def foo_h():
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """

    myList = [ez_list[8], ez_list[7], ez_list[6]]
    return myList
