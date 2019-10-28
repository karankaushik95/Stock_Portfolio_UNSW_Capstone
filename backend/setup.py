# We will use this for bootstrapping
from os import path
import sys


def bootstrap():
    if not path.exists('db/tickers.db'):
        print("The file tickers.db does not exist. System exiting.", file=sys.stderr)

    if not path.exists('db/stock.db'):
        print("The file stock.db does not exist. System exiting.", file=sys.stderr)

    bootstrap_system()


def bootstrap_system():
    print("to satisfy the compiler")