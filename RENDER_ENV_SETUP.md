# Render Environment Variables Setup

## 🔧 Backend Environment Variables

Render Dashboard → Your Backend Service → Environment tab mein yeh add karo:

### Required Variables:

```bash
# Python Version
PYTHON_VERSION=3.11.0

# Django Settings
DEBUG=False
SECRET_KEY=django-insecure-your-random-secret-key-here-change-this

# Database (Automatically set by Render PostgreSQL)
DATABASE_URL=<automatically-set-by-render>

# Allowed Hosts (IMPORTANT!)
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1

# CORS Settings (CRITICAL - Add your frontend URL!)
CORS_ALLOWED_ORIGINS=https://skillswap-frontend-o1u5.onrender.com,http://localhost:3000

# JWT Secret
JWT_SECRET=your-jwt-secret-key-change-this-to-random-string
```

---

## 🎯 Frontend URL Update

### Step 1: Get Your Backend URL
1. Render Dashboard → Backend Service
2. Copy URL (e.g., `https://skillswap-backend-xyz.onrender.com`)

### Step 2: Update Frontend Code
Edit `frontend/js/api-client.js` line 8:

```javascript
this.baseURL = 'https://YOUR-ACTUAL-BACKEND-URL.onrender.com/api';
```

Replace `YOUR-ACTUAL-BACKEND-URL` with your actual backend service name!

### Step 3: Update Backend CORS
Render Dashboard → Backend Service → Environment:

Update `CORS_ALLOWED_ORIGINS` with your frontend URL:
```
https://your-frontend-url.onrender.com,http://localhost:3000
```

---

## 🔍 How to Find Your URLs

### Backend URL:
1. Render Dashboard
2. Click on backend service
3. Top of page shows: `https://skillswap-backend-xyz.onrender.com`

### Frontend URL:
1. Render Dashboard
2. Click on frontend static site
3. Top of page shows: `https://skillswap-frontend-abc.onrender.com`

---

## ✅ Checklist

- [ ] Backend `CORS_ALLOWED_ORIGINS` includes frontend URL
- [ ] Frontend `api-client.js` has correct backend URL
- [ ] Both services redeployed after changes
- [ ] Browser cache cleared (Ctrl + Shift + Delete)
- [ ] Test login on frontend

---

## 🐛 Debugging Token Issue

### Check Browser Console:
1. Open frontend in browser
2. Press F12 → Console tab
3. Look for "API Base URL:" log
4. Should show: `https://your-backend.onrender.com/api`

### Check Network Tab:
1. F12 → Network tab
2. Try to login
3. Look for `/api/auth/login/` request
4. Check:
   - Status: Should be 200
   - Response: Should have `token` field
   - Headers: Check CORS headers

### Common Issues:

**Issue 1: CORS Error**
```
Access to fetch has been blocked by CORS policy
```
**Fix:** Update `CORS_ALLOWED_ORIGINS` in backend environment variables

**Issue 2: 404 Not Found**
```
POST https://...onrender.com/api/auth/login/ 404
```
**Fix:** Check backend URL in `api-client.js` - should end with `/api`

**Issue 3: Token is null**
```
Cannot read properties of null (reading 'token')
```
**Fix:** 
1. Check backend is running (visit backend URL)
2. Check backend logs for errors
3. Verify database is connected

---

## 🚀 Quick Fix Commands

### Redeploy Backend:
```
Render Dashboard → Backend Service → Manual Deploy → Deploy latest commit
```

### Redeploy Frontend:
```
Render Dashboard → Frontend Static Site → Manual Deploy → Clear cache & deploy
```

### Clear Browser Cache:
```
Ctrl + Shift + Delete → Clear cached images and files
```

---

## 📞 Still Having Issues?

1. Check Render logs:
   - Backend Service → Logs tab
   - Look for errors during startup

2. Test backend directly:
   - Visit: `https://your-backend.onrender.com/admin/`
   - Should show Django admin login

3. Test API endpoint:
   - Visit: `https://your-backend.onrender.com/api/`
   - Should show API info or 404 (not CORS error)

