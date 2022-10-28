#!/usr/bin/python3

import os

fnames = os.listdir(os.path.join(os.getcwd(), 'inputs'))

for fname in fnames:
    os.system(
        f'python3 tool/my_tool.py inputs/{fname} > results/output_{fname}'
    )