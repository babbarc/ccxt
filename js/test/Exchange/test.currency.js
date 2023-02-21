'use strict'

const sharedMethods = require ('./test.sharedMethods.js');

function testCurrency (exchange, entry, method) {
    const format = {
        'info': {},
        'id': 'btc', // string literal for referencing within an exchange
        'code': 'BTC', // uppercase string literal of a pair of currencies
        //----------------------------------------------------------------------
        'name': 'Bitcoin', // uppercase string, base currency, 2 or more letters
        'withdraw': true, // can withdraw
        'deposit': true, // can deposit
        // 'active': true, // can both withdraw & deposit
        'precision': exchange.parseNumber ('0.0001'), // in case of SIGNIFICANT_DIGITS it will be 8 - number of digits "after the dot"
        'fee': exchange.parseNumber ('0.001'), //
        'limits': { // value limits when placing orders on this market
            'withdraw':  {
                'min': exchange.parseNumber ('0.01'),
                'max': exchange.parseNumber ('1000'),
            },
            'deposit':  {
                'min': exchange.parseNumber ('0.01'),
                'max': exchange.parseNumber ('1000'),
            },
        },
        //----------------------------------------------------------------------
    };
    const emptyNotAllowedFor = [ 'id', 'code', 'precision' ];
    sharedMethods.reviseStructureKeys (exchange, method, entry, format, emptyNotAllowedFor);
    sharedMethods.reviseCurrencyCode (exchange, method, entry, entry['code']);
    //
    sharedMethods.Gt (exchange, method, entry, 'precision', '0');
    sharedMethods.Ge (exchange, method, entry, 'fee', '0')
    const limits = exchange.safeValue (entry, 'limits', {});
    const withdrawLimits = exchange.safeValue (limits, 'withdraw', {});
    const depositLimits = exchange.safeValue (limits, 'deposit', {});
    sharedMethods.Ge (exchange, method, withdrawLimits, 'min', '0');
    sharedMethods.Ge (exchange, method, withdrawLimits, 'max', '0');
    sharedMethods.Ge (exchange, method, depositLimits, 'min', '0');
    sharedMethods.Ge (exchange, method, depositLimits, 'max', '0');
}

module.exports = testCurrency;
