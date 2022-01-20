# -*- coding: utf-8 -*-

import click
from getproxy import GetProxy


@click.command()
@click.option('--in-proxy', help='Input proxy file')
@click.option('--out-proxy', help='Output proxy file')
@click.option('--token', help='github token')
def main(in_proxy, out_proxy):
    g = GetProxy(in_proxy, out_proxy)
    g.start()

@click.command()
@click.option('--in-proxy', help='Input proxy file')
@click.option('--out-proxy', help='Output proxy file')
@click.option('--token', help='github token')
def main(in_proxy, out_proxy, token):
    if token != "":
        print("token 有值！！！")
    g = GetProxy(in_proxy, out_proxy)
    g.start()

if __name__ == "__main__":
    main()
