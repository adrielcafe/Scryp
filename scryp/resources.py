import falcon
import moneywagon
import ujson
from version import VERSION

api_price = moneywagon.CurrentPrice()
api_block = moneywagon.GetBlock()
api_balance = moneywagon.AddressBalance()
api_single_transaction = moneywagon.SingleTransaction()
api_transactions = moneywagon.HistoricalTransactions()
api_identify = moneywagon.guess_currency_from_address

class Home(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps({
                'version': VERSION
            })

class Price(object):
    def on_get(self, req, resp, crypto, fiat):
        price = api_price.action(crypto, fiat)
        
        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps({
                'price': price
            })

class Balance(object):
    def on_get(self, req, resp, crypto, address):
        balance = api_balance.action(crypto, address)
        
        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps({
                'balance': balance
            })

class Identify(object):
    def on_get(self, req, resp, address):
        cryptos = map(lambda crypto: crypto[0], api_identify(address))

        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps(cryptos)

class Transactions(object):
    def on_get(self, req, resp, crypto, address = None, txid = None):
        transactions = api_transactions.action(crypto, address) if address \
                    else api_single_transaction.action(crypto, txid)
        
        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps(transactions)

class Block(object):
    def on_get(self, req, resp, crypto, filter = None):
        block = api_block.action(crypto, latest = True) if not filter \
            else api_block.action(crypto, block_number = filter) if type(filter) == int \
            else api_block.action(crypto, block_hash = filter)

        resp.status = falcon.HTTP_200
        resp.body = ujson.dumps(block)

def not_found(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = ujson.dumps({
            'error': 'Not found'
        })
