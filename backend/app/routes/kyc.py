from fastapi import APIRouter

from app.services.kyc_service import get_kyc_status

router = APIRouter()


@router.get("/status/{wallet_address}")
def read_kyc_status(wallet_address: str) -> dict[str, str]:
    return get_kyc_status(wallet_address)
