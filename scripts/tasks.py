#!/usr/bin/python
from fabric.api import settings, run
import sys


def connect():
    return settings(warn_only=True, host_string='icarus.zz50.co.uk',
                    user='dave', output_prefix=False)


if len(sys.argv) > 1 and sys.argv[1] == 'i':
    with connect():
        run('sudo docker exec -it tasks.zz50.co.uk bash')
else:
    with connect():
        run('sudo docker exec -it tasks.zz50.co.uk task %s ' %
            (' '.join(sys.argv[1:]), ))
