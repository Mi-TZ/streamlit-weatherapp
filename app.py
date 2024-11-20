import streamlit as st
import requests
from datetime import datetime

def get_weather_data(city_name):
    api_key = "f5b8b5c525e5a50b0924d16cf3224625"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "APPID": api_key,
        "units": "metric",
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.set_page_config(
        page_title="Mitz's Weather App",
        page_icon="🌦️",
        layout="centered",
    )
    
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f4f8;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🌦️ Weather Application")
    st.write("Enter a city name to get real-time weather updates!")

    city_name = st.text_input("🏙️ Enter a city name:", "")

    if st.button("Get Weather"):
        if city_name:
            weather_data = get_weather_data(city_name)
            if weather_data:
                st.subheader(f"🌍 Weather in {city_name.capitalize()}")
                
                icon_code = weather_data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
                st.image(icon_url, width=100)

                st.metric("🌡️ Temperature", f"{weather_data['main']['temp']}°C")
                st.metric("🌫️ Description", weather_data['weather'][0]['description'].capitalize())
                st.metric("💧 Humidity", f"{weather_data['main']['humidity']}%")
                st.metric("💨 Wind Speed", f"{weather_data['wind']['speed']} m/s")
                st.write(f"📅 Data last updated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                st.error("❌ Failed to fetch weather data. Please check the city name.")
        else:
            st.warning("⚠️ Please enter a valid city name.")

# Run the application
if __name__ == "__main__":
    main()
