import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime

airquality_df = pd.read_csv('./airquality_cleaned.csv')
airquality_df['timestamp'] = pd.to_datetime(airquality_df['timestamp'])
airquality_df.index = airquality_df['timestamp']
airquality_df.drop(['station'], axis=1, inplace=True)

min_datetime = airquality_df.index.min()
max_datetime = airquality_df.index.max()

print(min_datetime, max_datetime)

with st.sidebar:
    st.image("./icon.png")
    
    start_date, end_date = st.date_input(
        label='Rentang Date',
        min_value=min_datetime,
        max_value=max_datetime,
        value=[min_datetime, max_datetime]
    )

    start_time = st.time_input(
        label='Waktu Mulai',
        step=3600,
        value=min_datetime
    )
    end_time = st.time_input(
        label='Waktu Berakhir',
        step=3600,
        value=max_datetime
    )


st.header('Kondisi di Stasiun Wanshouxigong :fire:')
st.write("Dashboard ini menyajikan informasi terkini terkait kondisi cuaca yang ada di sekitar stasiun.")

st.markdown(
    """
        - **Nama:** Alexzander Purwoko Widiantoro
        - **Email:** purwoko908@gmail.com
        - **ID Dicoding:** alexzforger
    """
)

start_datetime_str = "" + str(start_date) + " " + str(start_time)
end_datetime_str = "" + str(end_date) + " "+ str(end_time)
start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M:%S")
end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d %H:%M:%S")

filtered_airquality_df = airquality_df.loc["" + str(start_date) + " " + str(start_time) : "" + str(end_date) + " "+str(end_time)]

print(start_datetime)
print(end_datetime)

deltatime_days = (end_datetime - start_datetime).days

if deltatime_days <= 90 and deltatime_days > 2:
    filtered_airquality_df = filtered_airquality_df.resample("D").mean()
elif deltatime_days > 90:
    filtered_airquality_df = filtered_airquality_df.resample("M").mean()

# print(filtered_airquality_df.head())
# print(filtered_airquality_df.tail())

st.subheader("Partikulat Polusi: PM2.5")
st.markdown(
    """
    PM2.5 adalah partikel polusi udara yang berukuran sangat kecil, dengan diameter kurang dari 2,5 mikrometer (µm). 
    Nama "PM" berarti __particulate matter__ atau materi partikulat, dan angka "2.5" menunjukkan ukuran partikelnya.
    Karena ukurannya yang sangat kecil, PM2.5 dapat dengan mudah terhirup ke dalam saluran pernapasan hingga mencapai paru-paru dan bahkan aliran darah, sehingga berpotensi menimbulkan berbagai masalah kesehatan.
    """
)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['PM2.5'], label='PM2.5', color='blue')

ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi')
ax.set_title('Konsentrasi PM2.5')
# ax.set_lelegend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Partikulat Polusi: PM10")
st.markdown(
    """
    PM10 adalah partikel polusi udara yang berukuran lebih besar dari PM2.5, dengan diameter kurang dari 10 mikrometer (µm).
    Sama seperti PM2.5, istilah "PM" merujuk pada particulate matter atau materi partikulat, dan angka "10" menunjukkan ukuran partikelnya. Meskipun ukurannya lebih besar dari PM2.5, PM10 masih cukup kecil untuk terhirup ke dalam saluran pernapasan, tetapi cenderung menumpuk di bagian atas sistem pernapasan, seperti hidung dan tenggorokan, sebelum mencapai paru-paru.
    """
)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['PM10'], label='PM10', color='red')

ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi')
ax.set_title('Konsentrasi PM10')
# ax.set_lelegend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Data Partikulat Polusi Lainnya")
st.write("PM2.5 dan PM10 tersusun dari beberapa partikel polusi, beberapa yang terekam diantaranya adalah SO2 (Sulfur Dioksida), NO2 (Nitrogen Dioksida), CO (Karbon monoksida), dan O3 (Ozon)")
st.markdown("**SO2 (Sulfur Dioksida), NO2 (Nitrogen Dioksida), dan O3 (Ozon)**")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['SO2'], label='SO2', color='red')
ax.plot(filtered_airquality_df.index, filtered_airquality_df['NO2'], label='NO2', color='green')
ax.plot(filtered_airquality_df.index, filtered_airquality_df['O3'], label='O3', color='blue')
# ax.plot(filtered_airquality_df.index, filtered_airquality_df['CO'], label='CO', color='blue')

ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi')
ax.set_title('Konsentrasi partikulat polusi SO2, NO2, dan O3')
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.markdown("**CO (Karbon monoksida)**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['CO'], label='CO', color='orange')
# ax.plot(filtered_airquality_df.index, filtered_airquality_df['CO'], label='CO', color='blue')

ax.set_xlabel('Waktu')
ax.set_ylabel('Konsentrasi')
ax.set_title('Konsentrasi partikulat polusi Karbon monoksida')
ax.grid(True)
st.pyplot(fig)

st.subheader("Data Curah Hujan")
st.write("Berikut adalah curah hujan yang terjadi selama rentang waktu yang dipilih.")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['RAIN'], label='RAIN', color='red')

ax.set_xlabel('Waktu')
ax.set_ylabel('Curah Hujan (mm)')
# ax.set_lelegend()
ax.grid(True)
st.pyplot(fig)

st.subheader("Data Temperature")
st.write("Berikut adalah temperature selama rentang waktu yang dipilih.")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_airquality_df.index, filtered_airquality_df['TEMP'], label='TEMP', color='green')

ax.set_xlabel('Waktu')
ax.set_ylabel('Temperature (in Celcius)')
# ax.set_lelegend()
ax.grid(True)
st.pyplot(fig)

# st.write(
#     """
#     # My first app
#     Hello, para calon praktisi data masa depan!
    
#     """
# )

st.caption("Copyright © Alexz Forger")