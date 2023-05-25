import streamlit as st  
import pandas as pd 
import plotly.express as px  

# utilisizegi
st.set_page_config(layout='wide')

def load_data():
    return pd.read_csv('dinkes-od_17532_persentase_orang_dengan_gangguan_jiwa_odgj_berat_menda_data.csv', sep=',', parse_dates=['tahun'], index_col='id')

odgj_jabar = load_data()
odgj_jabar['tahun'] = odgj_jabar['tahun'].dt.year 


# title
st.title('Dashboard Sederhana persentase orang gangguan jiwa Provinsi Jawa Barat')



with st.expander('Berikut parameter yang bisa dipilih'):
    st.write('Ada beberapa filterisasi yang bisa anda pilih')
    
    dates = odgj_jabar['tahun'].unique()
    regions = odgj_jabar['nama_kabupaten_kota'].unique()
    
    select_date = st.multiselect(
        label='Pilih tahun :',
        options= dates,
        default = dates
    )
    
    odgj_jabar = odgj_jabar.query('tahun == @select_date')
    
    if odgj_jabar.empty:
        st.error('tidak ada data yang terinput')
        st.stop()


fig = px.bar(odgj_jabar, x="nama_kabupaten_kota", y="persentase_odgj", color="nama_kabupaten_kota")
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': True})