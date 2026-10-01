import re
from urllib.parse import urlparse


def analyze_job(text):
    text = text.lower()

    risk_score = 0
    reasons = []
    breakdown = []

    # 1. Payment request detection
    payment_words = [
        "registration fee",
        "processing fee",
        "training fee",
        "security deposit",
        "pay now",
        "payment required",
        "send money",
        "pay ₹",
        "pay rs"
    ]

    for word in payment_words:
        if word in text:
            risk_score += 25
            reasons.append("Payment or fee is requested.")
            breakdown.append({
                "signal": "Payment request",
                "points": 25
            })
            break

    # 2. Sensitive information detection
    sensitive_words = [
        "bank account",
        "bank details",
        "credit card",
        "debit card",
        "cvv",
        "otp",
        "password",
        "aadhaar",
        "pan card"
    ]

    for word in sensitive_words:
        if word in text:
            risk_score += 25
            reasons.append(
                "Sensitive personal or financial information is requested."
            )
            breakdown.append({
                "signal": "Sensitive information request",
                "points": 25
            })
            break

    # 3. Urgency / pressure detection
    urgency_words = [
        "urgent",
        "immediately",
        "limited time",
        "act now",
        "today only",
        "last chance"
    ]

    for word in urgency_words:
        if word in text:
            risk_score += 15
            reasons.append("Urgent or pressure-based language detected.")
            breakdown.append({
                "signal": "Urgent language",
                "points": 15
            })
            break

    # 4. Suspicious job claim detection
    suspicious_words = [
        "earn money easily",
        "guaranteed job",
        "guaranteed income",
        "work from home and earn",
        "no interview",
        "easy money"
    ]

    for word in suspicious_words:
        if word in text:
            risk_score += 15
            reasons.append("Suspicious job-related claim detected.")
            breakdown.append({
                "signal": "Suspicious job claim",
                "points": 15
            })
            break

    # 5. URL detection and analysis
    urls = re.findall(r'https?://\S+|www\.\S+', text)

    for url in urls:

        url = url.rstrip(".,!?;:)")

        check_url = url

        if check_url.startswith("www."):
            check_url = "http://" + check_url

        parsed_url = urlparse(check_url)

        domain = parsed_url.netloc.lower()
        full_url = check_url.lower()

        # HTTP instead of HTTPS
        if parsed_url.scheme == "http":
            risk_score += 10
            reasons.append(
                "The detected website uses HTTP instead of secure HTTPS."
            )
            breakdown.append({
                "signal": "HTTP website",
                "points": 10
            })

        # IP address instead of domain
        if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain):
            risk_score += 20
            reasons.append(
                "The website uses an IP address instead of a normal domain name."
            )
            breakdown.append({
                "signal": "IP address URL",
                "points": 20
            })

        # Suspicious keywords in URL
        suspicious_url_words = [
            "login",
            "verify",
            "secure",
            "account",
            "payment",
            "claim",
            "reward",
            "free"
        ]

        for word in suspicious_url_words:
            if word in full_url:
                risk_score += 10
                reasons.append(
                    "The URL contains a potentially suspicious keyword."
                )
                breakdown.append({
                    "signal": "Suspicious URL keyword",
                    "points": 10
                })
                break

    # Keep score between 0 and 100
    risk_score = min(risk_score, 100)

    # Risk level
    if risk_score >= 60:
        risk_level = "HIGH RISK"
    elif risk_score >= 30:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "LOW RISK"

    # Safety recommendation
    if risk_level == "HIGH RISK":
        recommendation = (
            "Do not send money or sensitive personal information. "
            "Verify the employer and website independently."
        )

    elif risk_level == "MEDIUM RISK":
        recommendation = (
            "Verify the employer, recruiter, and website before proceeding."
        )

    else:
        recommendation = (
            "No major warning signs detected, but verify the employer "
            "before sharing sensitive information."
        )

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons,
        "breakdown": breakdown,
        "urls": urls,
        "recommendation": recommendation
    }