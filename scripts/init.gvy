// The init script sets up data structures on each shard for map and combine to use
// https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-metric-agg-init-context.html

// Stores counts for each subquery
// In real life, probably needs to be dynamic; in this simple example we know we have 3 subqueries
state.resultBuckets = [0, 0, 0];
