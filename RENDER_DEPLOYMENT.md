# SkillSwap - Render Deployment Guide

## Complete Setup for Render + Netlify

---

## 🚀 Backend Deployment (Render)

### Step 1: Create Render Account
1. Go to https://render.com/
2. Sign up with GitHub

### Step 2: Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. Fill in:
   - **Name**: `skillswap-db`
   - **Database**: `skillswap`
   - **User**: `skillswap`
   - **Region**: Oregon (US West)
   - **Plan**: Free
3. Click "Create Database"
4. **IMPORTANT**: Copy the "Internal Database URL" (starts with `postgresql://`)

### Step 3: Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `roshanipatel518/SkillSwap`
3. Fill in:
   - **Name**: `skillswap-backend`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
     ```
   - **Start Command**:
     ```bash
     gunicorn skillswap.wsgi:application
     ```
   - **Plan**: Free

### Step 4: Add Environment Variables
In the "Environment" tab, add these variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `DEBUG` | `False` |
| `SECRET_KEY` | Generate using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DATABASE_URL` | Paste the Internal Database URL from Step 2 |
| `ALLOWED_HOSTS` | `.onrender.com,.netlify.app,localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | `https://skillswap-frontend.netlify.app,http://localhost:3000` |
| `JWT_SECRET` | Generate a random string (e.g., `your-jwt-secret-key-12345`) |

### Step 5: Deploy Backend
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Once deployed, copy your backend URL: `https://skillswap-backend.onrender.com`

### Step 6: Create Superuser (Admin)
1. Go to your service → "Shell" tab
2. Run these commands:
   ```bash
   cd backend
   python manage.py createsuperuser
   ```
3. Enter admin details when prompted

---

## 🎨 Frontend Deployment (Netlify)

### Step 1: Update Backend URL
Before deploying frontend, update the backend URL in your code:

1. Open `frontend/js/api-client.js`
2. Replace `https://skillswap-backend.onrender.com` with your actual Render backend URL
3. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update backend URL for production"
   git push origin main
   ```

### Step 2: Create Netlify Account
1. Go to https://www.netlify.com/
2. Sign up with GitHub

### Step 3: Deploy Frontend
1. Click "Add new site" → "Import an existing project"
2. Choose GitHub → Select `roshanipatel518/SkillSwap`
3. Configure:
   - **Base directory**: `frontend`
   - **Build command**: (leave empty)
   - **Publish directory**: `frontend`
4. Click "Deploy site"

### Step 4: Update Site Name (Optional)
1. Go to "Site settings" → "Site details"
2. Click "Change site name"
3. Enter: `skillswap-frontend` (or your preferred name)
4. Your site will be at: `https://skillswap-frontend.netlify.app`

### Step 5: Update CORS Settings
1. Go back to Render backend
2. Update `CORS_ALLOWED_ORIGINS` environment variable with your actual Netlify URL
3. Example: `https://skillswap-frontend.netlify.app,http://localhost:3000`
4. Click "Save Changes" (backend will redeploy)

---

## ✅ Testing Deployment

### Test Backend
1. Visit: `https://skillswap-backend.onrender.com/admin/`
2. Login with superuser credentials
3. You should see Django admin panel

### Test Frontend
1. Visit: `https://skillswap-frontend.netlify.app`
2. Sign up for a new account
3. Test login
4. Create a skill swap request
5. Test all features

---

## 🔧 Environment Variables Reference

### Backend (Render)

```bash
# Required
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=<generate-random-secret-key>
DATABASE_URL=<from-render-postgresql>
ALLOWED_HOSTS=.onrender.com,.netlify.app,localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=https://skillswap-frontend.netlify.app,http://localhost:3000
JWT_SECRET=<generate-random-jwt-secret>
```

### How to Generate SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Output example: `django-insecure-abc123xyz789...`

---

## 📝 Important Notes

### Free Tier Limitations
- **Render Free**: 
  - Backend sleeps after 15 minutes of inactivity
  - First request after sleep takes 30-60 seconds
  - 750 hours/month free
  
- **Netlify Free**:
  - 100GB bandwidth/month
  - Unlimited sites

### Database Backups
- Render Free PostgreSQL doesn't include automatic backups
- Manually backup using:
  ```bash
  pg_dump $DATABASE_URL > backup.sql
  ```

### Static Files
- Static files are served via WhiteNoise
- Run `python manage.py collectstatic` during build

### Media Files (User Uploads)
- For production, use cloud storage (AWS S3, Cloudinary)
- Current setup stores in local filesystem (will reset on redeploy)

---

## 🐛 Troubleshooting

### Backend Issues

**Error: "Application failed to respond"**
- Check Render logs for errors
- Verify `DATABASE_URL` is correct
- Ensure migrations ran successfully

**Error: "CORS policy blocked"**
- Update `CORS_ALLOWED_ORIGINS` in Render
- Include your Netlify URL
- Redeploy backend after changes

**Error: "Static files not loading"**
- Check if `collectstatic` ran in build command
- Verify `STATIC_ROOT` and `STATIC_URL` in settings

### Frontend Issues

**Error: "Failed to fetch"**
- Check if backend URL in `api-client.js` is correct
- Verify backend is running (visit backend URL)
- Check browser console for exact error

**Error: "404 on page refresh"**
- Netlify redirects should handle this
- Check `netlify.toml` is in root directory

---

## 🔄 Redeployment

### Backend Changes
1. Push changes to GitHub
2. Render auto-deploys from `main` branch
3. Or manually trigger: Render Dashboard → "Manual Deploy"

### Frontend Changes
1. Push changes to GitHub
2. Netlify auto-deploys from `main` branch
3. Or manually trigger: Netlify Dashboard → "Trigger deploy"

---

## 📞 Support

### Useful Links
- Render Docs: https://render.com/docs
- Netlify Docs: https://docs.netlify.com/
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/

### Common Commands

**View Render Logs:**
```bash
# In Render Dashboard → Logs tab
```

**Run Django Commands on Render:**
```bash
# In Render Dashboard → Shell tab
python manage.py <command>
```

**Clear Render Build Cache:**
```bash
# In Render Dashboard → Settings → Clear build cache
```

---

## 🎉 Success!

Your SkillSwap platform is now live!

- **Frontend**: https://skillswap-frontend.netlify.app
- **Backend**: https://skillswap-backend.onrender.com
- **Admin Panel**: https://skillswap-backend.onrender.com/admin/

Share your deployed app and start swapping skills! 🚀
