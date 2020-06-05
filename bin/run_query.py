#!/usr/bin/env python3

import os.path
import json
from elasticsearch import Elasticsearch

query_dir = os.path.join(os.path.dirname(__file__), '..')
client = Elasticsearch()

with open(os.path.join(query_dir, 'query.json')) as queryfile:
    search_doc = json.load(queryfile)
    print(json.dumps(client.search(search_doc), indent=2))
