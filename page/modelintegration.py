import streamlit as st
import pandas as pd
import pickle

def main():
    st.title("Prediksi Payment Tier")

    # Load model dari berkas .pkl
    def load_model():
        with open('best.pkl', 'rb') as f:
            model = pickle.load(f)
        return model

    # Fungsi untuk membuat prediksi PaymentTier
    def predict_payment_tier(data):
        model = load_model()

        # Lakukan prediksi menggunakan model
        predicted_payment_tier = model.predict(data)
        return predicted_payment_tier

    # Input dari pengguna
    education_mapping = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
    education = st.selectbox("Pendidikan:", options=list(education_mapping.keys()))

    gender_mapping = {'Female': 0, 'Male': 1}
    gender = st.selectbox("Jenis Kelamin:", options=list(gender_mapping.keys()))

    age = st.slider("Usia:", min_value=20, max_value=50, step=1)
    years_in_company = st.slider("Tahun di Perusahaan:", min_value=0, max_value=15, step=1)
    
    years_category = st.selectbox("Years Category:", options=["Intermediate", "Senior"])

    if years_category == "Intermediate":
        years_category_value = 0
    else:
        years_category_value = 1

    # Tombol untuk membuat prediksi
    if st.button("Prediksi"):
        # Buat DataFrame dari input pengguna
        data = pd.DataFrame({
            'Education': [education_mapping[education]],
            'Age': [age],
            'Gender': [gender_mapping[gender]],
            'YearsInCompany': [years_in_company],
            'YearsCategorySenior': [years_category_value],
            'PaymentTier': [0]
        })

        # Lakukan prediksi
        # Model tidak memerlukan kolom PaymentTier
        predicted_payment_tier = predict_payment_tier(data)
        
        # Tampilkan hasil prediksi
        if predicted_payment_tier == 1:
            st.write("Prediksi Payment Tier: Rendah")
        elif predicted_payment_tier == 2:
            st.write("Prediksi Payment Tier: Sedang")
        else:
            st.write("Prediksi Payment Tier: Tinggi")

if __name__ == "__main__":
    main()
