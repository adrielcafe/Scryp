import falcon
from resources import *

api = falcon.API()
api.add_route('/', Home())
api.add_route('/price/{crypto}/{fiat}', Price())
api.add_route('/balance/{crypto}/{address}', Balance())
api.add_route('/identify/{address}', Identify())
api.add_route('/transaction/{crypto}/{address}', Transactions())
api.add_route('/transaction/{crypto}/single/{txid}', Transactions())
api.add_route('/block/{crypto}', Block())
api.add_route('/block/{crypto}/{filter}', Block())
api.add_sink(not_found, '')