# 🚀 Final Deployment Steps - Copy Paste Ready

## ✅ Backend Deployment (Render)

### Step 1: Create PostgreSQL Database
1. Render Dashboard → New + → PostgreSQL
2. Settings:
   - Name: `skillswap-db`
   - Database: `skillswap`
   - User: `skillswap`
   - Region: Oregon (US West)
   - Plan: **Free**
3. Click "Create Database"
4. **COPY** the "Internal Database URL" (starts with `postgresql://`)

---

### Step 2: Create Backend Web Service
1. Render Dashboard → New + → Web Service
2. Connect GitHub repo: `roshanipatel518/SkillSwap`
3. Settings:

**Name:**
```
skillswap-backend
```

**Region:**
```
Oregon (US West)
```

**Branch:**
```
main
```

**Root Directory:**
```
backend
```

**Runtime:**
```
Python 3
```

**Build Command:**
```
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate && python create_superuser.py
```

**Start Command:**
```
gunicorn skillswap.wsgi:application
```

**Plan:**
```
Free
```

---

### Step 3: Add Environment Variables

Click "Advanced" → Add Environment Variables:

```
PYTHON_VERSION=3.11.0
```

```
DEBUG=False
```

```
SECRET_KEY=django-insecure-skillswap-production-key-2024-change-this
```

```
DATABASE_URL=<PASTE-YOUR-POSTGRESQL-INTERNAL-URL-HERE>
```

```
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
```

```
CORS_ALLOWED_ORIGINS=https://skillswap-frontend-o1u5.onrender.com,http://localhost:3000
```

```
JWT_SECRET=skillswap-jwt-secret-key-2024-change-this
```

4. Click "Create Web Service"
5. Wait 10-15 minutes for deployment

---

### Step 4: Test Backend

Visit: `https://skillswap-backend.onrender.com/`

Should show:
```json
{
  "message": "SkillSwap API",
  "version": "1.0.0",
  "endpoints": {...}
}
```

Visit: `https://skillswap-backend.onrender.com/admin/`

Should show Django admin login page.

Login with:
- Username: `admin`
- Password: `admin123`

---

## 🎨 Frontend Deployment (Render)

### Step 1: Create Static Site
1. Render Dashboard → New + → Static Site
2. Connect GitHub repo: `roshanipatel518/SkillSwap`
3. Settings:

**Name:**
```
skillswap-frontend
```

**Branch:**
```
main
```

**Root Directory:**
```
frontend
```

**Build Command:**
```
(leave empty)
```

**Publish Directory:**
```
.
```

**Auto-Deploy:**
```
Yes (checked)
```

4. Click "Create Static Site"
5. Wait 2-3 minutes

---

### Step 2: Update Backend URL in Code

**IMPORTANT:** After backend deploys, update frontend code:

1. Go to GitHub repo
2. Edit `frontend/js/api-client.js`
3. Line 8, replace with your actual backend URL:

```javascript
this.baseURL = 'https://skillswap-backend.onrender.com/api';
```

4. Commit and push:
```bash
git add .
git commit -m "Update backend URL"
git push origin main
```

Frontend will auto-redeploy!

---

### Step 3: Update Backend CORS

1. Go to Render → Backend Service
2. Environment tab
3. Update `CORS_ALLOWED_ORIGINS` with your frontend URL:

```
https://skillswap-frontend-o1u5.onrender.com,http://localhost:3000
```

4. Save (backend will redeploy)

---

## ✅ Testing

### Test Backend:
```
https://skillswap-backend.onrender.com/
https://skillswap-backend.onrender.com/admin/
```

### Test Frontend:
```
https://skillswap-frontend-o1u5.onrender.com/
```

### Test Login:
1. Visit frontend URL
2. Click "Sign Up" or "Login"
3. Use admin credentials:
   - Username: `admin`
   - Password: `admin123`

---

## 🐛 Troubleshooting

### Issue: 404 on API calls

**Check:**
1. Backend URL in `api-client.js` is correct
2. Backend is running (visit backend URL)
3. Build command ran successfully (check Render logs)

**Fix:**
- Redeploy backend: Manual Deploy → Deploy latest commit
- Check logs for errors

### Issue: CORS Error

**Check:**
1. `CORS_ALLOWED_ORIGINS` includes frontend URL
2. Frontend URL is correct

**Fix:**
- Update environment variable
- Redeploy backend

### Issue: Database Error

**Check:**
1. PostgreSQL is connected
2. `DATABASE_URL` is set correctly
3. Migrations ran

**Fix:**
- Check Render logs
- Manually run: `python manage.py migrate`

---

## 📊 Admin Credentials

**Auto-created during deployment:**
- Username: `admin`
- Email: `admin@skillswap.com`
- Password: `admin123`

**⚠️ IMPORTANT:** Change password after first login!

---

## 💰 Cost

**Total: ₹0 (100% FREE)**

- Render PostgreSQL: Free (1GB)
- Render Web Service: Free (750 hours/month)
- Render Static Site: Free (100GB bandwidth)

---

## 🎉 Done!

Your SkillSwap platform is live!

- Frontend: https://skillswap-frontend-o1u5.onrender.com
- Backend: https://skillswap-backend.onrender.com
- Admin: https://skillswap-backend.onrender.com/admin/

Share and enjoy! 🚀
