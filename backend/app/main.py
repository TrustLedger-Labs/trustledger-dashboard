from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import audit_logs, kyc, risk

app = FastAPI(
    title="TrustLedger API",
    description="Starter API for the TrustLedger Dashboard.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kyc.router, prefix="/api/kyc", tags=["kyc"])
app.include_router(audit_logs.router, prefix="/api/audit-logs", tags=["audit logs"])
app.include_router(risk.router, prefix="/api/risk", tags=["risk"])


@app.get("/")
def health_check() -> dict[str, str]:
    return {"message": "TrustLedger API is running"}
