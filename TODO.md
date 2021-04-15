# TODO
## SQL statements
- [done] Write statements for overall statistics
- [done] Write statements for geography based statistics
- [] Write statements for URL based statistics
- [] Write statements for URL read next statistics
- [] Write statements for event statistics

## Worker
- Ensure that compute time is less than 50ms. Maybe by moving useragent parsing to the client?
- Add a session_referrer_class (Search, Social, Direct, Forum, Other)
- Add city type (Tier 1, Tier 2, other attributes) to either Worker or dashboard code -- to figure out
- Add affluence index calculation to worker code. Likely through KV?