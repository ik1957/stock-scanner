import streamlit as st
import requests
import pandas as pd

# מפתח ה-API שלך
API_KEY = "***"

def get_stock_data():
    # חיבור ל-API של Financial Modeling Prep (דוגמה)
    url = f"https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # המידע יחזור כתוצאה בנתיב הזה (אם תקבל משהו שונה יש לבדוק את התשובה)
    return data[0]  # החזרת המניה הראשונה מתוך התשובה

def check_macd_and_heikin_ashi(stock_data):
    # בדיקת MACD ו-Heikin Ashi
    macd_value = stock_data['macd']  # אם הנתונים מספקים את ה-MACD
    macd_signal = stock_data['macd_signal']  # אם הנתונים מספקים את קו ה-Signal

    # אסטרטגיה לכניסות
    # כלל כניסה ללונג
    if macd_value > macd_signal and macd_value > 0:
        if stock_data['heikin_ashi'] == "green":
            return "כניסה ללונג"

    # כלל כניסה לשורט
    if macd_value < macd_signal and macd_value < 0:
        if stock_data['heikin_ashi'] == "red":
            return "כניסה לשורט"

    return "אין כניסה"

def main():
    st.title("Stock Scanner - S&P 500")
    
    # קריאה לנתוני מניות
    stock_data = get_stock_data()

    # הצגת המידע ב-Streamlit
    st.write("נתוני מניית AAPL:")
    st.write(stock_data)

    # ביצוע בדיקת MACD ו-Heikin Ashi והצגת התוצאה
    action = check_macd_and_heikin_ashi(stock_data)
    st.write(f"פעולה מומלצת: {action}")

    # תוכל להוסיף כאן גם לוגיקה לסרוק מניות לפי קריטריונים טכניים (MACD, Heikin-Ashi)
    st.info("הסורק עובד... אנא המתן מספר שניות")
    st.success("תוצאות סריקה יופיעו כאן בקרוב!")

if __name__ == "__main__":
    main()
