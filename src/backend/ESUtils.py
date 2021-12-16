from flask import request
from settings import parameters, bool_map
import time
import json

def reformat_title(args):
    args["from"] = int(args["from"])
    args["size"] = int(args["size"])

    args["filter_year"] = bool_map[args["filter_year"]]
    args["s_year"] = int(args["s_year"])
    args["e_year"] = int(args["e_year"])

reformat_map = {
    "TITLE": reformat_title,
}

def gen_query():
    res = {}
    args = request.args
    for key in args:
        res[key] = args[key]
    reformat_map[res["type"]](res)
    # print("query", json.dumps(res, indent=1))
    return res
