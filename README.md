# RecruitSafe

## Explainable Cyber Risk Assessment for Online Job and Internship Offers

RecruitSafe is a cybersecurity web application that analyzes online job and internship offers for common scam warning signals.

The system examines job-related messages and URLs for suspicious patterns such as payment requests, sensitive information requests, urgent language, suspicious job claims, and potentially risky URLs.

It provides an explainable risk score, risk level, detected warning signals, safety recommendations, and scan history.

---

## Features

- Job and internship message analysis
- Payment and fee request detection
- Sensitive information request detection
- Urgency and pressure language detection
- Suspicious job claim detection
- URL detection and analysis
- HTTP website detection
- IP address URL detection
- Suspicious URL keyword detection
- Explainable 0–100 risk score
- LOW, MEDIUM and HIGH risk classification
- Risk score breakdown
- Safety recommendations
- Verification checklist
- SQLite-based scan history

---

## Technology Stack

- Python
- Flask
- HTML
- CSS
- SQLite
- Regular Expressions

---

## System Workflow

User enters job/internship message
        ↓
Flask Web Interface
        ↓
Job Offer Analyzer
        ↓
Rule-Based Risk Detection
        ↓
Risk Score Calculation
        ↓
Risk Level Classification
        ↓
Explanation & Safety Recommendation
        ↓
SQLite Scan History

---

## Risk Detection

RecruitSafe currently checks for:

### 1. Payment Requests

Examples:

- Registration fee
- Processing fee
- Training fee
- Security deposit
- Payment required

### 2. Sensitive Information

Examples:

- Bank account details
- Credit/debit card information
- OTP
- Password
- Aadhaar
- PAN card

### 3. Urgent Language

Examples:

- Urgent
- Act now
- Immediately
- Limited time
- Today only

### 4. Suspicious Job Claims

Examples:

- Guaranteed job
- Guaranteed income
- Easy money
- No interview
- Work from home and earn

### 5. URL Analysis

The system checks detected URLs for:

- HTTP instead of HTTPS
- IP address based URLs
- Suspicious URL keywords

---

## Risk Classification

| Risk Score | Risk Level |
|------------|------------|
| 0–29 | LOW RISK |
| 30–59 | MEDIUM RISK |
| 60–100 | HIGH RISK |

The risk score is a rule-based indicator and does not prove that a job offer is malicious.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RecruitSafe.git