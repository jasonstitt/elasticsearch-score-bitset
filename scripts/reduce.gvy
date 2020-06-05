// The reduce script runs at the end and produces the final aggregation result
// https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-metric-agg-reduce-context.html

// Total counts for each subquery
// In real life, probably needs to be dynamic; in this simple example we know we have 3 subqueries
ArrayList resultBuckets = [0, 0, 0];

// In real life this could be a variable number of queries
int numQueries = 3;

// states is a list all the return values from combine
// Docs say states is a Map. It's not. It's a List. Docs are wrong.
for (shardResults in states) {
  for (int i = 0; i < numQueries; ++i) {
    resultBuckets[i] += shardResults[i];
  }
}

return resultBuckets;
