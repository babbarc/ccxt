# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.pro.base.exchange import Exchange
import ccxt.async_support
from ccxt.pro.base.cache import ArrayCache, ArrayCacheBySymbolById, ArrayCacheByTimestamp
import hashlib
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import ArgumentsRequired


class okcoin(Exchange, ccxt.async_support.okcoin):

    def describe(self):
        return self.deep_extend(super(okcoin, self).describe(), {
            'has': {
                'ws': True,
                'watchTicker': True,
                'watchTickers': False,  # for now
                'watchOrderBook': True,
                'watchOrders': True,
                'watchTrades': True,
                'watchBalance': True,
                'watchOHLCV': True,
            },
            'urls': {
                'api': {
                    'ws': 'wss://real.okcoin.com:8443/ws/v3',
                },
                'logo': 'https://user-images.githubusercontent.com/1294454/27766791-89ffb502-5ee5-11e7-8a5b-c5950b68ac65.jpg',
                'www': 'https://www.okcoin.com',
                'doc': 'https://www.okcoin.com/docs/en/',
                'fees': 'https://www.okcoin.com/coin-fees',
                'referral': 'https://www.okcoin.com/account/register?flag=activity&channelId=600001513',
            },
            'options': {
                'fetchMarkets': ['spot'],
                'watchOrders': 'order',  # or algo_order
                'watchOrderBook': {
                    'limit': 400,  # max
                    'type': 'spot',  # margin
                    'depth': 'depth_l2_tbt',  # depth5, depth
                },
                'watchBalance': 'spot',  # margin, futures, swap
                'ws': {
                    'inflate': True,
                },
            },
            'streaming': {
                # okex does not support built-in ws protocol-level ping-pong
                # instead it requires a custom text-based ping-pong
                'ping': self.ping,
                'keepAlive': 20000,
            },
        })

    async def subscribe(self, channel, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        url = self.urls['api']['ws']
        messageHash = market['type'] + '/' + channel + ':' + market['id']
        request = {
            'op': 'subscribe',
            'args': [messageHash],
        }
        return await self.watch(url, messageHash, self.deep_extend(request, params), messageHash)

    async def watch_trades(self, symbol, since=None, limit=None, params={}):
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int|None since: timestamp in ms of the earliest trade to fetch
        :param int|None limit: the maximum amount of trades to fetch
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html?#public-trades>`
        """
        await self.load_markets()
        symbol = self.symbol(symbol)
        trades = await self.subscribe('trade', symbol, params)
        if self.newUpdates:
            limit = trades.getLimit(symbol, limit)
        return self.filter_by_since_limit(trades, since, limit, 'timestamp', True)

    async def watch_orders(self, symbol=None, since=None, limit=None, params={}):
        """
        watches information on multiple orders made by the user
        :param str|None symbol: unified market symbol of the market orders were made in
        :param int|None since: the earliest time in ms to fetch orders for
        :param int|None limit: the maximum number of  orde structures to retrieve
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns [dict]: a list of `order structures <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        await self.load_markets()
        await self.authenticate()
        if symbol is not None:
            symbol = self.symbol(symbol)
        orderType = self.safe_string(self.options, 'watchOrders', 'order')
        trades = await self.subscribe(orderType, symbol, params)
        if self.newUpdates:
            limit = trades.getLimit(symbol, limit)
        return self.filter_by_since_limit(trades, since, limit, 'timestamp', True)

    def handle_orders(self, client, message, subscription=None):
        #
        # {
        #     table: 'spot/order',
        #     data: [
        #       {
        #         client_oid: '',
        #         created_at: '2022-03-04T16:44:58.530Z',
        #         event_code: '0',
        #         event_message: '',
        #         fee: '',
        #         fee_currency: '',
        #         filled_notional: '0',
        #         filled_size: '0',
        #         instrument_id: 'LTC-USD',
        #         last_amend_result: '',
        #         last_fill_id: '0',
        #         last_fill_px: '0',
        #         last_fill_qty: '0',
        #         last_fill_time: '1970-01-01T00:00:00.000Z',
        #         last_request_id: '',
        #         margin_trading: '1',
        #         notional: '',
        #         order_id: '8629537900471296',
        #         order_type: '0',
        #         price: '1500',
        #         rebate: '',
        #         rebate_currency: '',
        #         side: 'sell',
        #         size: '0.0133',
        #         state: '0',
        #         status: 'open',
        #         timestamp: '2022-03-04T16:44:58.530Z',
        #         type: 'limit'
        #       }
        #     ]
        #   }
        #
        table = self.safe_string(message, 'table')
        orders = self.safe_value(message, 'data', [])
        ordersLength = len(orders)
        if ordersLength > 0:
            limit = self.safe_integer(self.options, 'ordersLimit', 1000)
            if self.orders is None:
                self.orders = ArrayCacheBySymbolById(limit)
            stored = self.orders
            marketIds = {}
            parsed = self.parse_orders(orders)
            for i in range(0, len(parsed)):
                order = parsed[i]
                stored.append(order)
                symbol = order['symbol']
                market = self.market(symbol)
                marketIds[market['id']] = True
            keys = list(marketIds.keys())
            for i in range(0, len(keys)):
                messageHash = table + ':' + keys[i]
                client.resolve(self.orders, messageHash)

    async def watch_ticker(self, symbol, params={}):
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/en/latest/manual.html#ticker-structure>`
        """
        return await self.subscribe('ticker', symbol, params)

    def handle_trade(self, client, message):
        #
        #     {
        #         table: 'spot/trade',
        #         data: [
        #             {
        #                 side: 'buy',
        #                 trade_id: '30770973',
        #                 price: '4665.4',
        #                 size: '0.019',
        #                 instrument_id: 'BTC-USDT',
        #                 timestamp: '2020-03-16T13:41:46.526Z'
        #             }
        #         ]
        #     }
        #
        table = self.safe_string(message, 'table')
        data = self.safe_value(message, 'data', [])
        tradesLimit = self.safe_integer(self.options, 'tradesLimit', 1000)
        for i in range(0, len(data)):
            trade = self.parse_trade(data[i])
            symbol = trade['symbol']
            marketId = self.safe_string(trade['info'], 'instrument_id')
            messageHash = table + ':' + marketId
            stored = self.safe_value(self.trades, symbol)
            if stored is None:
                stored = ArrayCache(tradesLimit)
                self.trades[symbol] = stored
            stored.append(trade)
            client.resolve(stored, messageHash)
        return message

    def handle_ticker(self, client, message):
        #
        #     {
        #         table: 'spot/ticker',
        #         data: [
        #             {
        #                 last: '4634.1',
        #                 open_24h: '5305.6',
        #                 best_bid: '4631.6',
        #                 high_24h: '5950',
        #                 low_24h: '4448.8',
        #                 base_volume_24h: '147913.11435388',
        #                 quote_volume_24h: '756850119.99108082',
        #                 best_ask: '4631.7',
        #                 instrument_id: 'BTC-USDT',
        #                 timestamp: '2020-03-16T13:16:25.677Z',
        #                 best_bid_size: '0.12348942',
        #                 best_ask_size: '0.00100014',
        #                 last_qty: '0.00331822'
        #             }
        #         ]
        #     }
        #
        table = self.safe_string(message, 'table')
        data = self.safe_value(message, 'data', [])
        for i in range(0, len(data)):
            ticker = self.parse_ticker(data[i])
            symbol = ticker['symbol']
            marketId = self.safe_string(ticker['info'], 'instrument_id')
            messageHash = table + ':' + marketId
            self.tickers[symbol] = ticker
            client.resolve(ticker, messageHash)
        return message

    async def watch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int|None since: timestamp in ms of the earliest candle to fetch
        :param int|None limit: the maximum amount of candles to fetch
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns [[int]]: A list of candles ordered as timestamp, open, high, low, close, volume
        """
        await self.load_markets()
        symbol = self.symbol(symbol)
        interval = self.safe_string(self.timeframes, timeframe, timeframe)
        name = 'candle' + interval + 's'
        ohlcv = await self.subscribe(name, symbol, params)
        if self.newUpdates:
            limit = ohlcv.getLimit(symbol, limit)
        return self.filter_by_since_limit(ohlcv, since, limit, 0, True)

    def handle_ohlcv(self, client, message):
        #
        #     {
        #         table: "spot/candle60s",
        #         data: [
        #             {
        #                 candle: [
        #                     "2020-03-16T14:29:00.000Z",
        #                     "4948.3",
        #                     "4966.7",
        #                     "4939.1",
        #                     "4945.3",
        #                     "238.36021657"
        #                 ],
        #                 instrument_id: "BTC-USDT"
        #             }
        #         ]
        #     }
        #
        table = self.safe_string(message, 'table')
        data = self.safe_value(message, 'data', [])
        parts = table.split('/')
        part1 = self.safe_string(parts, 1)
        interval = part1.replace('candle', '')
        interval = interval.replace('s', '')
        # use a reverse lookup in a static map instead
        timeframe = self.find_timeframe(interval)
        for i in range(0, len(data)):
            marketId = self.safe_string(data[i], 'instrument_id')
            candle = self.safe_value(data[i], 'candle')
            market = self.safe_market(marketId)
            symbol = market['symbol']
            parsed = self.parse_ohlcv(candle, market)
            self.ohlcvs[symbol] = self.safe_value(self.ohlcvs, symbol, {})
            stored = self.safe_value(self.ohlcvs[symbol], timeframe)
            if stored is None:
                limit = self.safe_integer(self.options, 'OHLCVLimit', 1000)
                stored = ArrayCacheByTimestamp(limit)
                self.ohlcvs[symbol][timeframe] = stored
            stored.append(parsed)
            messageHash = table + ':' + marketId
            client.resolve(stored, messageHash)

    async def watch_order_book(self, symbol, limit=None, params={}):
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int|None limit: the maximum amount of order book entries to return
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/en/latest/manual.html#order-book-structure>` indexed by market symbols
        """
        options = self.safe_value(self.options, 'watchOrderBook', {})
        depth = self.safe_string(options, 'depth', 'depth_l2_tbt')
        orderbook = await self.subscribe(depth, symbol, params)
        return orderbook.limit()

    def handle_delta(self, bookside, delta):
        price = self.safe_float(delta, 0)
        amount = self.safe_float(delta, 1)
        bookside.store(price, amount)

    def handle_deltas(self, bookside, deltas):
        for i in range(0, len(deltas)):
            self.handle_delta(bookside, deltas[i])

    def handle_order_book_message(self, client, message, orderbook):
        #
        #     {
        #         instrument_id: "BTC-USDT",
        #         asks: [
        #             ["4568.5", "0.49723138", "2"],
        #             ["4568.7", "0.5013", "1"],
        #             ["4569.1", "0.4398", "1"],
        #         ],
        #         bids: [
        #             ["4568.4", "0.84187666", "5"],
        #             ["4568.3", "0.75661506", "6"],
        #             ["4567.8", "2.01", "2"],
        #         ],
        #         timestamp: "2020-03-16T11:11:43.388Z",
        #         checksum: 473370408
        #     }
        #
        asks = self.safe_value(message, 'asks', [])
        bids = self.safe_value(message, 'bids', [])
        self.handle_deltas(orderbook['asks'], asks)
        self.handle_deltas(orderbook['bids'], bids)
        timestamp = self.parse8601(self.safe_string(message, 'timestamp'))
        orderbook['timestamp'] = timestamp
        orderbook['datetime'] = self.iso8601(timestamp)
        return orderbook

    def handle_order_book(self, client, message):
        #
        # first message(snapshot)
        #
        #     {
        #         table: "spot/depth",
        #         action: "partial",
        #         data: [
        #             {
        #                 instrument_id: "BTC-USDT",
        #                 asks: [
        #                     ["4568.5", "0.49723138", "2"],
        #                     ["4568.7", "0.5013", "1"],
        #                     ["4569.1", "0.4398", "1"],
        #                 ],
        #                 bids: [
        #                     ["4568.4", "0.84187666", "5"],
        #                     ["4568.3", "0.75661506", "6"],
        #                     ["4567.8", "2.01", "2"],
        #                 ],
        #                 timestamp: "2020-03-16T11:11:43.388Z",
        #                 checksum: 473370408
        #             }
        #         ]
        #     }
        #
        # subsequent updates
        #
        #     {
        #         table: "spot/depth",
        #         action: "update",
        #         data: [
        #             {
        #                 instrument_id:   "BTC-USDT",
        #                 asks: [
        #                     ["4598.8", "0", "0"],
        #                     ["4599.1", "0", "0"],
        #                     ["4600.3", "0", "0"],
        #                 ],
        #                 bids: [
        #                     ["4598.5", "0.08", "1"],
        #                     ["4598.2", "0.0337323", "1"],
        #                     ["4598.1", "0.12681801", "3"],
        #                 ],
        #                 timestamp: "2020-03-16T11:20:35.139Z",
        #                 checksum: 740786981
        #             }
        #         ]
        #     }
        #
        action = self.safe_string(message, 'action')
        data = self.safe_value(message, 'data', [])
        table = self.safe_string(message, 'table')
        if action == 'partial':
            for i in range(0, len(data)):
                update = data[i]
                marketId = self.safe_string(update, 'instrument_id')
                market = self.safe_market(marketId)
                symbol = market['symbol']
                options = self.safe_value(self.options, 'watchOrderBook', {})
                # default limit is 400 bidasks
                limit = self.safe_integer(options, 'limit', 400)
                orderbook = self.order_book({}, limit)
                self.orderbooks[symbol] = orderbook
                self.handle_order_book_message(client, update, orderbook)
                messageHash = table + ':' + marketId
                client.resolve(orderbook, messageHash)
        else:
            for i in range(0, len(data)):
                update = data[i]
                marketId = self.safe_string(update, 'instrument_id')
                market = self.safe_market(marketId)
                symbol = market['symbol']
                if symbol in self.orderbooks:
                    orderbook = self.orderbooks[symbol]
                    self.handle_order_book_message(client, update, orderbook)
                    messageHash = table + ':' + marketId
                    client.resolve(orderbook, messageHash)
        return message

    async def authenticate(self, params={}):
        self.check_required_credentials()
        url = self.urls['api']['ws']
        messageHash = 'login'
        client = self.client(url)
        future = self.safe_value(client.subscriptions, messageHash)
        if future is None:
            future = client.future('authenticated')
            timestamp = str(self.seconds())
            method = 'GET'
            path = '/users/self/verify'
            auth = timestamp + method + path
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha256, 'base64')
            request = {
                'op': messageHash,
                'args': [
                    self.apiKey,
                    self.password,
                    timestamp,
                    signature,
                ],
            }
            self.spawn(self.watch, url, messageHash, request, messageHash, future)
        return await future

    async def watch_balance(self, params={}):
        """
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict params: extra parameters specific to the okcoin api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/en/latest/manual.html?#balance-structure>`
        """
        defaultType = self.safe_string_2(self.options, 'watchBalance', 'defaultType')
        type = self.safe_string(params, 'type', defaultType)
        if type is None:
            raise ArgumentsRequired(self.id + " watchBalance requires a type parameter(one of 'spot', 'margin', 'futures', 'swap')")
        # query = self.omit(params, 'type')
        negotiation = await self.authenticate()
        return await self.subscribe_to_user_account(negotiation, params)

    async def subscribe_to_user_account(self, negotiation, params={}):
        defaultType = self.safe_string_2(self.options, 'watchBalance', 'defaultType')
        type = self.safe_string(params, 'type', defaultType)
        if type is None:
            raise ArgumentsRequired(self.id + " watchBalance requires a type parameter(one of 'spot', 'margin', 'futures', 'swap')")
        await self.load_markets()
        currencyId = self.safe_string(params, 'currency')
        code = self.safe_string(params, 'code', self.safe_currency_code(currencyId))
        currency = None
        if code is not None:
            currency = self.currency(code)
        symbol = self.safe_string(params, 'symbol')
        market = self.market(symbol)
        marketUndefined = (market is None)
        currencyUndefined = (currency is None)
        if type == 'spot':
            if currencyUndefined:
                raise ArgumentsRequired(self.id + " watchBalance requires a 'currency'(id) or a unified 'code' parameter for " + type + ' accounts')
        elif (type == 'margin') or (type == 'swap') or (type == 'option'):
            if marketUndefined:
                raise ArgumentsRequired(self.id + " watchBalance requires a 'instrument_id'(id) or a unified 'symbol' parameter for " + type + ' accounts')
        elif type == 'futures':
            if currencyUndefined and marketUndefined:
                raise ArgumentsRequired(self.id + " watchBalance requires a 'currency'(id), or unified 'code', or 'instrument_id'(id), or unified 'symbol' parameter for " + type + ' accounts')
        suffix = None
        if not currencyUndefined:
            suffix = currency['id']
        elif not marketUndefined:
            suffix = market['id']
        accountType = 'spot' if (type == 'margin') else type
        account = 'margin_account' if (type == 'margin') else 'account'
        messageHash = accountType + '/' + account
        subscriptionHash = messageHash + ':' + suffix
        url = self.urls['api']['ws']
        request = {
            'op': 'subscribe',
            'args': [subscriptionHash],
        }
        query = self.omit(params, ['currency', 'code', 'instrument_id', 'symbol', 'type'])
        return await self.watch(url, messageHash, self.deep_extend(request, query), subscriptionHash)

    def handle_balance(self, client, message):
        #
        # spot
        #
        #     {
        #         table: 'spot/account',
        #         data: [
        #             {
        #                 available: '11.044827320825',
        #                 currency: 'USDT',
        #                 id: '',
        #                 balance: '11.044827320825',
        #                 hold: '0'
        #             }
        #         ]
        #     }
        #
        # margin
        #
        #     {
        #         table: "spot/margin_account",
        #         data: [
        #             {
        #                 maint_margin_ratio: "0.08",
        #                 liquidation_price: "0",
        #                 'currency:USDT': {available: "0", balance: "0", borrowed: "0", hold: "0", lending_fee: "0"},
        #                 tiers: "1",
        #                 instrument_id:   "ETH-USDT",
        #                 'currency:ETH': {available: "0", balance: "0", borrowed: "0", hold: "0", lending_fee: "0"}
        #             }
        #         ]
        #     }
        #
        table = self.safe_string(message, 'table')
        parts = table.split('/')
        data = self.safe_value(message, 'data', [])
        self.balance['info'] = data
        type = self.safe_string(parts, 0)
        if type == 'spot':
            part1 = self.safe_string(parts, 1)
            if part1 == 'margin_account':
                type = 'margin'
        for i in range(0, len(data)):
            balance = self.parseBalanceByType(type, data)
            oldBalance = self.safe_value(self.balance, type, {})
            newBalance = self.deep_extend(oldBalance, balance)
            self.balance[type] = self.safe_balance(newBalance)
            client.resolve(self.balance[type], table)

    def handle_subscription_status(self, client, message):
        #
        #     {"event":"subscribe","channel":"spot/depth:BTC-USDT"}
        #
        # channel = self.safe_string(message, 'channel')
        # client.subscriptions[channel] = message
        return message

    def handle_authenticate(self, client, message):
        #
        #     {event: 'login', success: True}
        #
        client.resolve(message, 'authenticated')
        return message

    def ping(self, client):
        # okex does not support built-in ws protocol-level ping-pong
        # instead it requires custom text-based ping-pong
        return 'ping'

    def handle_pong(self, client, message):
        client.lastPong = self.milliseconds()
        return message

    def handle_error_message(self, client, message):
        #
        #     {event: 'error', message: 'Invalid sign', errorCode: 30013}
        #     {"event":"error","message":"Unrecognized request: {\"event\":\"subscribe\",\"channel\":\"spot/depth:BTC-USDT\"}","errorCode":30039}
        #     {event: 'error', message: "Channel spot/order doesn't exist", errorCode: 30040}
        #
        errorCode = self.safe_string(message, 'errorCode')
        try:
            if errorCode is not None:
                feedback = self.id + ' ' + self.json(message)
                self.throw_exactly_matched_exception(self.exceptions['exact'], errorCode, feedback)
                messageString = self.safe_value(message, 'message')
                if messageString is not None:
                    self.throw_broadly_matched_exception(self.exceptions['broad'], messageString, feedback)
        except Exception as e:
            if isinstance(e, AuthenticationError):
                client.reject(e, 'authenticated')
                method = 'login'
                if method in client.subscriptions:
                    del client.subscriptions[method]
                return False
        return message

    def handle_message(self, client, message):
        if not self.handle_error_message(client, message):
            return
        #
        #     {"event":"error","message":"Unrecognized request: {\"event\":\"subscribe\",\"channel\":\"spot/depth:BTC-USDT\"}","errorCode":30039}
        #     {"event":"subscribe","channel":"spot/depth:BTC-USDT"}
        #     {
        #         table: "spot/depth",
        #         action: "partial",
        #         data: [
        #             {
        #                 instrument_id:   "BTC-USDT",
        #                 asks: [
        #                     ["5301.8", "0.03763319", "1"],
        #                     ["5302.4", "0.00305", "2"],
        #                 ],
        #                 bids: [
        #                     ["5301.7", "0.58911427", "6"],
        #                     ["5301.6", "0.01222922", "4"],
        #                 ],
        #                 timestamp: "2020-03-16T03:25:00.440Z",
        #                 checksum: -2088736623
        #             }
        #         ]
        #     }
        # {
        #     "table":"spot/order",
        #     "data":[
        #         {
        #             "client_oid":"",
        #             "filled_notional":"0",
        #             "filled_size":"0",
        #             "instrument_id":"ETC-USDT",
        #             "last_fill_px":"0",
        #             "last_fill_qty":"0",
        #             "last_fill_time":"1970-01-01T00:00:00.000Z",
        #             "margin_trading":"1",
        #             "notional":"",
        #             "order_id":"3576398568830976",
        #             "order_type":"0",
        #             "price":"5.826",
        #             "side":"buy",
        #             "size":"0.1",
        #             "state":"0",
        #             "status":"open",
        #             "fee_currency":"ETC",
        #             "fee":"-0.01",
        #             "rebate_currency":"open",
        #             "rebate":"0.05",
        #             "timestamp":"2019-09-24T06:45:11.394Z",
        #             "type":"limit",
        #             "created_at":"2019-09-24T06:45:11.394Z"
        #         }
        #     ]
        # }
        #
        if message == 'pong':
            return self.handle_pong(client, message)
        table = self.safe_string(message, 'table')
        if table is None:
            event = self.safe_string(message, 'event')
            if event is not None:
                methods = {
                    # 'info': self.handleSystemStatus,
                    # 'book': 'handleOrderBook',
                    'login': self.handle_authenticate,
                    'subscribe': self.handle_subscription_status,
                }
                method = self.safe_value(methods, event)
                if method is None:
                    return message
                else:
                    return method(client, message)
        else:
            parts = table.split('/')
            name = self.safe_string(parts, 1)
            methods = {
                'depth': self.handle_order_book,
                'depth5': self.handle_order_book,
                'depth_l2_tbt': self.handle_order_book,
                'ticker': self.handle_ticker,
                'trade': self.handle_trade,
                'account': self.handle_balance,
                'margin_account': self.handle_balance,
                'order': self.handle_orders,
                # ...
            }
            method = self.safe_value(methods, name)
            if name.find('candle') >= 0:
                method = self.handle_ohlcv
            if method is None:
                return message
            else:
                return method(client, message)
