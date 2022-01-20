# -*- coding: utf-8 -*-

import click
from getproxy import GetProxy


@click.command()
@click.option('--in-proxy', help='Input proxy file')
@click.option('--out-proxy', help='Output proxy file')
@click.option('--token', help='github token')
def main(in_proxy, out_proxy, git_token):
    g = GetProxy(in_proxy, out_proxy,git_token)
    g.start()


if __name__ == "__main__":
    main()
