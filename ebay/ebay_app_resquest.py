import requests


class EbayApp(object):
    def __init__(self):
        pass

    def ebay_request(self):
        ebay_url = 'https://apisd.ebay.com/experience/listing_details/v1/view_item?item_id=143338955601&modules=VLS&supported_partial_modules=VOLUME_PRICING&supported_ux_components=ADD_ON%2CALERT%2CALERT_CUSTOM%2CALERT_GUIDANCE%2CALERT_INLINE%2CAT_A_GLANCE%2CBANNER_IMAGE%2CBUY_BOX%2CCONDITION%2CCONDITION_CONTAINER%2CCUSTOMIZATION%2CEBAY_PLUS_PROMO%2CFITMENT%2CITEM_CARD%2CITEM_CONDENSED%2CITEM_CONDENSED_CONTAINER%2CITEM_STATUS_MESSAGE%2CKLARNA_FINANCING%2CMSKU_PICKER%2CPICTURES%2CPRODUCT_REVIEWS_SUMMARY%2CPRP_PRODUCT_DETAILS%2CQUANTITY%2CSECTIONS%2CSME%2CTITLE%2CUNANSWERED_Q%2CVALIDATE%2CVAS_HUB_V2%2CVAS_SPOKE_V2%2CVEHICLE_HISTORY%2CMERCH_CAROUSEL%2CMERCH_DISCOVERY%2CMERCH_GROUPED_CAROUSEL%2CMERCH_GRID%2CMERCH_PAGED_GRID%2CFEEDBACK_DETAIL_LIST%2CFEEDBACK_DETAIL_LIST_TABBED%2CFEEDBACK_DETAILED_SELLER_RATING_SUMMARY%2CALERT_FITMENT%2CFINDERS&inputoption=image.seller.avatar.200X200-jpg-l%2CEEK1%2Cebayplus%2Cdescription%2Csignals%2Cfitmentsvcv2%2Cincludedigital%2Cpaylogov1%2Capplepay%2Caddonv1%2Cshipbrand%2Csiooffer%2Csiooffer2%2Cincludetax&fieldgroups=addon%2Ccompact%2Cstatusmessage%2Ccompatibility%2Creview%2Cvehiclehistoryreport&supported_gadget_ux_components=BEST_OFFER_TOOL_TIP%2CTOOL_TIP_WITH_DISMISS%2CFIXED_COUPON_BANNER_V3%2CDRAWER_COUPON_BANNER%2CREWARDS_ENROLLMENT_MODAL%2CREWARDS_ACTIVATION_MODAL%2CREWARDS_REDEMPTION_MODAL%2CWIDGET_RESPONSE_MODAL%2CCOUPONS_LAYER%2CEBAY_PLUS_BANNER'
        headers = {
            "X-EBAY-C-ENDUSERCTX": 'contextualLocation=country%3DCN,deviceId=18358d999af.a9b1d2a.359cd.fffff267,deviceIdType=IDREF,userAgent=ebayUserAgent/"eBayIOS;6.78.0;iOS;15.4;Apple;iPhone14_2;%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8;390x844;3.0',
            "Authorization": "Bearer v^1.1#i^1#p^1#I^3#f^0#r^1#t^Ul42XzEwOjFFNzFCMUU2QjQ1MkY3REZGRDU3NjY3MzY2OTVDMzBEXzBfMSNFXjI2MA==",
        }
        r = requests.get(url=ebay_url, headers=headers)
        data = r.text
        print(r)

    def run_ebay_app_spider(self):
        self.ebay_request()


def run_ebayapp():
    run_ebayapp = EbayApp()
    run_ebayapp.run_ebay_app_spider()


if __name__ == '__main__':
    run_ebayapp()









