def get_risk_score(wallet_address: str) -> dict[str, str | int]:
    return {
        "wallet_address": wallet_address,
        "risk_score": 42,
        "risk_level": "medium",
    }
