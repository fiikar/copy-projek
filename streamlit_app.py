import streamlit as st
import base64

st.set_page_config(page_title="MindTrack", page_icon="🧠")

menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Fungsi untuk tampilkan PDF
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    return pdf_display

# Halaman Catatan Kuliah
if menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

    tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"])
    blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
    matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

    if st.button("✅ Tampilkan Catatan PDF"):
        file_path = f"catatan pdf/{matkul}.pdf"
        try:
            st.markdown(show_pdf(file_path), unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("❌ Catatan PDF belum tersedia!")

# Halaman lainnya contoh
elif menu == "Beranda":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di **MindTrack**, platform latihan soal dan catatan kuliah 👋")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman soal belum dibuat.")

elif menu == "Riwayat Jawaban":
    st.title("🗂️ Riwayat Jawaban")
    st.write("Belum ada riwayat.")

elif menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat oleh tim mahasiswa.")
