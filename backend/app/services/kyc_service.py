def get_kyc_status(wallet_address: str) -> dict[str, str]:
    return {
        "wallet_address": wallet_address,
        "status": "pending",
        "message": "KYC verification is pending",
    }
