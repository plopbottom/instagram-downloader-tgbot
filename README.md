# Instagram Downloader Telegram Bot

A Telegram bot that downloads Instagram content — posts, reels, stories, highlights — instantly and for free.

## Supported Links

- `instagram.com/p/...` — Posts
- `instagram.com/reel/...` — Reels
- `instagram.com/tv/...` — IGTV
- `instagram.com/stories/username/id` — Single story
- `instagram.com/stories/username/` — All user stories
- `instagram.com/highlights/...` — Highlights
- `instagram.com/s/...` — Share links

Just send a link — the bot handles the rest.

---

## Build Your Own Instagram Bot

This bot is powered by **[HikerAPI](https://hikerapi.com)** — the fastest Instagram API on the market.

### Get 100 Free API Requests

**[Sign up with this link](https://hikerapi.com/p/hsazcgym)** and get **100 free requests** — no credit card required. Enough to build and test your own Instagram bot, scraper, or analytics tool.

What you get with HikerAPI:

- **Profiles, posts, stories, reels, highlights** — all media types
- **Followers, following, comments, likes** — full social graph
- **OSINT data** — emails, phones, locations, account age
- **No rate limits on paid plans** — scale as you grow
- **99.9% uptime** — production-ready infrastructure

> **[Get your free 100 requests here](https://hikerapi.com/p/hsazcgym)**

---

## Setup

1. Get a Telegram bot token from [@BotFather](https://t.me/BotFather)
2. Get a HikerAPI access key — **[100 free requests here](https://hikerapi.com/p/hsazcgym)**
3. Copy `default.env` to `.env` and fill in your tokens:
   ```
   cp default.env .env
   ```
4. Run with Docker Compose:
   ```
   docker compose up -d --build
   ```
