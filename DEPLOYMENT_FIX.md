# 🚀 SkillSwap Deployment Fix Guide

## Issues Fixed:
1. ✅ Build script error handling
2. ✅ Static files collection with --clear flag
3. ✅ CORS configuration for wildcard domains
4. ✅ Proper ALLOWED_HOSTS configuration
5. ✅ Gunicorn workers and timeout settings
6. ✅ Root directory specification in render.yaml

---

## 📋 Render Deployment Steps (Updated)

### Step 1: Create PostgreSQL Database
1. Go to Render Dashboard → New + → PostgreSQL
2. Settings:
   - Name: `skillswap-db`
   - Database: `skillswap`
   - User: `skillswap`
   - Region: Oregon (US West)
   - Plan: Free
3. Click "Create Database"
4. **Copy the Internal Database URL**

---

### Step 2: Deploy Backend

#### Option A: Using render.yaml (Recommended)
1. Push code to GitHub
2. Render Dashboard → New + → Blueprint
3. Connect repository
4. Render will auto-detect `render.yaml`
5. Add environment variables:
   - `SECRET_KEY`: Generate using Python
   - `JWT_SECRET`: Any random string
   - `DATABASE_URL`: From Step 1
   - `CORS_ALLOWED_ORIGINS`: Your frontend URL
6. Click "Apply"

#### Option B: Manual Setup
1. Render Dashboard → New + → Web Service
2. Connect GitHub repo
3. Settings:
   - **Name**: `skillswap-backend`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: Python 3
   - **Build Command**:
     ```bash
     pip install --upgrade pip && pip install -r requirements.txt && python manage.py collectstatic --no-input --clear && python manage.py migrate --no-input && python create_superuser.py
     ```
   - **Start Command**:
     ```bash
     gunicorn skillswap.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
     ```

4. Environment Variables:
   ```
   PYTHON_VERSION=3.11.0
   DEBUG=False
   SECRET_KEY=<generate-random-key>
   DATABASE_URL=<from-postgresql>
   ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com,http://localhost:3000
   JWT_SECRET=<random-string>
   ```

---

### Step 3: Deploy Frontend (Static Site)

1. Render Dashboard → New + → Static Site
2. Connect GitHub repo
3. Settings:
   - **Name**: `skillswap-frontend`
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: (leave empty)
   - **Publish Directory**: `.`

---

### Step 4: Update Frontend Backend URL

After backend deploys, update `frontend/js/api-client.js`:

```javascript
// Line 10-11
if (hostname.includes('onrender.com')) {
    this.baseURL = 'https://YOUR-BACKEND-NAME.onrender.com/api';
}
```

Replace `YOUR-BACKEND-NAME` with your actual backend service name.

---

### Step 5: Update Backend CORS

Go to backend service → Environment → Update:

```
CORS_ALLOWED_ORIGINS=https://your-frontend-name.onrender.com,http://localhost:3000
```

Save and redeploy.

---

## 🔍 Testing

### Test Backend:
```
https://your-backend.onrender.com/admin/
```

Login:
- Username: `admin`
- Password: `admin123`

### Test API:
```
https://your-backend.onrender.com/api/
```

### Test Frontend:
```
https://your-frontend.onrender.com/
```

---

## 🐛 Common Issues & Fixes

### Issue 1: Build Failed
**Error**: `ModuleNotFoundError` or `ImportError`

**Fix**:
- Check `requirements.txt` has all dependencies
- Verify Python version is 3.11.0
- Check build logs for specific missing package

### Issue 2: Static Files Not Loading
**Error**: 404 on CSS/JS files

**Fix**:
- Ensure `collectstatic` ran successfully
- Check `STATIC_ROOT` and `STATIC_URL` in settings
- Verify WhiteNoise is in MIDDLEWARE

### Issue 3: CORS Error
**Error**: `Access to fetch has been blocked by CORS policy`

**Fix**:
- Update `CORS_ALLOWED_ORIGINS` with exact frontend URL
- No trailing slash in URLs
- Redeploy backend after changes
- Clear browser cache (Ctrl + Shift + Delete)

### Issue 4: Database Connection Error
**Error**: `could not connect to server`

**Fix**:
- Verify `DATABASE_URL` is set correctly
- Check PostgreSQL database is running
- Ensure database is in same region as backend

### Issue 5: Application Timeout
**Error**: `Application failed to respond`

**Fix**:
- Increased timeout to 120 seconds in gunicorn
- Added 2 workers for better performance
- Check logs for actual error

---

## 📊 Generate SECRET_KEY

Run this locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy output and use as `SECRET_KEY` environment variable.

---

## 🔄 Redeploy

### Backend:
```
Render Dashboard → Backend Service → Manual Deploy → Deploy latest commit
```

### Frontend:
```
Render Dashboard → Frontend Static Site → Trigger deploy
```

---

## 📝 Checklist

Before going live:

- [ ] PostgreSQL database created
- [ ] Backend deployed successfully
- [ ] Frontend deployed successfully
- [ ] Backend URL updated in frontend code
- [ ] CORS origins updated in backend
- [ ] Admin login works
- [ ] API endpoints responding
- [ ] Frontend can login/signup
- [ ] Browser cache cleared
- [ ] Test on different browsers

---

## 💡 Pro Tips

1. **First Deploy**: Takes 10-15 minutes
2. **Subsequent Deploys**: 3-5 minutes
3. **Free Tier Sleep**: Backend sleeps after 15 min inactivity
4. **Wake Up Time**: First request takes 30-60 seconds
5. **Logs**: Always check logs for errors
6. **Environment Variables**: Changes trigger redeploy

---

## 🎉 Success!

Your app should now be live at:
- Backend: `https://your-backend.onrender.com`
- Frontend: `https://your-frontend.onrender.com`
- Admin: `https://your-backend.onrender.com/admin/`

Happy deploying! 🚀
