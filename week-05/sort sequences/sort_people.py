from datastubs import PEOPLE_LIST
from operator import itemgetter

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    # fill it out
    newlist = sorted(PEOPLE_LIST, key=itemgetter('age'))
    return newlist

def oldest():
    """
    sort by age in descending order
    """
    # fill it out
    newlist = sorted(PEOPLE_LIST, key=itemgetter('age'), reverse=True)
    return newlist

def name_reverse_alpha():
    # fill it out
    return sorted(PEOPLE_LIST, key=itemgetter('name'), reverse=True)
    
def country_then_age():
    # fill it out
    return sorted(PEOPLE_LIST, key=itemgetter('country', 'age'))
