import os
import pickle
import argparse
import json

parse = argparse.ArgumentParser()
parse.add_argument("-f", "--file", help="filename")
args = parse.parse_args()

nombre = args.file;

with open(f"{nombre}", "rb") as lector:
	datos_ = pickle.load(lector)

print("{}".format(json.dumps(datos_, indent=4, sort_keys=True)))