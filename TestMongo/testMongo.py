from pymongo import MongoClient
from proxy_pool.settings import MONGO_URL
from proxy_pool.utils.proxy_module import Proxy


if __name__ == "__main__":
    mongo_client = MongoClient(MONGO_URL)
    print(mongo_client)
    proxies =mongo_client['proxy_pool']['proxies']
    # proxytest = Proxy(ip='192.168.0.1', port='8885')
    # #proxies.insert_one(proxytest.__dict__)
    # print(proxies)
    #
    # reslt= proxies.count_documents({'_id': proxytest.ip})
    # print(reslt)
    # result=proxies.delete_one({'ip': proxytest.ip})
    # print(result.deleted_count)
    conditions = {
        'nick_type': -1,
        'protocol': -1
    }
    print(conditions)
    proxies = proxies.find(filter=conditions, limit=3)
    print(proxies)

    ret=[]
    for i in proxies:
        ret.append(i)
    print(ret)