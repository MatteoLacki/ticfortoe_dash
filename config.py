from datetime import date
import requests
import pandas as pd
import pathlib
from typing import List


def ask_for_paths(patterns: List[str], ip: str = "192.168.1.209", port: int = 8958):
    return requests.post(
        f"http://{ip}:{str(port)}/find", json={"query": patterns}
    ).json()


def ask_for_paths_df(*args, **kwargs):
    res = ask_for_paths(*args, **kwargs)
    res = pd.DataFrame(res.items())[[1, 0]]
    res.columns = ["pattern", "path"]
    return res


# ask_for_paths_df("G210115*.d")


def get_all_files():
    import json
    res = {"pattern": "*"}
    with open("/home/matteo/Projects/ticfortoe/all_paths.json", "r") as f:
        res["path"] = json.load(f)
    return pd.DataFrame(res)


def get_all_paths():
    import json
    res = {"pattern": "*"}
    with open("/home/matteo/Projects/ticfortoe/all_paths.json", "r") as f:
        res["path"] = json.load(f)
    res = pd.DataFrame(res)
    res = res.drop(columns="pattern")
    return res




instrument2pattern = {
    instrument: f"old/rawdata/{instrument}/[ARCHIVIERT/*/*.d|RAW/*.d]"
    for instrument in ("gutamine", "falbala", "obelix", "majestix")
}

def get_url(pattern, ip='192.168.1.209', port=8958):
    return rf"http://{ip}:{str(port)}/search/{pattern}"

def file2date(filename):
    return date.fromisoformat(f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}")


# instrument = 'gutamine'
def search_paths_on_instrument(instrument):
    try:
        url = get_url(instrument2pattern[instrument])
        paths = requests.get(url).json()
        res = []
        for path in paths:
            file = pathlib.Path(path).name
            try:
                date = file2date(file)
                row = {"file": file, "path": path, "date":date}
                res.append(row)
            except ValueError:
                print(path)
        res = pd.DataFrame(res)
        print(res)
        return res
    except KeyError:
        return pd.DataFrame(columns=("path",))



