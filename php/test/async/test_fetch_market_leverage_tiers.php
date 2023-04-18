<?php
namespace ccxt;
use \ccxt\Precise;
use React\Async;
use React\Promise;

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------
include_once __DIR__ . '/../base/test_leverage_tier.php';

function test_fetch_market_leverage_tiers($exchange, $symbol) {
    return Async\async(function () use ($exchange, $symbol) {
        $method = 'fetchMarketLeverageTiers';
        $tiers = Async\await($exchange->fetch_market_leverage_tiers($symbol));
        assert(gettype($tiers) === 'array' && array_keys($tiers) === array_keys(array_keys($tiers)), $exchange->id . ' ' . $method . ' ' . $symbol . ' must return an array. ' . $exchange->json($tiers));
        $array_length = count($tiers);
        assert($array_length >= 1, $exchange->id . ' ' . $method . ' ' . $symbol . ' must return an array with at least one entry. ' . $exchange->json($tiers));
        for ($j = 0; $j < count($tiers); $j++) {
            test_leverage_tier($exchange, $method, $tiers[$j]);
        }
    }) ();
}
