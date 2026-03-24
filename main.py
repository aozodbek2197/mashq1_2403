# 1-mashq
class Product:
    def __init__(self, name, price, quantity):
        if price <= 0:
            raise ValueError("Price 0 dan katta bo'lishi kerak")
        if quantity < 0:
            raise ValueError("Quantity manfiy bo'lmasligi kerak")

        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def sell(self, amount):
        if amount > self.quantity:
            raise ValueError("Yetarli mahsulot yo'q")
        self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount


p1 = Product("Laptop", 1000, 5)
p2 = Product("Phone", 500, 10)
p3 = Product("Keyboard", 50, 20)
p4 = Product("Monitor", 300, 7)

products = [p1, p2, p3, p4]

most_expensive = max(products, key=lambda p: p.total_price())

print("Eng katta total price:", most_expensive.name, most_expensive.total_price())
# 2-mashq
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount 0 dan katta bo'lishi kerak")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Balans yetarli emas")
        self.__balance -= amount

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Vali", 500)

acc1.transfer(acc2, 300)

print(acc1.owner, "balans:", acc1.get_balance())
print(acc2.owner, "balans:", acc2.get_balance())

try:
    acc1.withdraw(5000)
except ValueError as e:
    print("Xatolik:", e)
