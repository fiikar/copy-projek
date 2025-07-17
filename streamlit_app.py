import streamlit as st

st.set_page_config(page_title="MindTrack", page_icon="🧠")

menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

if menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

    if "page" not in st.session_state:
        st.session_state.page = "form"

    # FORM PILIH SEMESTER, BLOK, MATKUL
    if st.session_state.page == "form":
        Semester = st.radio("Pilih Semester", ["Semester 1", "Semester 2"], horizontal=True)
        blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
        matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

        if st.button("✅ simpan"):
            st.session_state.selected_Semester = Semester
            st.session_state.selected_blok = blok
            st.session_state.selected_matkul = matkul
            st.session_state.page = "pertemuan"

    # TAMPILKAN TOMBOL PERTEMUAN
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

    # TAMPILKAN ISI MATERI
    elif st.session_state.page == "materi":
        st.header(f"📖 {st.session_state.selected_pertemuan}")
        st.write(f"Materi untuk {st.session_state.selected_matkul} - {st.session_state.selected_Semester} {st.session_state.selected_blok} - {st.session_state.selected_pertemuan}")
        if st.button("⬅️ Kembali"):
            st.session_state.page = "pertemuan"
