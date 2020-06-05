// The map script is run for every document that matches the search and updates the state
// https://www.elastic.co/guide/en/elasticsearch/painless/current/painless-metric-agg-map-context.html

// Lucene score is a double
int score = (int)(_score + 0.1);

// In real life this could be a variable number of queries
int numQueries = 3;

// Check each bit in turn
// For larger real world cases you could generate a lookup table in the init script
for (int i = 0; i < numQueries; ++i) {
  int mask = 1 << i;
  // Look for exclusive matches for this example
  // Intersections, deduped first match and other cases are done in the same general way, just change this loop
  if ((score & mask) > 0 && (score - mask) == 0) {
    state.resultBuckets[i]++;
    break;
  }
}
