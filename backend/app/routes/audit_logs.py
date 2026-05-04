from fastapi import APIRouter

from app.services.audit_service import get_audit_logs

router = APIRouter()


@router.get("")
def read_audit_logs() -> list[dict[str, str | int]]:
    return get_audit_logs()
