elif menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

    if "show_notes" not in st.session_state:
        st.session_state.show_notes = False

    tingkat = st.radio("Pilih Tingkat", ["Tingkat 1", "Tingkat 2"], horizontal=True)
    blok = st.selectbox("Pilih Blok", ["Blok 1", "Blok 2"])
    matkul = st.selectbox("Pilih Mata Kuliah", ["Kimia Fisika", "Spektrofotometri", "Biokimia"])

    if st.button("✅ simpan"):
        st.session_state.show_notes = True
        st.session_state.selected_tingkat = tingkat
        st.session_state.selected_blok = blok
        st.session_state.selected_matkul = matkul

    if st.session_state.show_notes:
        st.subheader(f"📘 Catatan untuk {st.session_state.selected_matkul} - {st.session_state.selected_tingkat} {st.session_state.selected_blok}")
        st.info("Belum ada catatan yang ditambahkan.")
