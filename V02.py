from bottle import route, run, template, error, abort, static_file, request
#import bottle
#from bottle import *


@route('/')
def index():
    return '''
    <h2>Verkefni 2. </h2>
    <p><a href='/A'>Liður A</a></p>
    <p><a href='/B'>Liður B</a></p>  
    '''
@route('/A')
def A():
    return '''
        <h2>Verkefni 2. Liður A</h2>
        <a href='/Sida/1'>Siða 1.</a> -
        <a href='/Sida/2'>Siða 2.</a> -
        <a href='/Sida/3'>Siða 3.</a> -
        <a href='/'>Forsíða.</a> -
        '''

@route('/Sida/<id>')
def pege(id):
    if id == '1':
        return "Þetta er síða 1<br><a href='/A'>Til baka</a>"
    if id == '2':
        return "Þetta er síða 2<br><a href='/A'>Til baka</a>"
    if id == '3':
        return "Þetta er síða 3<br><a href='/A'>Til baka</a>"
    else:
        abort(404,"<h2 style='color:blue'> Þessi síða finnst ekki</h2>")




#############################

@route('/B')
def b():
    return """
    <h2>Verkefni 2. Liður B</h2>
    <h4> Veldu upaháls myndina þína </h4>
    <a href='/sida2?pondur=a'><img src='myndir/panda1.jpeg'>
    <a href='/sida2?pondur=b'><img src='myndir/panda2.jpg'>
    <a href='/sida2?pondur=c'><img src='myndir/panda3.jpg'>
    <a href='/sida2?pondur=d'><img src='myndir/panda4.jpg'>
    <br><a href='/'>Forsíða.</a> 
    """
@route('/sida2')
def page():
    x = request.query.pondur
    if x == 'a':
        return "<h3>Uppaháls myndin mín er: </h3><img src='myndir/panda1.jpeg'><br><a href='/'>Forsíða.</a>"
    x = request.query.pondur
    if x == 'b':
        return "<h3>Uppaháls myndin mín er: </h3><img src='myndir/panda2.jpg'><br><a href='/'>Forsíða.</a>"
    x = request.query.pondur
    if x == 'c':
        return "<h3>Uppaháls myndin mín er: </h3><img src='myndir/panda3.jpg'><br><a href='/'>Forsíða.</a>"
    x = request.query.pondur
    if x == 'd':
        return "<h3>Uppaháls myndin mín er: </h3><img src='myndir/panda4.jpg'><br><a href='/'>Forsíða.</a> "

#############################

@route('/myndir/<skra>')
def static_skra(skra):
    return static_file(skra, root='myndir')



@error(404)
def villa(error):
    return "<h2 style='color:blue'>Error 404</h2>"




run(host='localhost',port=8060,reloader=True, debug=True)
#run(host='0.0.0.0',  port=os.ehviro.get('PORT'))
