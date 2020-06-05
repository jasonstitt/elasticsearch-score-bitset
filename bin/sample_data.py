#!/usr/bin/env python3

from itertools import permutations
from elasticsearch import Elasticsearch, helpers


def sample_data(n):
    for apples, bananas, pears in permutations(range(n), 3):
        yield {'_index': 'bitset_example', 'apples': apples, 'bananas': bananas, 'pears': pears}


for _ in helpers.parallel_bulk(Elasticsearch(), sample_data(100)):
    pass
