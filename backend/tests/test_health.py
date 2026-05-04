import sys
from pathlib import Path

from fastapi.testclient import TestClient

BACKEND_DIR = Path(__file__).resolve().parents[1]
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.main import app


client = TestClient(app)
WALLET_ADDRESS = "0x1234567890abcdef"


def test_root_endpoint() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "TrustLedger API is running"}


def test_kyc_status_endpoint() -> None:
    response = client.get(f"/api/kyc/status/{WALLET_ADDRESS}")

    assert response.status_code == 200
    assert response.json() == {
        "wallet_address": WALLET_ADDRESS,
        "status": "pending",
        "message": "KYC verification is pending",
    }


def test_audit_logs_endpoint() -> None:
    response = client.get("/api/audit-logs")

    assert response.status_code == 200
    audit_logs = response.json()
    assert isinstance(audit_logs, list)
    assert len(audit_logs) > 0
    assert audit_logs[0] == {
        "id": 1,
        "action": "KYC_SUBMITTED",
        "actor": "user",
        "timestamp": "2026-05-04T12:00:00Z",
    }


def test_risk_score_endpoint() -> None:
    response = client.get(f"/api/risk/{WALLET_ADDRESS}")

    assert response.status_code == 200
    assert response.json() == {
        "wallet_address": WALLET_ADDRESS,
        "risk_score": 42,
        "risk_level": "medium",
    }
