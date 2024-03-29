# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 2:13 PM

import pandas as pd
import json


def json2csv(json_data):
    # 加载json数据
    data = pd.read_json(json_data)

    # 将数据写入csv文件
    data.to_csv('data.csv', index=False)


if __name__ == '__main__':
    # 1. 读取 json 文件
    with open('../data/target.json', 'r') as file:
        json_data = json.load(file)
        json2csv(json.dumps(json_data))
