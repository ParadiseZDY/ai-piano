# -*- coding:utf-8 -*-
# Author:ZDY
# Date: 2024/3/29 11:39 AM


import json

import requests

from ai.service.result import Content, Extra


def buildRequest(topK, query):
    return {"topK": topK, "query": query}


headers = {
    "Content-type": "application/json",
    "Cookie": "ajs_user_id=8339806826d06be3e184c126da24bda506e10448; ajs_anonymous_id=d0a3c863-aed4-4c22-9965-6986d4685d4b; fp=d17dbb1f0922c7619c78cc234efccf20; YFD_U=1711096005189-46095; code_time_ec583190dcd12bca757dd13df10f59c3=1711425324; token_ec583190dcd12bca757dd13df10f59c3=ab0e95687334e717cee758611e6d77b3; code_phone_ec583190dcd12bca757dd13df10f59c3=0; sn_ec583190dcd12bca757dd13df10f59c3=392abf5fd34b576d1b7e9367e9c38bb9; SESS=I49UJrIwJWJDBwBPLRXWW%2BO8CTcOilUoVKPbKeCOZVJkDviXI%2BDlQS1WUH%2FxobpxuIDJ%2BjGqxidfo5TnqKoUWA%3D%3D; SESS_V2=AuPliuJVuC8rfOzR5RDEgM9%2BFUOrcjSvtMkJW763PdPUSrktCUS3KuA%2BpEZPVowOATXa9E2P5vpjcpFb4rHPJdtnKVTpMNvN1bA8aM57%2B%2FRgHLveEoRm5uYL14MW9XnYJDrgOX2fxenS7%2BLwZch1mSJclrpakLGU41IUhMmpduQ%3D; octopus_user=nhHSzjFkZOoEVBTi8Dxquj+Q4JLejuUoNDNMuygC9waHuqZMd2l0Ts9jBrwT3cqIwDfI3V48mRzdflSFQDdU/K3CoSTVKcy2v9DGe+rMzMe+HTtL/8IHbkpdiX37iqXZUycAqZLQdMkRU9axkNtX08d+knOFROCb; _ga=GA1.2.873067109.1670466929; _ga_62Z3H32JRP=GS1.1.1711592578.76.1.1711594341.0.0.0; redirect_url_ec583190dcd12bca757dd13df10f59c3=https%3A%2F%2Fjira.zhenguanyu.com%2Fsecure%2FRapidBoard.jspa%3FrapidView%3D907%26projectKey%3DZZ%26quickFilter%3D20856"
}


def queryWithVector(topK, query):
    vectorRequest = buildRequest(topK, query)
    url = "https://ai-platform-test.zhenguanyu.com/conan-chat-ai/admin/api/embedding/88"
    response = requests.post(url, headers=headers, data=json.dumps(vectorRequest))

    content_list = []
    embeddings = json.loads(response.text).get("embeddings", [])

    for embedding in embeddings:
        extra = embedding.get("extra", {})
        content_extra = Extra(extra.get("filetag", ""), extra.get("additionalContent", ""))
        content = Content(embedding.get("content", ""), embedding.get("id", ""), embedding.get("score", ""),
                          content_extra.__dict__)
        content_list.append(content.__dict__)

    return content_list
