# Deployment Guide

## Backend Deployment (Render)

### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub** (already done!)

2. **Go to Render Dashboard**: https://dashboard.render.com

3. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `thisiskanhaiya/qa-agent-hub`
   - Configure:
     - **Name**: `qa-agent-hub-backend`
     - **Root Directory**: `backend`
     - **Runtime**: Python 3
     - **Build Command**: `chmod +x render-build.sh && ./render-build.sh`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - **Instance Type**: Free

4. **Add Environment Variables**:
   - Go to Environment tab
   - Add: `OPENAI_API_KEY` = `your-key-here` (optional - users can provide via UI)

5. **Deploy**: Click "Create Web Service"

### Option 2: Using render.yaml (Blueprint)

1. Push code to GitHub (done!)
2. Go to Render Dashboard → "New +" → "Blueprint"
3. Connect repository and select `render.yaml`
4. Render will auto-configure everything

### After Deployment:

Your backend URL will be: `https://qa-agent-hub-backend.onrender.com`

**Important**: Copy this URL for frontend configuration!

---

## Frontend Deployment (Vercel)

### Update Frontend with Backend URL:

1. **In Vercel Dashboard**, go to your project settings
2. **Environment Variables** → Add:
   ```
   VITE_API_BASE_URL=https://qa-agent-hub-backend.onrender.com
   ```
3. **Redeploy** the frontend

### Or update locally and push:

```bash
cd frontend
# Create .env.production file
echo "VITE_API_BASE_URL=https://qa-agent-hub-backend.onrender.com" > .env.production

# Commit and push
git add .env.production
git commit -m "Add production API URL"
git push origin main
```

Vercel will auto-deploy!

---

## Update CORS (After Deployment)

1. **Get your Vercel URL**: `https://your-app.vercel.app`

2. **Update backend/main.py** CORS settings:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "http://localhost:5173",  # Local dev
           "https://your-app.vercel.app"  # Production
       ],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. **Push changes** to trigger Render redeploy

---

## Testing

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Open browser console (F12)
3. Check Network tab for API calls
4. Should see requests to: `https://qa-agent-hub-backend.onrender.com/api/...`

---

## Troubleshooting

### Backend Issues:

- **Build fails**: Check Render logs → Build tab
- **Start fails**: Check Render logs → Deploy tab
- **Runtime error**: Check Render logs → Logs tab
- **SSL/Connection errors**: Already handled with `verify=False` in httpx client

### Frontend Issues:

- **CORS error**: Update backend CORS with correct Vercel URL
- **API not reachable**: Check `VITE_API_BASE_URL` environment variable
- **404 errors**: Ensure backend is deployed and running

### Free Tier Notes:

- **Render Free**: Spins down after 15 min inactivity (first request will be slow)
- **Vercel Free**: Always on, generous limits
- **Solution**: Paid Render tier ($7/mo) for always-on backend

---

## Current Status

✅ Backend ready for Render deployment
✅ Frontend deployed on Vercel
✅ SSL verification disabled for corporate networks
✅ Dynamic port configuration (Render compatible)
✅ Flexible dependency versions (Python 3.11+ compatible)

Next: Deploy backend to Render and update frontend API URL!
