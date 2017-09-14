#!/usr/bin/python
# encoding: utf-8

import sys
import os
from workflow import Workflow3
from workflow import Variables

log = None

def main(wf):
    snippet_body = os.getenv("snippetBody")

    # var_names = os.getenv("varNames").split()

    variables = {}

    # for var_name in var_names:
    #     variables.update({var_name : os.getenv(var_name)})

    v = Variables(**variables)

    v.config = {
        "clipboardtext" : snippet_body
    }

    print(v)

if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])

    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))
