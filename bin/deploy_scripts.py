#!/usr/bin/env python3

import os.path
import json
from elasticsearch import Elasticsearch

script_names = ['init', 'map', 'combine', 'reduce']
script_dir = os.path.join(os.path.dirname(__file__), '../scripts')
client = Elasticsearch()

for name in script_names:
    # So about those .gvy extensions... painless syntax highlighting basically doesn't exist,
    # but it's close enough to Groovy...
    file_path = os.path.join(script_dir, name + '.gvy')
    source = open(file_path).read()
    es_script_name = 'bitset_example_' + name
    script_data = {'script': {'lang': 'painless', 'source': source}}

    # Pretty sure context IDs aren't actually documented anywhere, but you can get a list from the API:
    # GET /_scripts/painless/_context
    # (Pretty sure that API endpoint isn't documented either...)
    context = 'aggs_' + name
    client.put_script(id=es_script_name, body=script_data, context=context)
    print(json.dumps(client.get_script(id=es_script_name), indent=2))

# Cache is not invalidated by using an updated script. With a static dataset you will get stale results
client.indices.clear_cache(index='*')
