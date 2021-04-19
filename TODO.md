# TODO
## SQL statements
- [done] Write initial statements for overall statistics
- [done] Write initial statements for geography based statistics
- [done] Write initial statements for URL based statistics
- [done] Write initial statements for URL read next statistics
- [done] Write initial statements for event statistics
- [done] Add time constraints so that the entire BQ table isn't being queried all at once
- [] Write create statements for the PostgreSQL tables (can add indexes later)
- [] Make changes needed to the worker worker outlined in the section below
- [] Create a server that runs PostgreSQL, and also add PostgREST and python cronjobs to it
- [] Write CF Worker scripts to make requests from the PostgreSQL server

## Ingest Worker
- Ensure that compute time is always less than 50ms for the `ingest` worker. Maybe by moving useragent parsing to the client?
- Add a session_referrer_class (Search, Social, Direct, Forum, Other)
- Add city type (Tier 1, Tier 2, other attributes) to either Worker or dashboard code -- to figure out
- Add affluence index calculation to worker code. Likely through KV?