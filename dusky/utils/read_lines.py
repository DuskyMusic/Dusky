"""
Copyright (c) 2022-2023 DuskyMusic
This is part of @DuskyXBot so don't change anything....
"""

from random import choice


async def random_line(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    return choice(data)
