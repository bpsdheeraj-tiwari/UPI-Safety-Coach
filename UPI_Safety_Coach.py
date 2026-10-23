import streamlit as st

st.set_page_config(page_title="UPI Safety Coach", page_icon="🛡️", layout="centered")

st.title("🛡️ UPI Safety Coach")
st.write("Describe a suspicious UPI-related situation and get safety advice.")

text = st.text_area("Enter your situation:", height=150)


def analyze(user_text):
    txt = user_text.lower()
    risk = 0
    categories = []

    if "otp" in txt:
        risk += 35
        categories.append("OTP Scam")

    if "refund" in txt:
        risk += 20
        categories.append("Refund Scam")

    if "qr" in txt or "qr code" in txt:
        risk += 30
        categories.append("QR Code Scam")

    if "kyc" in txt:
        risk += 25
        categories.append("KYC Scam")

    if "anydesk" in txt or "teamviewer" in txt:
        risk += 40
        categories.append("Screen Sharing Scam")

    if "collect request" in txt:
        risk += 35
        categories.append("UPI Collect Request Scam")

    if risk >= 60:
        level = "🔴 Highly Likely Scam"
    elif risk >= 30:
        level = "🟠 Suspicious"
    else:
        level = "🟢 Low Risk"

    return level, min(risk, 100), categories


if st.button("Analyze"):
    if text.strip():
        level, score, categories = analyze(text)

        st.subheader(level)
        st.metric("Risk Score", f"{score}/100")

        st.write("### Detected Categories")
        if categories:
            for item in categories:
                st.write("✅", item)
        else:
            st.write("No known scam indicators detected.")

        st.write("### Recommended Action")
        st.success(
            """
• Never share OTPs.
• Never scan a QR code to receive money.
• Verify callers through official channels.
• Avoid installing screen-sharing apps.
• Contact your bank directly.
• Report fraud: Cyber Helpline 1930.
"""
        )
    else:
        st.warning("Please enter a situation to analyze.")
