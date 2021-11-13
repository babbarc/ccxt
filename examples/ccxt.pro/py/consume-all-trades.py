import ccxtpro
from asyncio import get_running_loop, run


async def consume_all_trades(exchange, symbol):
    await exchange.load_markets()
    while True:
        try:
            trades = await exchange.watch_trades(symbol)
            print('----------------------------------------------------------------------')
            print(exchange.iso8601(exchange.milliseconds()), 'received', len(trades), 'new', symbol, 'trades:')
            for trade in trades:
                print(exchange.id, symbol, trade['id'], trade['datetime'], trade['amount'], trade['price'])
            exchange.trades[symbol].clear()
        except Exception as e:
            print(type(e).__name__, str(e))
    await exchange.close()


loop = get_running_loop()
exchange = ccxtpro.bitmex({
    'enableRateLimit': True,
    'asyncio_loop': loop,
})

symbol = 'BTC/USD'

run(consume_all_trades(exchange, symbol))