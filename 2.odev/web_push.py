__author__ = 'Emre'

class WebPush():
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print('Push gönderildi!')

class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, trigger_page):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
        self.trigger_page = trigger_page

trigger_push = TriggerPush('Mobile', True, 1, 1607879442, 1607879475, 'English', 'Trigger Push', 'Cart Page')
trigger_push.send_push()

class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
        self.send_date = send_date

bulk_push = BulkPush('Mobile', True, 0, 1607879705, 1607879718, 'German', 'Bulk Push', 1607879773)
bulk_push.send_push()

class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, segment_name):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
        self.segment_name = segment_name

segment_push = SegmentPush('Desktop', False, 1, 1607879442, 1607879475, 'Chinese', 'Segment Push', 'Purchased Amount')
segment_push.send_push()

class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, price_info, discount_rate):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self, price_info, discount_rate):
        return price_info * (discount_rate / 100)


price_alert = PriceAlertPush('Desktop', False, 1, 1607879442, 1607879475, 'Russia', 'Price Alert Push', 100, 10)
price_alert.send_push()
price_alert.discountPrice(150,10)

class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, stock_info):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
        self.stock_info = stock_info

    def stockUpdate(self, stock_info):
        if(stock_info == True):
            stock_info == False
        else:
            stock_info == True

        return stock_info

instock = InstockPush('Desktop', True, 0, 1607879442, 1607879475, 'Poland', 'In Stock Push', False)
instock.stockUpdate(True)
instock.send_push()
