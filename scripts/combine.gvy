// The combine script runs on each shard after map - basically shard-specific reduce
// https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-metric-agg-combine-context.html

// Since we're incrementing counters in map, there's nothing much to do here
// But despite what the docs say (they're wrong) combine script is required
return state.resultBuckets;
