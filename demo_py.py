import json

j1 = {"type": "http", "country": "US", "export_address": ["unknown", "66.228.61.159"], "port": 8080,
      "from": "freeproxylist", "host": "66.228.61.159", "response_time": 0.73, "anonymity": "high_anonymous"}
j2 = {"type": "http", "country": "US", "export_address": ["208.52.157.86"], "port": 5555, "from": "proxylist",
      "host": "208.52.157.86", "response_time": 0.59, "anonymity": "transparent"}
j3 = {"type": "http", "country": "US", "export_address": ["38.94.111.208"], "port": 80, "from": "freeproxylist",
      "host": "38.94.111.208", "response_time": 0.88, "anonymity": "high_anonymous"}
j4 = {"type": "http", "country": "US", "export_address": ["38.94.111.208"], "port": 80, "from": "freeproxylist",
      "host": "38.94.111.208", "response_time": 0.88, "anonymity": "high_anonymous"}

dbjson = {}


def procew(js1):
    tps = js1['type'] + "_" + js1['anonymity']

    if tps not in dbjson.keys():
        dbjson[tps] = [js1]
    else:
        lis = dbjson[tps]
        print(type(lis))
        if js1 not in lis:
            lis.append(js1)
            dbjson[tps] = lis


if __name__ == '__main__':
    print("首个:" + json.dumps(dbjson))
    procew(j1)
    print("J1后:" + json.dumps(dbjson))
    procew(j2)
    print("J2后:" + json.dumps(dbjson))
    procew(j3)
    print("J3后:" + json.dumps(dbjson))
    procew(j4)
    print("J4后:" + json.dumps(dbjson))
