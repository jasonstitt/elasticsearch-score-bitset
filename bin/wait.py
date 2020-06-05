#!/usr/bin/env python3

from elasticsearch import Elasticsearch

client = Elasticsearch()
ready = False

try:
    while not ready:
        ready = client.ping()
except KeyboardInterrupt:
    pass
