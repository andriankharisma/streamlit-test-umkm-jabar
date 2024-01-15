import streamlit as st
import pandas as pd

# Judul
st.title("Proyeksi Jumlah UMKM pada Kabupaten/Kota di Jawa Barat")
st.divider()

image_url = "https://imgsrv2.voi.id/26DXRaFB78isvNRt-IFIecCv9kM_bvVKValgIq5bWQU/auto/1200/675/sm/1/bG9jYWw6Ly8vcHVibGlzaGVycy8xOTMwNzkvMjAyMjA3MjEyMzIyLW1haW4uY3JvcHBlZF8xNjU4NDIwNTU5LmpwZw.jpg"
st.image(image_url, use_column_width=True)

# Deskripsi web
st.write("""
         Website ini menampilkan data proyeksi jumlah usaha mikro kecil menengah (UMKM) berdasarkan Kabupaten/Kota di provinsi Jawa Barat dari 
         tahun 2016 - 2023. 
         
         Dataset ini dibuat oleh Dinas Koperasi dan Usaha Kecil yang dikeluarkan dalam periode 1 tahun sekali. 
         """)

# Dataset 
df = pd.read_csv("https://raw.githubusercontent.com/andriankharisma/streamlit-test-umkm-jabar/main/data_umkm_jabar.csv")

# Total Kab/Kota dan UMKM
st.header("Total Kab/Kota & Proyeksi UMKM")
total_kab_kota = len(df['Nama Kabupaten / Kota'].unique())
total_proyeksi_umkm = df['Proyeksi Jumlah UMKM'].sum()
formatted_total_proyeksi_umkm = "{:,.0f}".format(total_proyeksi_umkm)

col1, col2 = st.columns(2)

with col1 :
    st.metric(label="Jumlah Kabupaten/Kota",
              value=total_kab_kota)
    
with col2:
    st.metric(label="Jumlah Proyeksi UMKM",
              value=f"{formatted_total_proyeksi_umkm} UMKM")

# Proyeksi UMKM dari 2016-2023
st.header("Jumlah Proyeksi UMKM dari 2016-2023")
jumlah_proyeksi_per_tahun = df.groupby('Tahun')['Proyeksi Jumlah UMKM'].sum()
st.bar_chart(jumlah_proyeksi_per_tahun)

# Nilai unik dari kolom "Nama Kabupaten / Kota"
kab_kota_unique = ['SEMUA KAB/KOTA'] + list(df['Nama Kabupaten / Kota'].unique())
tahun_unique = ['SEMUA TAHUN'] + list(df['Tahun'].unique())


# Proyeksi Jumlah UMKM untuk Kabupaten/Kota dan Tahun yang Dipilih
st.header("Proyeksi Jumlah UMKM untuk Kabupaten/Kota dan Tahun yang Dipilih") 
# Checkbox Filter
col1, col2 = st.columns(2)

with col1:
    # Filter Kabupaten/Kota
    kab_kota_filter = st.multiselect(
    'Pilih Kabupaten/Kota :',
    kab_kota_unique
    )

with col2 :
    # Filter Tahun
    tahun_filter = st.multiselect(
        'Pilih Tahun :',
        tahun_unique
    )
    
filtered_df = df

if 'SEMUA KAB/KOTA' not in kab_kota_filter:
    filtered_df = filtered_df[filtered_df['Nama Kabupaten / Kota'].isin(kab_kota_filter)]

if 'SEMUA TAHUN' not in tahun_filter:
    filtered_df = filtered_df[filtered_df['Tahun'].isin(tahun_filter)]
    

# Hitung jumlah UMKM berdasarkan hasil filter
total_umkm = filtered_df['Proyeksi Jumlah UMKM'].sum()

# Format nilai dalam format ribuan dan tambahkan kata "UMKM"
formatted_umkm = "{:,.0f}".format(total_umkm)
st.metric(label="Jumlah UMKM", value=f"{formatted_umkm} UMKM")

st.divider()
st.write("Copyright © 2024 by Tim Pengembangan DGX, Universitas Gunadarma")
st.link_button("Klik untuk menuju sumber dataset", "https://opendata.jabarprov.go.id/id/dataset/proyeksi-jumlah-usaha-mikro-kecil-menengah-umkm-berdasarkan-kabupatenkota-di-jawa-barat")

# Menampilkan dataset
# st.dataframe(df, use_container_width=True)