import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Enterprise GTM Decision Copilot", layout="wide")

st.title("Enterprise GTM Decision Copilot")
st.subheader("Trust-aware AI workflow intelligence for enterprise go-to-market teams")

customer_notes = st.text_area(
    "Paste customer interaction notes",
    height=250,
    placeholder="Paste customer meeting notes, call summaries, objections, opportunity details..."
)

if st.button("Analyze Opportunity"):

    if not customer_notes.strip():
        st.warning("Please enter customer interaction notes.")
    else:

        prompt = f"""
You are an enterprise AI decision intelligence assistant for GTM teams.

Analyze the customer interaction notes below.

Return output in EXACT structured sections:

## 1. Opportunity Intelligence
Include:
- Executive summary
- Buying signals
- Customer intent indicators
- Competitive references
- Key objections

## 2. Confidence Assessment
Provide:
- Decision Confidence Score (0-100)
- Short explanation

Assess confidence based on:
clarity of customer intent,
budget certainty,
technical readiness,
stakeholder alignment,
competitive ambiguity.

## 3. Human Review Gate
Decide:
YES or NO

Trigger YES if:
security concerns,
compliance concerns,
unclear intent,
high competitive risk,
budget ambiguity,
technical uncertainty.

Explain why.

## 4. Risk & Governance Flags
Classify:
- Security risk
- Compliance risk
- Procurement risk
- Budget risk
- Competitive displacement risk
- Stakeholder alignment risk

Rate each:
LOW / MEDIUM / HIGH

## 5. Workflow Routing Recommendation
Recommend which teams should engage next:
- Sales
- Solutions Engineering
- Security
- Revenue Operations
- Leadership
- Legal / Compliance

Explain routing logic.

## 6. Fallback Workflow
If confidence is low or risk is high, recommend human fallback workflow.

## 7. Recommended GTM Next Actions
Provide prioritized next actions.

## 8. Leadership Brief
Create concise executive summary.

## 9. Follow-up Email Draft
Create customer-ready professional follow-up email.

Customer Notes:
{customer_notes}
"""

        with st.spinner("Running enterprise decision intelligence analysis..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert enterprise AI product decision intelligence assistant focused on trust-aware GTM workflow support."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )

        result = response.choices[0].message.content

        st.success("Enterprise decision analysis complete")
        st.markdown(result)