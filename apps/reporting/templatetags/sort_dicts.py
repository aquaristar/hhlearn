from django import template
import re
register = template.Library()

def sort_dict(value):
    #custom template tag used like so:
    #{{dictionary|dict_get:var}}
    #where dictionary is duh a dictionary and var is a variable representing
    #one of it's keys

    return sorted(value)
#def sort_dict_by_id(value):


def dict_id(tup):
    key, d = tup
    id = key.find(".")
    id = int(key[:id])
    return id

def sort_dict_acronym(value):

    return sorted(value, key=acronym_key)

def acronym_key(tup):
    key, d = tup
    #s = re.search('\(\s*([^} ]+)\s*\)', key)
    s = re.findall(r'\(\s*([^} ]+)\s*\)', key)[-1]
    acronym = s
    return acronym

register.filter('sort_dict',sort_dict)
register.filter('sort_dict_acronym',sort_dict_acronym)