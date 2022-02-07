#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

import json
import logging

import requests
import retrying

logger = logging.getLogger(__name__)


class Proxy(object):
    def __init__(self):
        self.url = 'https://gimmeproxy.com/api/getProxy?post=true&supportsHttps=true&maxCheckPeriod=300'
        self.cur_proxy = None
        self.proxies = []
        self.result = []

    @retrying.retry(stop_max_attempt_number=3)
    def extract_proxy(self, url):
        re_ip_port_result = []
        logger.info("[-] Request url {url} ".format(url=url))
        for cc in range(30):
            try:
                headers = {
                    'User-Agent': "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) "
                                  "Chrome/21.0.1180.89 Safari/537.1'"
                }
                rp = requests.get(url, proxies=self.cur_proxy, headers=headers, timeout=10)

                jsonText = json.loads(rp.text)
                re_ip_port_result.append(jsonText["ip"] + ":" + jsonText["port"])
                # print(re_ip_port_result)
                if not re_ip_port_result:
                    raise Exception("empty")

            except Exception as e:
                logger.error("[-] Request url {url} error: {error}".format(url=url, error=str(e)))
                while self.proxies:
                    new_proxy = self.proxies.pop(0)
                    self.cur_proxy = {new_proxy['type']: "%s:%s" % (new_proxy['host'], new_proxy['port'])}
                    raise e
                else:
                    return []

        return [{'host': host, 'port': int(port), 'from': 'gimmeproxy'} for host, port in re_ip_port_result]

    def start(self):
        try:
            page_result = self.extract_proxy(self.url)
        except:
            return

        if not page_result:
            return

        self.result.extend(page_result)


if __name__ == '__main__':
    p = Proxy()
    p.start()

    for i in p.result:
        print(i)

    print(len(p.result))
