# Data Decision - RoleFit

**What's available:** StatsBomb open data covers 80 competition-season entries (checked Sept 2026), spanning Bundesliga, Champions League, several World Cups, La Liga, Premier League, Serie A, Ligue 1, and several women's competitions. Most entries are thin curated subsets (1–40 matches), likely centred on specific high-profile players/teams rather than full league coverage.

**What we chose:** Four full 2015/16 seasons - Premier League (380 matches), La Liga (380), Serie A (380), Ligue 1 (377) - combined into one dataset (~1,517 matches, ~5.5M events).

**Why:** Only these four competition-seasons have genuine full-league coverage. Combining them gives a large, statistically robust player pool for clustering and Bayesian shrinkage, and enables a league-context angle (comparing a player's stats to their own league's baseline) that a single-league dataset wouldn't support. Event schema is consistent across all four leagues (confirmed by direct inspection of event types and attribute keys), so combining is a straightforward engineering task, not a data-reconciliation problem.

**What it costs us:**
- No consecutive-season data exists for any of these leagues, so next-season prediction is not possible - replaced with a within-season (first half → second half) split, a standard, defensible substitute.
- Combining four leagues requires per-league baseline normalisation throughout, adding engineering overhead versus a single-league approach.
- Dataset is from 2015/16, so no current transfer relevance - mitigated by using it as a backward-looking case study rather than a live recruitment tool.

**Event schema confirmed present:** Pass (length, angle, height, end location, body part, recipient, through_ball/cross/cut_back/switch/assist qualifiers), Shot (xG, end location, technique, body part, freeze frame), Carry (start/end location), under_pressure and counterpress flags on ~20% of events, play_pattern context, possession chain IDs.

## Day 15 - Player join key: player_id over player_name

Original prototype (Days 12-13) keyed events and minutes-played dicts on player.name.
Switched to player.id before scaling to the full 1,517-match dataset, because name
strings risk collisions/inconsistent unicode across ~2,176 players spanning four
leagues. player.id is StatsBomb's dedicated unique identifier for exactly this reason.
Kept player_name as a descriptive column alongside player_id for readability.

## Day 15 - Gold aggregation join bug

First attempt joined player_minutes (one row per player-per-match) directly to
events (one row per individual event) on player_id + match_id. Because events
has many rows per player per match, this produced a many-to-one join that duplicated
each player's minutes_played once per matching event, inflating summed totals by
orders of magnitude (e.g. one player showed over 1,000,000 total minutes). Fixed by
pre-aggregating events to one row per player-per-match (shots, passes counted per
match) via a CTE before joining to player_minutes, restoring a 1-to-1 join.

## Day 16 - Minutes threshold: 900 minutes

Considered picking a round-number threshold (e.g. 900 min, about 10 matches, a common
convention) but wanted evidence from the actual dataset rather than an arbitrary
cutoff. Bucketed players by total_minutes and computed STDDEV(shots_per_90) per
bucket, expecting spread to be inflated at low minutes by sampling noise, then
decline and flatten once noise stops dominating (per the law of large numbers).

Result: STDDEV(shots_per_90) was <500: 1.67, 500-899: 0.88, 900-1499: 0.96,
1500-2499: 0.96, 2500+: 1.06. Spread drops sharply between <500 and 500-899,
then flattens from 500-899 onward. Chose 900 minutes as the threshold: a clean,
slightly conservative cutoff comfortably inside the stable range, rather than
exactly at the flattening point (which starts nearer 500).

Caveat acknowledged: this method assumes genuine talent variance is roughly
constant across minutes buckets. That assumption may not fully hold, since minutes
played correlates with player quality (fringe or rotation players get less time for
reasons connected to ability, not just chance). The slight uptick at 2500+ (1.06,
above the 900-2499 range) may reflect real variance among elite players rather
than the method breaking down. A more rigorous treatment of the small-sample
problem comes via Bayesian shrinkage (Week 7, H4), which this threshold decision
is a rough interim proxy for.

Bucket counts (total_minutes): under 500: 563 players, 500-899: 264, 900-1499: 363,
1500-2499: 566, 2500+: 429.
