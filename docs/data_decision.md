# Data Decision - RoleFit

**What's available:** StatsBomb open data covers 80 competition-season entries (checked Sept 2026), spanning Bundesliga, Champions League, several World Cups, La Liga, Premier League, Serie A, Ligue 1, and several women's competitions. Most entries are thin curated subsets (1–40 matches), likely centred on specific high-profile players/teams rather than full league coverage.

**What we chose:** Four full 2015/16 seasons - Premier League (380 matches), La Liga (380), Serie A (380), Ligue 1 (377) - combined into one dataset (~1,517 matches, ~5.5M events).

**Why:** Only these four competition-seasons have genuine full-league coverage. Combining them gives a large, statistically robust player pool for clustering and Bayesian shrinkage, and enables a league-context angle (comparing a player's stats to their own league's baseline) that a single-league dataset wouldn't support. Event schema is consistent across all four leagues (confirmed by direct inspection of event types and attribute keys), so combining is a straightforward engineering task, not a data-reconciliation problem.

**What it costs us:**
- No consecutive-season data exists for any of these leagues, so next-season prediction is not possible - replaced with a within-season (first half → second half) split, a standard, defensible substitute.
- Combining four leagues requires per-league baseline normalisation throughout, adding engineering overhead versus a single-league approach.
- Dataset is from 2015/16, so no current transfer relevance - mitigated by using it as a backward-looking case study rather than a live recruitment tool.

**Event schema confirmed present:** Pass (length, angle, height, end location, body part, recipient, through_ball/cross/cut_back/switch/assist qualifiers), Shot (xG, end location, technique, body part, freeze frame), Carry (start/end location), under_pressure and counterpress flags on ~20% of events, play_pattern context, possession chain IDs.
