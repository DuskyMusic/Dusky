"""
Copyright (c) 2022-2023 DuskyMusic
This is part of @DuskyXBot so don't change anything....
"""

from dusky.utils.http import post

BASE = "https://batbin.me/"


async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]
