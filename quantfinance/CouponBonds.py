class CouponBonds:

  def __init__(self, principal, coupon, maturity, interest_rate):
    self.principal = principal
    self.coupon = coupon
    self.maturity = maturity
    self.interest_rate = interest_rate


  def present_value(self, x, n):
    return x / (1 + self.interest_rate)**n

  
  def calculate_price(self):
    price = 0
    # pv of coupon payments
    for i in range(1, self.maturity + 1):
      price = price + self.present_value(self.principal * self.coupon, i)
    # pv of the principal
    price = price + self.present_value(self.principal, self.maturity)
    return price

