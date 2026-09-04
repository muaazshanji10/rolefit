# RoleFit — Project Brief

**Business question:** Given a club's stated tactical requirement, which available players best fit - and which of their current output is likely to persist rather than being small-sample noise?

**Stakeholder:** A club's recruitment analyst, briefing scouts and sporting director on shortlist candidates.

**Decision supported:** Which players to prioritise for scouting/pursuit given a defined tactical need and minutes budget.

**Success criteria:** A working end-to-end pipeline (raw event data → features → role clusters → shrunk metrics → predictive model → natural-language interface → deployed app) that produces defensible, interpretable shortlists, with honest reporting of where the model beats or fails to beat a naive baseline.

**Scope - in:**
- Four full 2015/16 top-five European league seasons (Premier League, La Liga, Serie A, Ligue 1), combined with per-league baseline adjustment for cross-league comparability
- Role discovery via clustering
- Uncertainty via bootstrap + empirical Bayes shrinkage
- Within-season (first half → second half) prediction, since consecutive full seasons aren't available
- Interpretability via SHAP
- Natural-language brief → structured query interface
- Case study validation: take a real, publicly reported tactical need a team had going into 2016/17, feed it into RoleFit's own interface, and compare RoleFit's recommended profile against what the team actually did

**Scope — out:**
- Season-over-season prediction (data doesn't support it - only one full season per league is available)
- Player transfer-and-performance tracking into new clubs/seasons (later-season data is thin, curated subsets, not full squad coverage - may be included opportunistically as a bonus if a specific high-profile transfer happens to have follow-on data available)
- Injury history, contract/wage data, tactical/formation fit beyond statistical profile
- Video or physical/athletic data - event-data only
