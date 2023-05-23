# Дан целочисленный массив цен, где цены[i] — цена i-го товара в магазине.
#
# В магазине действуют специальные скидки на товары. Если вы купите i-й товар, то получите скидку, эквивалентную ценам[j],
# где j — минимальный индекс, такой что j > i и цены[j] <= цены[i]. В противном случае вы не получите никакой скидки вообще.

class Discount:
    def __init__(self):
        self.price = [1, 3, 3, 3]
        self.price_new = []

    def pop(self):
        if self.empty():
            return None

    def fees(self):
        for i in range(len(self.price)):
            self.price_new.append(self.price[i])
            for j in range(len(self.price)):
                if i < j and self.price[i] >= self.price[j]:
                    self.price_new[i] = self.price_new[i] - self.price[j]
                    break;
        for index in range(len(self.price_new)):
            if self.price_new[index] == 0:
                self.price_new[index] = 1
        return self.price_new


q = Discount()

print(q.fees())
