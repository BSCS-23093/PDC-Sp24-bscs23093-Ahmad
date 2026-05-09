from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def add_student_id_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = "BSCS23093"
    return response

app.include_router(challenge.router, prefix="/api")
app.include_router(webhooks.router, prefix="/webhooks")