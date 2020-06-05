# Example code for Elasticsearch score bitsets

This is the example to accompany "[Elasticsearch mapreduce aggregations that correlate multiple queries](https://jasonstitt.com/elasticsearch-mapreduce-multiple-queries)", showing you how to manipulate Lucene scores and scripted metric aggregations in Elasticsearch to efficiently obtain aggregates that compare or correlate multiple subqueries.

This is a flexible technique that can be used in various ways. The example here is simplistic and looks at one possible question, which is "how many documents match each of the subqueries but don't match any others". The example has only 3 simple subqueries, but I have used this approach in production with up to 20 very complex subqueries.

Please see the linked article and the comments in the source files for more explanation of what's happening.

## Usage

To just run the example:

```
pip3 install -r requirements.txt
./bin/start_server.sh
./bin/wait.py
./bin/sample_data.py
./bin/deploy_scripts.py
./bin/run_query.py
```

To clean up:

```
./bin/stop_server.sh
```

## Dependencies

* Docker
* Python 3
