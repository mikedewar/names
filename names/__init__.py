from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
import math


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}

def get_full_names(N):
    with open(FILES["first:male"]) as m:
        male_names = [x.split()[0] for x in random.choices(m.readlines(), k=math.floor(N/2))]

    with  open(FILES["first:female"]) as f:
        female_names = [x.split()[0] for x in random.choices(f.readlines(), k=math.ceil(N/2))]

    with open(FILES["last"]) as l:
        last_names = [x.split()[0] for x in random.choices(l.readlines(), k=N)]

    return [" ".join([f,l]) for f,l in zip(male_names + female_names, last_names)]


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())
