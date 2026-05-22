import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="GTM Innovation Copilot", layout="wide")

st.title("GTM Innovation Copilot")
st.subheader("AI workflow accelerator for Sales, Technical Success, and Revenue Operations")

customer_notes = st.text_area(
    "Paste customer interaction notes",
    height=250,
    placeholder="Paste meeting notes, call summaries, opportunity details..."
)

if st.button("Analyze Opportunity"):

    if not customer_notes.strip():
        st.warning("Please enter customer notes.")
    else:

        prompt = f"""
You are an elite GTM innovation copilot for enterprise go-to-market teams.

Analyze the following customer interaction notes.

Return clearly structured sections:

1. Executive Summary
2. Objection Intelligence
3. Opportunity Risk Signals (Low / Medium / High)
4. Recommended GTM Next Actions
5. Leadership Brief
6. Follow-up Email Draft

Customer Notes:
{customer_notes}
"""

        with st.spinner("Analyzing..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert enterprise GTM workflow AI copilot."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )

        result = response.choices[0].message.content

        st.success("Analysis complete")
        st.markdown(result)