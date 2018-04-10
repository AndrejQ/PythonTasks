def banknotes(values, price):
    for i in values:
        if i > price:
            values.remove(i)
    papers = [price + 1] * (1 + max(values))
    for i in values:
        papers[i] = 1

    for i in range(1 + max(values), price + 1):
        papers.append(1 + min([papers[i - j] for j in values]))

    return -1 if papers[price] > price else papers[price]


values = [30, 1, 14]
price = 29

papers = banknotes(values, price)

print(papers)
