import requests
from typing import List
import pandas as pd


def ask_for_paths(
    patterns: List[str],
    ip: str="192.168.1.209",
    port: int=8958
):
    return requests.post(f"http://{ip}:{str(port)}/find", json={"query":patterns}).json()



def ask_for_paths_df(*args, **kwargs):
    res = ask_for_paths(*args, **kwargs)
    res = pd.DataFrame(res.items())[[1,0]]
    res.columns = ["pattern","path"]
    return res

# ask_for_paths_df("G210115*.d")


def get_all_files():
    import json
    res = {"pattern":"*"}
    with open("/home/matteo/Projects/ticfortoe/all_paths.json",'r') as f:
        res["path"] = json.load(f)
    return pd.DataFrame(res)

    