import streamlit as st
import pandas as pd
import requests

def main():
    st.title("🔎 Stock Scanner - S&P 500")
    st.write("סריקה חכמה של מניות לפי תנאים טכניים (MACD ו-Heikin Ashi)")
    st.info("🔄 הסורק עובד... אנא המתן מספר שניות")
    st.success("✅ תוצאות סריקה יופיעו כאן בקרוב!")

if __name__ == "__main__":
    main()
