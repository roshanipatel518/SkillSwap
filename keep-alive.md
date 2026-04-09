# Keep Backend Alive

## Problem
Render free tier sleeps after 15 minutes of inactivity. First request takes 30-60 seconds.

## Solutions

### Option 1: Use UptimeRobot (FREE)
1. Go to https://uptimerobot.com/
2. Sign up (free)
3. Add New Monitor:
   - Monitor Type: HTTP(s)
   - Friendly Name: SkillSwap Backend
   - URL: `https://skillswap-e7kv.onrender.com/health/`
   - Monitoring Interval: 5 minutes
4. Save

This will ping your backend every 5 minutes to keep it awake!

### Option 2: Use Cron-Job.org (FREE)
1. Go to https://cron-job.org/
2. Sign up (free)
3. Create new cronjob:
   - Title: SkillSwap Keep Alive
   - URL: `https://skillswap-e7kv.onrender.com/health/`
   - Schedule: Every 5 minutes
4. Save

### Option 3: Frontend Auto-Ping
Add this to your frontend to ping backend every 10 minutes when page is open.

Already added in code - check `frontend/js/app.js`

## Current Status
- First request: 30-60 seconds (cold start)
- Subsequent requests: Fast (< 1 second)
- After 15 min idle: Sleeps again

## Note
Free tier limitations:
- 750 hours/month (enough for 24/7 with keep-alive)
- Cold start on first request
- Upgrade to paid plan for instant response
