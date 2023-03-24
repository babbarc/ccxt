// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

import { implicitReturnType } from '../base/types.js';
import { Exchange as _Exchange } from '../base/Exchange.js';

export default abstract class Exchange extends _Exchange {
    abstract xreserveGetNonce (params?: {}): Promise<implicitReturnType>;
    abstract xreserveGetFee (params?: {}): Promise<implicitReturnType>;
    abstract xreserveGetDelegatedTransactions (params?: {}): Promise<implicitReturnType>;
    abstract xreservePostDelegateTransfer (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetTimestamp (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetCurrencies (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetMarkets (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetTickers (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetK (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetTradesHistory (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetFees (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetExchangeRates (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetExchangeRatesCurrency (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetBookMarket (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetKunaCodesCodeCheck (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetLandingPageStatistic (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetTranslationsLocale (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicGetTradesMarketHist (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostHttpTest (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostDepositChannels (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostWithdrawChannels (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostSubscriptionPlans (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostSendTo (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostConfirmToken (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostKunaid (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostWithdrawPrerequest (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostDepositPrerequest (params?: {}): Promise<implicitReturnType>;
    abstract v3PublicPostDepositExchangeRates (params?: {}): Promise<implicitReturnType>;
    abstract v3SignGetResetPasswordToken (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSignupGoogle (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSignupResendConfirmation (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSignup (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSignin (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSigninTwoFactor (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSigninResendConfirmDevice (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostSigninConfirmDevice (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostResetPassword (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPostCoolSignin (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPutResetPasswordToken (params?: {}): Promise<implicitReturnType>;
    abstract v3SignPutSignupCodeConfirm (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthWOrderSubmit (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrders (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersMarket (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersMarkets (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthApiTokensDelete (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthApiTokensCreate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthApiTokens (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSigninHistoryUniq (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSigninHistory (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDisableWithdrawConfirmation (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthChangePassword (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDepositAddress (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthAnnouncementsAccept (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthAnnouncementsUnaccepted (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthOtpDeactivate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthOtpActivate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthOtpSecret (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrderMarketOrderIdTrades (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersMarketHist (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersHist (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersHistMarkets (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthROrdersDetails (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthAssetsHistory (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthAssetsHistoryWithdraws (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthAssetsHistoryDeposits (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthRWallets (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMarketsFavorites (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMarketsFavoritesList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMeUpdate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMe (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthFundSources (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthFundSourcesList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthWithdrawResendConfirmation (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthWithdraw (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthWithdrawDetails (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthWithdrawInfo (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthPaymentAddresses (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDepositPrerequest (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDepositExchangeRates (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDeposit (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDepositDetails (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDepositInfo (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesCount (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesDetails (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesEdit (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesSendPdf (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodes (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesRedeemedByMe (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaCodesIssuedByMe (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthPaymentRequestsInvoice (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthPaymentRequestsType (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthReferralProgramWeeklyEarnings (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthReferralProgramStats (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMerchantPayoutServices (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMerchantWithdraw (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMerchantPaymentServices (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthMerchantDeposit (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthVerificationAuthToken (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaidPurchaseCreate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthDevicesList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSessionsList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSubscriptionsReactivate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSubscriptionsCancel (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSubscriptionsProlong (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSubscriptionsCreate (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthSubscriptionsList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostAuthKunaIdsList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostOrderCancelMulti (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePostOrderCancel (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePutAuthFundSourcesId (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivatePutAuthKunaCodesRedeem (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthMarketsFavorites (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthFundSources (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthDevices (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthDevicesList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthSessionsList (params?: {}): Promise<implicitReturnType>;
    abstract v3PrivateDeleteAuthSessions (params?: {}): Promise<implicitReturnType>;
    abstract publicGetDepth (params?: {}): Promise<implicitReturnType>;
    abstract publicGetKWithPendingTrades (params?: {}): Promise<implicitReturnType>;
    abstract publicGetK (params?: {}): Promise<implicitReturnType>;
    abstract publicGetMarkets (params?: {}): Promise<implicitReturnType>;
    abstract publicGetOrderBook (params?: {}): Promise<implicitReturnType>;
    abstract publicGetOrderBookMarket (params?: {}): Promise<implicitReturnType>;
    abstract publicGetTickers (params?: {}): Promise<implicitReturnType>;
    abstract publicGetTickersMarket (params?: {}): Promise<implicitReturnType>;
    abstract publicGetTimestamp (params?: {}): Promise<implicitReturnType>;
    abstract publicGetTrades (params?: {}): Promise<implicitReturnType>;
    abstract publicGetTradesMarket (params?: {}): Promise<implicitReturnType>;
    abstract privateGetMembersMe (params?: {}): Promise<implicitReturnType>;
    abstract privateGetDeposits (params?: {}): Promise<implicitReturnType>;
    abstract privateGetDeposit (params?: {}): Promise<implicitReturnType>;
    abstract privateGetDepositAddress (params?: {}): Promise<implicitReturnType>;
    abstract privateGetOrders (params?: {}): Promise<implicitReturnType>;
    abstract privateGetOrder (params?: {}): Promise<implicitReturnType>;
    abstract privateGetTradesMy (params?: {}): Promise<implicitReturnType>;
    abstract privateGetWithdraws (params?: {}): Promise<implicitReturnType>;
    abstract privateGetWithdraw (params?: {}): Promise<implicitReturnType>;
    abstract privatePostOrders (params?: {}): Promise<implicitReturnType>;
    abstract privatePostOrdersMulti (params?: {}): Promise<implicitReturnType>;
    abstract privatePostOrdersClear (params?: {}): Promise<implicitReturnType>;
    abstract privatePostOrderDelete (params?: {}): Promise<implicitReturnType>;
    abstract privatePostWithdraw (params?: {}): Promise<implicitReturnType>;
}