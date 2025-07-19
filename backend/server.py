from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from weekly_fno_generator import generate_weekly_fno_file

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse({"message": "F&O Backend is running. Use /api/top-fno-picks to get data."})

@app.get("/api/top-fno-picks")
async def fno_top_picks():
    try:
        data = get_top_picks()
        return data
    except Exception as e:
        return {"error": str(e)}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/top-fno-picks")
def get_top_picks():
    try:
        df = pd.read_excel("Weekly_FNO_Analysis_With_OI.xlsx")
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

# Schedule XLSX generation every Monday at 6:00 AM
scheduler = BackgroundScheduler()
scheduler.add_job(generate_weekly_fno_file, "cron", day_of_week="mon", hour=6, minute=0)
scheduler.start()
