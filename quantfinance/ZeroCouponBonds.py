class ZeroCouponBonds:

    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate

    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)


#amount = float(input("Principal Amount : "))
#mat = float(input("Maturity : "))
#int_rate = float(input("Market Rate of Interest : "))


#if __name__ == "__main__":
#    bond = ZeroCouponBonds(amount, mat, int_rate)
#    print(bond.calculate_price())