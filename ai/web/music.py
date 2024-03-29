# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 10:29 AM
import json
import random

from flask import Flask, request, jsonify

from ai.service import search

app = Flask(__name__)


def init_app():
    # 1. 读取 json 文件
    with open('../data/target.json', 'r') as file:
        data = json.load(file)

    # 2. 排序 json 文件
    sorted_data = sorted(data, key=lambda x: x['likeCount'] + x['degree'] * 10 - x['unlikeCount'], reverse=True)

    # 3. 取前100个
    top_100 = sorted_data[:100]

    # 将结果保存为全局变量
    app.config['TOP_100'] = top_100
    print("App initialization complete.")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/rand')
def rand_item():
    # 从 TOP_100 中随机抽取一个对象
    item = random.choice(app.config['TOP_100'])
    # 将对象转为 JSON 格式并返回
    return jsonify(item)


# 相似 top k
@app.route('/similar', methods=['POST'])
def post_json():
    data = request.get_json(force=True)

    # 这里你可以处理你的数据
    print(data)

    retrunData = {}
    retrunData['rendered'] = data['rendered'];

    # 返回一个响应
    return jsonify({'code': 200, 'data': retrunData}), 200


# top k
@app.route('/top')
def top():
    topK = request.args.get("topK", 10)
    resp = search.queryWithVector(topK, request.args.get("query"))
    return jsonify(resp)


if __name__ == '__main__':
    init_app()
    app.run(host='0.0.0.0', port=9999, debug=True)
