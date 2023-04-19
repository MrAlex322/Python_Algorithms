# Даны массив arr, каждый из элементов массива хэшмапа.
#
# Например:
# arr = [{email: “vas@gmail.com”, max_amount: 1}, {email: “gg@gmail.com”, max_amount: 123} … ]
#
# Требуется найти
# самый популярный email в массиве
# максимальное и минимальное значение max_amount
# отсортировать массив в порядке убывания max_amount, при этом избавившись от email дубликатов


from collections import Counter


class EmailAnalyzer:
    def __init__(self, arr):
        self.arr = arr

    def find_most_frequent_email(self):
        emails = [item["email"] for item in self.arr]
        email_count = Counter(emails)
        max_email = email_count.most_common(1)[0][0]
        return max_email

    def find_sum_values(self):
        max_amounts = [item["max_amount"] for item in self.arr]
        sum_values = (min(max_amounts), max(max_amounts))
        return sum_values

    def sort_by_max_amount(self):
        sorted_arr = sorted(self.arr, key=lambda item: item["max_amount"], reverse=True)
        unique_emails = set()
        new_arr = []
        for item in sorted_arr:
            email = item["email"]
            if email not in unique_emails:
                new_arr.append(item)
                unique_emails.add(email)
        return new_arr


# Пример использования класса
arr = [
    {"email": "vas@gmail.com", "max_amount": 1},
    {"email": "gg@gmail.com", "max_amount": 123},
    {"email": "test@gmail.com", "max_amount": 10},
    {"email": "vas@gmail.com", "max_amount": 5},
    {"email": "xyz@gmail.com", "max_amount": 45},
    {"email": "gg@gmail.com", "max_amount": 12},
]

analyzer = EmailAnalyzer(arr)

most_frequent_email = analyzer.find_most_frequent_email()
print("Самый популярный email в массиве: ", most_frequent_email)

sum_values = analyzer.find_sum_values()
print("Минимальное и максимальное значение max_amount: ", sum_values)

sorted_arr = analyzer.sort_by_max_amount()
print("Массив, отсортированный по убыванию max_amount: ")
for item in sorted_arr:
    print(item)

