#!/usr/bin/env python3
"""documented"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx

    logs = collection.count_documents({})
    print(f"{logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    stat = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{stat} status check")
