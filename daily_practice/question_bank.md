# Question Bank

## Week 1

### List vs Dict
Q: Explain the difference between a list and a dict and when you'd use each.
A: A list is when something defined is attributed to a bunch of values through []. A dictionary is when something defined is attributed to key and value pairs through {}. In general a list is useful when that something defined is either a key or a value whereas a dictionary is for when hat something has both. ##a list holds values you access by position; a dict holds values you access by a named key.

### Top 3 by key (function from blank)
Q: Write a function that takes a list of dicts and returns the top 3 by a given key, from a blank file, no help.
A:

### JSON event counting (Week 1 check)
Q: From a blank file, write a function that opens a StatsBomb JSON match file and returns a count of each event type. No AI, no notes.
A:

## Week 2

### Top 3 players by minutes (SQL window function)
Q: Write, without hesitating, a query finding the top 3 players by minutes per team.
A:

### PARTITION BY vs ORDER BY
Q: State whether PARTITION BY comes before ORDER BY inside OVER(), without thinking.
A:

### LEFT JOIN row count
Q: Explain why a LEFT JOIN can increase your row count.
A:

### loc vs iloc
Q: What's the difference between .loc and .iloc, and when would they give different results?
A: .loc/.iloc are both about selecting rows within a single DataFrame, nothing to do with aligning two separate tables. Recall the actual distinction from Day 6: .loc[] selects by row label (whatever the index actually says, e.g. label 2), .iloc[] selects by positional order (the 3rd row, regardless of what its label says). They diverge specifically when a DataFrame's index has been reordered or filtered so that labels no longer match positions (like your sort_values() example)

### transform vs agg
Q: Explain groupby().transform() vs groupby().agg() and give a case where you need transform.
A: groupby allows grouping when there is a subgroup of something within a column. when we apply something to the groupby like sum or mean then it gives a value for that specific group. transform then gives a value for each row of that subgroup whereas agg gives a value for the subgriup in general not each individual row. 

### Chained assignment
Q: Explain why chained assignment is dangerous in pandas.
A:

### Week 2 check (full task)
Q: From blank, load a match, aggregate events per player with groupby, merge in the lineup to get minutes, and plot the top 10. Unaided.
A: