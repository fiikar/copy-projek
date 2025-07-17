import streamlit as st
import pandas as pd

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di **MindTrack**, platform latihan soal dan catatan kuliah 👋")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

# Halaman Latihan Soal
elif menu == "Latihan Soal":
    st.title("✏️ Latihan Soal")
    st.write("Halaman ini nanti akan menampilkan soal-soal dari berbagai mata kuliah.")

# Halaman Catatan Kuliah
elif menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

    if "page" not in st.session_state:
        st.session_state.page = "form"

    if st.session_state.page == "form":
        Semester = st.radio("Pilih Semester", ["Semester 1", "Semester 2"], horizontal=True)
        blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
        matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

        if st.button("✅ simpan"):
            st.session_state.selected_Semester = Semester
            st.session_state.selected_blok = blok
            st.session_state.selected_matkul = matkul
            st.session_state.page = "pertemuan"

    elif st.session_state.page == "pertemuan":
        st.subheader(f"📘 Catatan untuk {st.session_state.selected_matkul} - {st.session_state.selected_Semester} {st.session_state.selected_blok}")
        st.write("Pilih Pertemuan:")
        col1, col2, col3 = st.columns(3)
        if col1.button("Pertemuan 1"):
            st.session_state.selected_pertemuan = "Pertemuan 1"
            st.session_state.page = "materi"
        if col2.button("Pertemuan 2"):
            st.session_state.selected_pertemuan = "Pertemuan 2"
            st.session_state.page = "materi"
        if col3.button("Pertemuan 3"):
            st.session_state.selected_pertemuan = "Pertemuan 3"
            st.session_state.page = "materi"

    elif st.session_state.page == "materi":
        st.header(f"📖 {st.session_state.selected_pertemuan}")
        st.write(f"Materi untuk {st.session_state.selected_matkul} - {st.session_state.selected_Semester} {st.session_state.selected_blok} - {st.session_state.selected_pertemuan}")
        if st.button("⬅️ Kembali"):
            st.session_state.page = "pertemuan"

# Halaman Riwayat Jawaban
elif menu == "Riwayat Jawaban":
    st.title("🗂️ Riwayat Jawaban")
    st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")

# Halaman Tentang
elif menu == "Tentang":
    st.title("ℹ️ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
    st.header("Tentang Pendiri")
    st.write("Zulfikar Syahid")
    st.write("Rizmi Maitri Nurgianti")
    st.write("Nafisah Nailalhusna I.")
    st.write("Jane Lazarina Bora Isu")
