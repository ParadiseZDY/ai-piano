import random

def topK(rendered_array, topNum, config):
    # 初始化对象数组
    topK = []

    for i in range(topNum):  # 我们用 num+1 因为 range() 是不包含上界的
        item = random.choice(config['TOP_100'])
        topK.append(item)

    # 返回对象数组
    return topK