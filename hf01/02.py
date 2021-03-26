products = [
  [input("name: "), int(input("price: "))]
  for i in range(4)
]

names = (product[0] for product in products)
for name in sorted(names):
  print(name, end=' ')
print()

prices = [product[1] for product in products]
print(sum(prices) / len(products))
print(max(prices) - min(prices))
