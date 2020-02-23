def bucket_sort(dataset, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in dataset:
        i = min(var // (max_num // n), n-1)
        # 把var添加到桶里面
        buckets[i].append(var)
        # 保持桶内顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j -
                                          1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_dataset = []
    for buc in buckets:
        sorted_dataset.extend(buc)
    return sorted_dataset


if __name__ == "__main__":
    import random
    dataset = [random.randint(0, 100) for i in range(100)]
    dataset = bucket_sort(dataset)
    print(dataset)
