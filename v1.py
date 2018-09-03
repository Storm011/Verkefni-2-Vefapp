#from bottle import route,run,template

from sys import argv

import bottle
from bottle import *

@route('/')
def index():
    return '''
    <h2>Verkefni 1. </h2>
    <p><a href='/about'>Sunna</a></p>
    <p><a href='/bio'>bio</a></p>
    <p><a href='/pics'>D</a></p>
    '''
@route('/about')
def lappi():
    return 'Hæ. eg heiti Sunna'

@route('/bio')
def lappi():
    return 'Bio'

@route('/pics')
def lappi():
    return 'D er stafur'

bottle.run(host='0.0.0.0',  port=argv[1])

#run(host='localhost',port=8060, debug=True)
