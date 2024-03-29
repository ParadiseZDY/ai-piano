import random
import pandas as pd
import json


def topK(rendered_array, topNum, config):
    # 初始化对象数组
    topK = []

    for i in range(topNum):  # 我们用 num+1 因为 range() 是不包含上界的
        item = random.choice(config['TOP_100'])
        topK.append(item)

    # 返回对象数组
    return topK


# json转成csv
def json2csv():
    # 1. 读取 json 文件
    with open('../data/target.json', 'r') as file:
        json_data = json.load(file)
        # 加载json数据
        data = pd.read_json(json.dumps(json_data))
        # 将数据写入csv文件
        data.to_csv('../data/data.csv', index=False)


if __name__ == '__main__':
    json2csv()
