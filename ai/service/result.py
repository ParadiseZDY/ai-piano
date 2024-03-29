# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 11:56 AM

class Content:
    def __init__(self, content, id, score, extra):
        self.content = content
        self.id = id
        self.score = score
        self.extra = extra


class Extra:
    def __init__(self, filetag, additionalContent):
        self.filetag = filetag
        self.additionalContent = additionalContent
