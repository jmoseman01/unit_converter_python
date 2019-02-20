'''
Created on Feb 16, 2019

@author: jesse
'''


def convert_metric(from_metric,to_metric):
    metricExponents = {
        'M': 6,
        'k': 3,
        'noprefix': 0,
        'd':-1,
        'c':-2,
        'm':-3,
        'u':-6,
        'n':-9,
        'p':-12
    }
    from_unit_value = metricExponents[from_metric]
    to_unit_value = metricExponents[to_metric]
    exponent_delta = from_unit_value - to_unit_value
    return exponent_delta


number_of_initial_units=input('number of initial units:  ')
from_metric= raw_input('from metric:  ')
to_metric=raw_input('to metric:  ')

print('%d %s=%d*10^%d %s'%(number_of_initial_units,from_metric,number_of_initial_units,convert_metric(from_metric,to_metric),to_metric))