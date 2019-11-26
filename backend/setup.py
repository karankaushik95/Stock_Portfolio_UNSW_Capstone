# We will use this for bootstrapping
import os
import sys


def bootstrap():
    if not os.path.exists('db/users.db'):
        print("The file db/users.db does not exist.", file=sys.stderr)
        print("Run the runlocal script again.", file=sys.stderr)
        print("System exiting.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists('db/users'):
        print("The folder db/users does not exist.", file=sys.stderr)
        print("Run the runlocal script again.", file=sys.stderr)
        print("System exiting.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists('sqlite/'):
        print("The folder slite does not exist.", file=sys.stderr)
        print("Download the sqlite tools using the sqlite3_setup script.", file=sys.stderr)
        print("System exiting.", file=sys.stderr)
        sys.exit(1)
