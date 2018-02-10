import falcon
from resources import *
from config import *

api = falcon.API()
api.add_route(ROUTE_PREFIX + '/', Home())
api.add_route(ROUTE_PREFIX + '/price/{crypto}/{fiat}', Price())
api.add_route(ROUTE_PREFIX + '/balance/{crypto}/{address}', Balance())
api.add_route(ROUTE_PREFIX + '/identify/{address}', Identify())
api.add_route(ROUTE_PREFIX + '/transaction/{crypto}/{address}', Transactions())
api.add_route(ROUTE_PREFIX + '/transaction/{crypto}/single/{txid}', Transactions())
api.add_route(ROUTE_PREFIX + '/block/{crypto}', Block())
api.add_route(ROUTE_PREFIX + '/block/{crypto}/{filter}', Block())
api.add_sink(not_found, '')