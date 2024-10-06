import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import geopandas as gpd


st.title("Proyek Analisis Data: [E-Commerce Public Dataset]")
st.write("Nama: Ahmad Luthfi Amirulloh")
st.write("Email: m117b4ky0214@bangkit.academy")
st.write("ID Dicoding: ahmadluthfi10")

st.header("1. Diagram Batang Total Pesanan per Kota")
data = {
    'city': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasilia', 'Curitiba'],
    'total_orders': [17500, 4880, 3920, 1751, 1654]
}
df_orders = pd.DataFrame(data)


plt.figure(figsize=(10, 6))
sns.barplot(x='city', y='total_orders', data=df_orders, palette='Blues')
plt.title('Total Orders per City', fontsize=16)
plt.xlabel('City', fontsize=12)
plt.ylabel('Total Orders', fontsize=12)
st.pyplot(plt)

st.write("""
Sao Paulo adalah pusat dari aktivitas pemesanan, dengan total pesanan yang sangat tinggi, sehingga menjadi target yang ideal untuk strategi pemasaran. Produk dalam kategori furniture_decor dan bed_bath_table menunjukkan minat konsumen yang signifikan, dan bisnis harus mempertimbangkan untuk meningkatkan stok dan promosi untuk kategori ini.
""")


st.header("2. Visualisasi Scatter Plot")

category_shipping_analysis = pd.DataFrame({
    'product_weight_g': [2000, 3000, 4000, 5000, 6000],
    'freight_value': [50, 70, 100, 130, 160],
    'delivery_delay': [2, 4, 6, 8, 10],
    'product_length_cm': [30, 50, 70, 90, 110]
})

sns.set(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

sns.scatterplot(ax=axes[0, 0], 
                data=category_shipping_analysis, 
                x='product_weight_g', 
                y='freight_value', 
                hue='delivery_delay', 
                size='delivery_delay',
                sizes=(20, 200), 
                palette='coolwarm', 
                alpha=0.7)

axes[0, 0].set_title('Weight vs Freight Value', fontsize=16)
axes[0, 0].set_xlabel('Average Product Weight (g)', fontsize=12)
axes[0, 0].set_ylabel('Average Freight Value', fontsize=12)

sns.scatterplot(ax=axes[0, 1], 
                data=category_shipping_analysis, 
                x='product_length_cm', 
                y='freight_value', 
                hue='delivery_delay', 
                size='delivery_delay',
                sizes=(20, 200), 
                palette='coolwarm', 
                alpha=0.7)

axes[0, 1].set_title('Length vs Freight Value', fontsize=16)
axes[0, 1].set_xlabel('Average Product Length (cm)', fontsize=12)
axes[0, 1].set_ylabel('Average Freight Value', fontsize=12)

sns.scatterplot(ax=axes[1, 0], 
                data=category_shipping_analysis, 
                x='product_weight_g', 
                y='delivery_delay', 
                hue='freight_value', 
                size='freight_value',
                sizes=(20, 200), 
                palette='viridis', 
                alpha=0.7)

axes[1, 0].set_title('Weight vs Delivery Delay', fontsize=16)
axes[1, 0].set_xlabel('Average Product Weight (g)', fontsize=12)
axes[1, 0].set_ylabel('Average Delivery Delay (days)', fontsize=12)

sns.scatterplot(ax=axes[1, 1], 
                data=category_shipping_analysis, 
                x='product_length_cm', 
                y='delivery_delay', 
                hue='freight_value', 
                size='freight_value',
                sizes=(20, 200), 
                palette='viridis', 
                alpha=0.7)

axes[1, 1].set_title('Length vs. Delivery Delay', fontsize=16)
axes[1, 1].set_xlabel('Average Product Length (cm)', fontsize=12)
axes[1, 1].set_ylabel('Average Delivery Delay (days)', fontsize=12)


plt.tight_layout(pad=3.0)

st.pyplot(fig)

st.write("""
Distribusi berat dan ukuran produk dalam kategori tertentu menunjukkan adanya hubungan yang signifikan antara kedua faktor tersebut dengan biaya pengiriman dan keterlambatan pengiriman. Semakin berat dan besar ukuran produk, semakin tinggi biaya pengiriman yang dikenakan dan semakin lama keterlambatan yang dialami. Visualisasi data melalui scatter plots mengungkapkan pola di mana produk dengan berat antara 2000 hingga 8000 gram dan panjang antara 30 hingga 100 cm cenderung memiliki biaya pengiriman yang tinggi serta keterlambatan yang lebih lama.
""")


st.header("3. Peta Distribusi Pesanan")

geo_data = {
    'latitude': [-23.5505, -22.9068, -19.9208],
    'longitude': [-46.6333, -43.1729, -43.9372],
    'order_count': [17500, 4880, 3920],  
    'customer_city': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

gdf = gpd.GeoDataFrame(geo_data, 
                       geometry=gpd.points_from_xy(geo_data['longitude'], geo_data['latitude']))


m = folium.Map(location=[-22.0, -47.0], zoom_start=6)
for idx, row in gdf.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['customer_city']}: {row['order_count']} pesanan",
        icon=folium.Icon(color='blue')
    ).add_to(m)


st_folium = st.components.v1.html(m._repr_html_(), height=500)

st.write("""
Analisis geospasial memberikan wawasan yang kuat tentang bagaimana lokasi geografis dapat mempengaruhi jumlah pesanan. Ini mengindikasikan bahwa strategi pemasaran dan distribusi yang ditargetkan dapat lebih efektif jika dipertimbangkan berdasarkan lokasi.
""")
