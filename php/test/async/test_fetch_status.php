<?php
namespace ccxt;
use \ccxt\Precise;
use React\Async;
use React\Promise;

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------
include_once __DIR__ . '/../base/test_status.php';

function test_fetch_status($exchange) {
    return Async\async(function () use ($exchange) {
        $method = 'fetchStatus';
        $status = Async\await($exchange->fetch_status());
        test_status($exchange, $method, $status, $exchange->milliseconds());
    }) ();
}
