# 每个商品的元组表示(价格,重量)
goods = [(60, 10), (100, 20), (120, 30)]


def fractional_backpack(goods, w):
    # 单位重量里面最值钱的排序
    goods.sort(key=lambda x: x[0]/x[1], reverse=True)
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
            total_v += prize
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m, total_v


if __name__ == "__main__":
    # print(fractional_backpack(goods, 50))
    pass
