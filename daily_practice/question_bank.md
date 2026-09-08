# Question Bank

Answer these out loud, from memory, no notes, during the daily N1/N3 drill block.
If an answer comes out as recognition rather than explanation, leave it in rotation.

---

## Week 1 — Python foundations

- From a blank file, write a function that opens a StatsBomb JSON match file and returns a count of each event type.

## Week 2 — pandas, SQL joins

- Explain `groupby().transform()` vs `groupby().agg()` and give a case where you need `transform`.
- Explain list vs dict and when you'd use each.
- Explain `loc` vs `iloc`.
- From blank: load a match, aggregate events per player with `groupby`, merge in the lineup to get minutes, and plot the top 10 — unaided.

## Week 3 — SQL window functions

- Write, from memory in under 3 minutes, a window-function query returning each team's top 3 players by minutes. If you hesitate on syntax, drill it again.
- Explain the difference between `RANK`, `DENSE_RANK`, and `ROW_NUMBER`.
- Explain what `PARTITION BY` does differently from `GROUP BY`.
- Why can't you filter on a window function result using `WHERE` in the same query it's defined in? (Execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.)
- Explain cohort retention vs churn, conceptually.
- What does `COUNT(DISTINCT player)` do differently from plain `COUNT(player)`?

---

## Module A — Python foundations
- Write a function that takes a list of dicts and returns the top 3 by a given key, from a blank file, no help.
- Explain the difference between a list and a dict and when you'd use each.

## Module B — SQL
- Write, without hesitating, a query finding the top 3 players by minutes per team.
- State whether `PARTITION BY` comes before `ORDER BY` inside `OVER()` without thinking.
- Explain why a `LEFT JOIN` can increase your row count.

## Module C — NumPy, pandas, visualisation
- Explain `groupby().transform()` vs `groupby().agg()` and give a case where you need `transform`.
- Explain why chained assignment is dangerous.

## Module D — Statistics and inference
- Explain a p-value to a non-statistician in two sentences without saying "probability the null is true."
- State the assumptions of linear regression.
- Explain why a player with 3 goals from 2 shots is not a good finisher.

## Module E — Core ML: regression and classification
- Derive the logistic regression gradient.
- Explain why cross-entropy and not MSE for classification.
- Given AUC 0.85 but terrible calibration, explain what that means and when it matters.

## Module F — Trees, ensembles, interpretability
- How does a tree choose a split?
- Bagging vs boosting — what is each correcting for?
- Why is impurity importance misleading with correlated features? (Directly relevant: football stats are heavily correlated.)

## Module G — Unsupervised learning and similarity
- Why must you scale before k-means and before PCA?
- What does PC1 actually represent?
- When is cosine better than Euclidean?

## Module H — Bayesian methods and uncertainty
- Explain shrinkage to a football scout in plain English.
- Why does a Bayesian approach help when you have 200 minutes of data on a player?
- What's the difference between a credible and a confidence interval?

## Module I — Neural networks
- Walk through backprop for a 2-layer network on a whiteboard.
- What is vanishing gradient?
- Why would you choose LightGBM over a neural net for a 5,000-row tabular problem?

## Module J — NLP, LLMs and agentic systems
- How do you stop an LLM returning malformed JSON?
- How would you evaluate whether an LLM's output is any good?
- What makes something an agent rather than a single API call?

## Module K — Engineering and delivery
- Why does your pipeline have tests?
- What happens if someone clones your repo — can they reproduce your results, and how do you know?

## Module L — Cloud and big data literacy
- When would you reach for Spark instead of pandas?
- What's model drift and how would you detect it?
- Explain the difference between a data lake and a warehouse to a non-technical client.

## Module M — Communication and consulting skills
(No standalone Checks listed — covered via M3/M4 deliverables: exec summary, 5-min presentation.)

---

## Project-specific (from today's sessions)

- Why does the flat events table use `match_id` as a hardcoded literal for now, and what will need to change when scaling to multiple matches?
- Explain what `os.path.expanduser`, `os.makedirs`, and `.write_parquet` each do in the P1 save step.
- Why is Parquet preferred over CSV for this project?
