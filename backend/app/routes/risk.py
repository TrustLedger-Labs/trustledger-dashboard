from fastapi import APIRouter

from app.services.risk_service import get_risk_score

router = APIRouter()


@router.get("/{wallet_address}")
def read_risk_score(wallet_address: str) -> dict[str, str | int]:
    return get_risk_score(wallet_address)
