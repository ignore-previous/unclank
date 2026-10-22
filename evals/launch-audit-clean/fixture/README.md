# Tidepool 🦀

[![CI](https://github.com/tidepool-app/tidepool/actions/workflows/ci.yml/badge.svg)](https://github.com/tidepool-app/tidepool/actions/workflows/ci.yml)

Tide tables and low-tide alerts for the beaches near you, with a shared log of what people found.

## Run it

```
npm install
npm run dev
```

Tide data comes from the national tide service's public API. Set `TIDE_API_KEY` in `.env` first; without it the app shows a sample week.

## What works and what doesn't

- Tide tables and alerts work for any beach with a nearby tide station.
- Offline tables aren't done: the app needs a connection for now.
- The find log has no moderation yet, so it's invite-only.

## Licence

MIT, see LICENSE.
