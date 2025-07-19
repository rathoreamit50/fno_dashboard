
# 📊 F&O Dashboard (Open Source & Free Hosting)

## 🔧 Technologies Used
- Frontend: React (with Tailwind or Vite)
- Backend: FastAPI
- Data Source: Excel (generated via Python)
- Deployment: Docker + GitHub + Render (Free)

---

## 🧱 Project Structure
```
fno-dashboard/
├── backend/        # FastAPI backend
├── frontend/       # React dashboard
├── docker-compose.yml
├── render.yaml     # For Render.com auto-deployment
```

---

## 🚀 Local Setup with Docker
```bash
docker-compose up --build
```
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/top-fno-picks

---

## ☁️ Cloud Hosting on Render.com
1. Push this folder to GitHub
2. Go to [Render.com](https://render.com)
3. Click **New Web Service** for:
   - Backend → Python → Port 10000
   - Frontend → Node → `NEXT_PUBLIC_API_URL=https://<backend>.onrender.com/api/top-fno-picks`
4. Use `render.yaml` for CI/CD automation (optional)

---

## 📁 Excel Data Source
Place `Weekly_FNO_Analysis_With_OI.xlsx` in the backend folder.

---

Need help? Ping me for setup, build errors, or GitHub push assistance!
