class AliPay:

    def pay(self):
        print("通过支付宝消费")


class WX:

    def pay(self):
        print("通过微信")


class Order(object):

    def account(self, pay_obj):
        pay_obj.pay()


order = Order()

a = AliPay()
b = WX()

order.account(a)
order.account(b)
