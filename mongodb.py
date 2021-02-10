from pymongo import MongoClient
import csv
import os
import json

cluster = MongoClient("mongodb+srv://ermander:Pippotanto01!@cluster0.4xisp.mongodb.net/Odds?retryWrites=true&w=majority")
db = cluster["Odds"]
collection = db["Betaland"]

odd = {"_id": 3, "1": 1.5, "X": 3, "2": 4.5, "1X": 1.11, "12": 1.11, "2X": 1.11, "U25": 2}
collection.insert_one(odd)
results = collection.find({})
for result in results:
    print(result)
