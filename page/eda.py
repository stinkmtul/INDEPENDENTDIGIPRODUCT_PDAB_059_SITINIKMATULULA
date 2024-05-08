import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Employee.csv")

import streamlit as st
import plotly.express as px

def plot_education_distribution(df):
    st.title('Proporsi Jumlah Karyawan untuk Setiap Tingkat Pendidikan')
    # Dropdown untuk memilih pendidikan
    education_options = ['Semua'] + df['Education'].unique().tolist()
    selected_education = st.selectbox("Pilih Pendidikan", education_options)

    if selected_education == 'Semua':
        # Hitung jumlah karyawan untuk setiap tingkat pendidikan
        education_counts = df['Education'].value_counts().reset_index()
        education_counts.columns = ['Education', 'Count']  # Ubah nama kolom

        # Plot pie chart untuk menampilkan proporsi jumlah karyawan untuk setiap tingkat pendidikan
        fig = px.pie(education_counts, values='Count', names='Education',
                     color_discrete_sequence=px.colors.qualitative.Set3)  # Gunakan palet warna Set3
        fig.update_traces(textposition='inside', textinfo='percent+label')  # Tampilkan label di dalam pie chart
        fig.update_layout(showlegend=False)  # Sembunyikan legend
        st.plotly_chart(fig)
    else:
        # Filter data berdasarkan pendidikan yang dipilih
        data = df[df['Education'] == selected_education]

        # Hitung jumlah karyawan untuk tingkat pendidikan yang dipilih
        gender_counts = data['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']  # Ubah nama kolom

        # Plot pie chart untuk menampilkan proporsi jumlah karyawan untuk tingkat pendidikan yang dipilih
        fig = px.pie(gender_counts, values='Count', names='Gender', 
                     title=f'Proporsi Jumlah Karyawan dengan Pendidikan {selected_education}',
                     color_discrete_sequence=px.colors.qualitative.Set3)  # Gunakan palet warna Set3
        fig.update_traces(textposition='inside', textinfo='percent+label')  # Tampilkan label di dalam pie chart
        fig.update_layout(showlegend=True)  # Tampilkan legend
        st.plotly_chart(fig)

    # Interpretasi
    st.subheader("Interpretasi:")
    st.write("Mayoritas karyawan memiliki gelar sarjana, diikuti oleh gelar magister, dan hanya sebagian kecil yang memiliki gelar doktor. Laki-laki mendominasi di tingkat pendidikan tinggi, menunjukkan ketimpangan gender.")

    # Actionable Insight
    st.subheader("Actionable Insight:")
    st.write("Perusahaan dapat membantu perempuan dengan memperkenalkan program-program pendukung, seperti mentoring dan pembentukan jaringan profesional. Hal ini dapat membantu perempuan meraih kesuksesan karier lebih baik.")


def plot_payment_tier_distribution(df):
    # Menghitung jumlah karyawan dalam setiap kelompok pembayaran tier berdasarkan pengalaman dalam domain saat ini
    payment_tier_counts = df.groupby(['ExperienceInCurrentDomain', 'PaymentTier']).size().unstack(fill_value=0)

    # Plotting
    st.title('Distribusi Tingkat Pembayaran Berdasarkan Pengalaman dalam Domain Saat Ini')
    fig = px.bar(payment_tier_counts, x=payment_tier_counts.index, y=payment_tier_counts.columns, 
                 title='Distribusi Tingkat Pembayaran Berdasarkan Pengalaman dalam Domain Saat Ini',
                 labels={'index': 'Pengalaman dalam Domain Saat Ini', 'value': 'Jumlah Karyawan'},
                 color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig)

    # Interpretasi
    st.subheader("Interpretasi:")
    st.write("Mayoritas karyawan dengan pengalaman 0-7 tahun cenderung memiliki tingkat pembayaran tertentu, sementara mereka dengan pengalaman lebih tinggi mungkin mendapat pembayaran lebih tinggi.")

    # Actionable Insight
    st.subheader("Actionable Insight:")
    st.write("Perusahaan bisa menyesuaikan kebijakan kompensasi berdasarkan pengalaman saat ini. Ini bisa berupa peninjauan struktur gaji, insentif tambahan, atau program pengembangan karier untuk mendorong karyawan meningkatkan keterampilan dan pengalaman mereka.")


def plot_age_distribution(df):
    st.title('Distribusi Usia Karyawan Berdasarkan Gender')

    # Buat histogram untuk distribusi usia karyawan berdasarkan gender
    fig = px.histogram(df, x='Age', color='Gender', marginal='rug', nbins=30, 
                       labels={'Age': 'Usia', 'count': 'Jumlah Karyawan'}, 
                       title='Distribusi Usia Karyawan Berdasarkan Gender',
                       histfunc='count', 
                       category_orders={'Gender': ['Female', 'Male']},
                       barmode='overlay')

    # Tampilkan histogram
    st.plotly_chart(fig)

    # Interpretasi
    st.subheader("Interpretasi:")
    st.write("Mayoritas karyawan berusia antara 22 hingga 40 tahun, dengan jumlah karyawan laki-laki lebih banyak dibandingkan perempuan.")

    # Actionable Insight
    st.subheader("Actionable Insight:")
    st.write("Untuk meningkatkan keberagaman gender, perusahaan dapat meningkatkan upaya rekrutmen karyawan perempuan lebih banyak.")

def main():
    # Sidebar untuk memilih menu
    menu = st.sidebar.radio("Pilih Menu", ["Pendidikan", "Tingkat Pembayaran", "Usia"])

    if menu == 'Pendidikan':
        plot_education_distribution(df)
    elif menu == 'Tingkat Pembayaran':
        plot_payment_tier_distribution(df)
    elif menu == 'Usia':
        plot_age_distribution(df)

if __name__ == "__main__":
    main()
