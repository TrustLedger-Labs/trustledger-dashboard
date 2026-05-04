def get_audit_logs() -> list[dict[str, str | int]]:
    return [
        {
            "id": 1,
            "action": "KYC_SUBMITTED",
            "actor": "user",
            "timestamp": "2026-05-04T12:00:00Z",
        }
    ]
