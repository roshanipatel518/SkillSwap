# ⚡ Quick Deployment Fix

## What Was Fixed:

### 1. render.yaml
- Added `rootDir: backend` to avoid path issues
- Improved build command with `--clear` flag
- Added proper gunicorn configuration with workers and timeout
- Fixed ALLOWED_HOSTS to include localhost

### 2. backend/build.sh
- Added `set -e` for error handling
- Added `pip install --upgrade pip`
- Added `--clear` flag to collectstatic
- Made superuser creation non-blocking

### 3. backend/skillswap/settings.py
- Fixed ALLOWED_HOSTS parsing
- Improved CORS configuration with regex for wildcards
- Added CORS_ALLOWED_ORIGIN_REGEXES for preview deployments
- Better environment variable handling

---

## 🚀 Deploy Now:

### If using Render Blueprint (render.yaml):
```bash
git add .
git commit -m "Fix deployment configuration"
git push origin main
```

Then in Render:
1. New + → Blueprint
2. Connect repo
3. Add environment variables
4. Deploy

### If using Manual Setup:

**Build Command:**
```bash
pip install --upgrade pip && pip install -r requirements.txt && python manage.py collectstatic --no-input --clear && python manage.py migrate --no-input && python create_superuser.py
```

**Start Command:**
```bash
gunicorn skillswap.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

**Environment Variables:**
```
PYTHON_VERSION=3.11.0
DEBUG=False
SECRET_KEY=<generate-using-django>
DATABASE_URL=<from-postgresql>
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com,http://localhost:3000
JWT_SECRET=<any-random-string>
```

---

## 🔧 Generate SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## ✅ After Deployment:

1. Update frontend URL in `frontend/js/api-client.js` (line 10)
2. Update CORS_ALLOWED_ORIGINS in backend environment
3. Test admin: `https://your-backend.onrender.com/admin/`
4. Login: admin / admin123

---

## 🐛 Still Having Issues?

Check Render logs:
- Backend Service → Logs tab
- Look for red error messages
- Common issues:
  - Missing environment variables
  - Database connection failed
  - Static files not collected
  - CORS misconfiguration

---

## 📞 Need Help?

1. Check DEPLOYMENT_FIX.md for detailed guide
2. Check Render logs for specific errors
3. Verify all environment variables are set
4. Test backend URL directly in browser

Good luck! 🚀
