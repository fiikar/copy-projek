import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="MindTrack", page_icon="🧠")

# Menu Sidebar
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["Beranda", "Latihan Soal", "Catatan Kuliah", "Riwayat Jawaban", "Tentang"])

# Data Soal
soal_data = {
    "Spektrofotometri": [
        {"question": "Perbedaan metode analisis secara konvensional dan analisis intrumen adalah sebagai berikut, kecuali ?", "options": ["Metode analisis instrumen digunakan untuk analit dengan konsentrasi rendah, sedangkan metode analisis konvensional digunakan untuk analit konsentrasi tinggi", "Metode analisis instrumen membutuhkan standar sedangkan metode analis konvensional tidak ", "Metode analisis instrumen membutuhkan pemisahan analit secara fisik sedangkan metode analis konvensional tidak ","Metode analisis instrumen memiliki sensitivitas lebih tinggi dengan metode analis konvensional"], "answer": "Metode analisis instrumen membutuhkan pemisahan analit secara fisik sedangkan metode analis konvensional tidak "},
        {"question": "Jika transmita suatu larutan adalah 19.4% maka absorbansi larutan tersebut adalah?", "options": [" 1.288 ", "1,404 ", "0,806 ","0,712"], "answer": "0,712"},
        {"question": "Apa itu panjang gelombang?", "options": ["Jarak antara dua puncak gelombang", "Jumlah gelombang per detik", "Energi cahaya"], "answer": "Jarak antara dua puncak gelombang"},
        {"question": "Apa yang dimaksud dengan absorbansi?", "options": ["Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Jumlah cahaya yang diserap"},
        {"question": "Apa itu hukum Beer-Lambert?", "options": ["Hubungan antara konsentrasi dan absorbansi", "Hubungan antara suhu dan tekanan", "Hubungan antara volume dan massa"], "answer": "Hubungan antara konsentrasi dan absorbansi"},
        {"question": "Apa yang dimaksud dengan spektrometer?", "options": ["Alat untuk mengukur suhu", "Alat untuk mengukur cahaya", "Alat untuk mengukur tekanan"], "answer": "Alat untuk mengukur cahaya"},
        {"question": "Apa itu fotodetektor?", "options": ["Alat untuk menghasilkan cahaya", "Alat untuk mendeteksi cahaya", "Alat untuk menyimpan cahaya"], "answer": "Alat untuk mendeteksi cahaya"},
        {"question": "Apa yang dimaksud dengan transmittance?", "options": ["Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Jumlah cahaya yang diteruskan"},
        {"question": "Apa itu larutan standar?", "options": ["Larutan dengan konsentrasi yang diketahui", "Larutan dengan pH yang diketahui", "Larutan dengan suhu yang diketahui"], "answer": "Larutan dengan konsentrasi yang diketahui"},
        {"question": "Apa yang dimaksud dengan kalibrasi?", "options": ["Proses mengukur suhu", "Proses mengukur konsentrasi", "Proses menyesuaikan alat ukur"], "answer": "Proses menyesuaikan alat ukur"},
        {"question": "Apa itu spektrum?", "options": ["Rentang panjang gelombang", "Jumlah cahaya yang diserap", "Jumlah cahaya yang dipantulkan"], "answer": "Rentang panjang gelombang"},
        {"question": "Apa yang dimaksud dengan fotometri?", "options": ["Ilmu tentang cahaya", "Ilmu tentang suara", "Ilmu tentang suhu"], "answer": "Ilmu tentang cahaya"},
        {"question": "Apa itu sumber cahaya?", "options": ["Alat untuk mengukur cahaya", "Alat untuk menghasilkan cahaya", "Alat untuk menyimpan cahaya"], "answer": "Alat untuk menghasilkan cahaya"},
        {"question": "Apa yang dimaksud dengan panjang gelombang maksimum?", "options": ["Panjang gelombang dengan absorbansi tertinggi", "Panjang gelombang dengan suhu tertinggi", "Panjang gelombang dengan tekanan tertinggi"], "answer": "Panjang gelombang dengan absorbansi tertinggi"},
        {"question": "Apa itu larutan sampel?", "options": ["Larutan yang akan diuji", "Larutan yang digunakan untuk kalibrasi", "Larutan yang digunakan untuk mencuci alat"], "answer": "Larutan yang akan diuji"},
        {"question": "Apa yang dimaksud dengan noise dalam spektrofotometri?", "options": ["Gangguan pada sinyal", "Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap"], "answer": "Gangguan pada sinyal"},
        {"question": "Apa itu resolusi dalam spektrofotometri?", "options": ["Kemampuan alat untuk membedakan panjang gelombang", "Jumlah cahaya yang diteruskan", "Jumlah cahaya yang diserap"], "answer": "Kemampuan alat untuk membedakan panjang gelombang"},
        {"question": "Apa yang dimaksud dengan fotometri UV-Vis?", "options": ["Pengukuran cahaya ultraviolet dan tampak", "Pengukuran cahaya inframerah", "Pengukuran cahaya mikro"], "answer": "Pengukuran cahaya ultraviolet dan tampak"},
        {"question": "Apa itu cuvette?", "options": ["Wadah untuk larutan", "Alat untuk mengukur suhu", "Alat untuk mengukur tekanan"], "answer": "Wadah untuk larutan"},
        {"question": "Apa yang dimaksud dengan efek sel?", "options": ["Perubahan absorbansi akibat konsentrasi", "Perubahan suhu akibat cahaya", "Perubahan tekanan akibat cahaya"], "answer": "Perubahan absorbansi akibat konsentrasi"},
        {"question": "Apa itu spektrofotometer UV-Vis?", "options": ["Alat untuk mengukur cahaya ultraviolet dan tampak", "Alat untuk mengukur suhu", "Alat untuk mengukur tekanan"], "answer": "Alat untuk mengukur cahaya ultraviolet dan tampak"},
    ],
    "Kimia Fisika": [
        {"question": "Apa hukum pertama termodinamika?", "options": ["Energi tidak dapat diciptakan atau dimusnahkan", "Energi dapat diciptakan", "Energi selalu meningkat"], "answer": "Energi tidak dapat diciptakan atau dimusnahkan"},
        {"question": "Apa itu entropi?", "options": ["Ukuran ketidakteraturan", "Ukuran energi", "Ukuran massa"], "answer": "Ukuran ketidakteraturan"},
        {"question": "Apa yang dimaksud dengan energi potensial?", "options": ["Energi yang dimiliki benda karena posisinya", "Energi yang dimiliki benda karena gerakannya", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang dimiliki benda karena posisinya"},
        {"question": "Apa itu energi kinetik?", "options": ["Energi yang dimiliki benda karena gerakannya", "Energi yang dimiliki benda karena posisinya", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang dimiliki benda karena gerakannya"},
        {"question": "Apa yang dimaksud dengan hukum kedua termodinamika?", "options": ["Energi selalu mengalir dari yang panas ke yang dingin", "Energi tidak dapat diciptakan atau dimusnahkan", "Energi selalu meningkat"], "answer": "Energi selalu mengalir dari yang panas ke yang dingin"},
        {"question": "Apa itu kalor?", "options": ["Energi yang berpindah karena perbedaan suhu", "Energi yang dihasilkan oleh reaksi kimia", "Energi yang dimiliki benda karena posisinya"], "answer": "Energi yang berpindah karena perbedaan suhu"},
        {"question": "Apa yang dimaksud dengan sistem tertutup?", "options": ["Sistem yang tidak dapat bertukar energi dengan lingkungan", "Sistem yang dapat bertukar energi dengan lingkungan", "Sistem yang tidak dapat bertukar materi dengan lingkungan"], "answer": "Sistem yang tidak dapat bertukar energi dengan lingkungan"},
        {"question": "Apa itu reaksi eksotermik?", "options": ["Reaksi yang melepaskan energi", "Reaksi yang menyerap energi", "Reaksi yang tidak melibatkan energi"], "answer": "Reaksi yang melepaskan energi"},
        {"question": "Apa yang dimaksud dengan reaksi endotermik?", "options": ["Reaksi yang melepaskan energi", "Reaksi yang menyerap energi", "Reaksi yang tidak melibatkan energi"], "answer": "Reaksi yang menyerap energi"},
        {"question": "Apa itu hukum kekekalan energi?", "options": ["Energi tidak dapat diciptakan atau dimusnahkan", "Energi dapat diciptakan", "Energi selalu meningkat"], "answer": "Energi tidak dapat diciptakan atau dimusnahkan"},
        {"question": "Apa yang dimaksud dengan tekanan?", "options": ["Gaya per satuan luas", "Energi per satuan volume", "Massa per satuan volume"], "answer": "Gaya per satuan luas"},
        {"question": "Apa itu volume?", "options": ["Ruang yang ditempati oleh suatu benda", "Massa per satuan luas", "Energi per satuan volume"], "answer": "Ruang yang ditempati oleh suatu benda"},
        {"question": "Apa yang dimaksud dengan suhu?", "options": ["Ukuran energi kinetik rata-rata partikel", "Ukuran massa", "Ukuran volume"], "answer": "Ukuran energi kinetik rata-rata partikel"},
        {"question": "Apa itu gas ideal?", "options": ["Gas yang mengikuti hukum gas ideal", "Gas yang tidak memiliki volume", "Gas yang tidak dapat ditekan"], "answer": "Gas yang mengikuti hukum gas ideal"},
        {"question": "Apa yang dimaksud dengan hukum Boyle?", "options": ["Tekanan berbanding terbalik dengan volume pada suhu tetap", "Tekanan berbanding lurus dengan volume pada suhu tetap", "Volume berbanding lurus dengan suhu pada tekanan tetap"], "answer": "Tekanan berbanding terbalik dengan volume pada suhu tetap"},
        {"question": "Apa itu hukum Charles?", "options": ["Volume berbanding lurus dengan suhu pada tekanan tetap", "Tekanan berbanding terbalik dengan volume pada suhu tetap", "Volume berbanding terbalik dengan tekanan pada suhu tetap"], "answer": "Volume berbanding lurus dengan suhu pada tekanan tetap"},
        {"question": "Apa yang dimaksud dengan hukum Avogadro?", "options": ["Volume gas berbanding lurus dengan jumlah mol pada suhu dan tekanan tetap", "Tekanan berbanding terbalik dengan volume pada suhu tetap", "Volume berbanding lurus dengan suhu pada tekanan tetap"], "answer": "Volume gas berbanding lurus dengan jumlah mol pada suhu dan tekanan tetap"},
        {"question": "Apa itu energi bebas Gibbs?", "options": ["Energi yang tersedia untuk melakukan kerja", "Energi yang tidak dapat digunakan", "Energi yang dihasilkan oleh reaksi kimia"], "answer": "Energi yang tersedia untuk melakukan kerja"},
        {"question": "Apa yang dimaksud dengan reaksi redoks?", "options": ["Reaksi yang melibatkan transfer elektron", "Reaksi yang tidak melibatkan transfer elektron", "Reaksi yang melibatkan perubahan suhu"], "answer": "Reaksi yang melibatkan transfer elektron"},
        {"question": "Apa itu katalis?", "options": ["Zat yang mempercepat reaksi tanpa ikut bereaksi", "Zat yang memperlambat reaksi", "Zat yang tidak berpengaruh pada reaksi"], "answer": "Zat yang mempercepat reaksi tanpa ikut bereaksi"},
        {"question": "Apa yang dimaksud dengan pH?", "options": ["Ukuran keasaman atau kebasaan suatu larutan", "Ukuran konsentrasi", "Ukuran energi"], "answer": "Ukuran keasaman atau kebasaan suatu larutan"},
    ],
    "Biokimia": [
        {"question": "Apa itu enzim?", "options": ["Katalisator biologis", "Zat pewarna", "Zat pengawet"], "answer": "Katalisator biologis"},
        {"question": "Apa yang dimaksud dengan metabolisme?", "options": ["Proses penguraian makanan", "Proses pembentukan energi", "Proses pengolahan limbah"], "answer": "Proses penguraian makanan"},
        {"question": "Apa itu asam amino?", "options": ["Penyusun protein", "Penyusun karbohidrat", "Penyusun lemak"], "answer": "Penyusun protein"},
        {"question": "Apa yang dimaksud dengan DNA?", "options": ["Materi genetik", "Zat pewarna", "Zat pengawet"], "answer": "Materi genetik"},
        {"question": "Apa itu RNA?", "options": ["Asam ribonukleat", "Asam deoksiribonukleat", "Asam amino"], "answer": "Asam ribonukleat"},
        {"question": "Apa yang dimaksud dengan glukosa?", "options": ["Karbohidrat sederhana", "Lemak", "Protein"], "answer": "Karbohidrat sederhana"},
        {"question": "Apa itu lipid?", "options": ["Zat yang tidak larut dalam air", "Zat yang larut dalam air", "Zat yang tidak berfungsi dalam tubuh"], "answer": "Zat yang tidak larut dalam air"},
        {"question": "Apa yang dimaksud dengan karbohidrat?", "options": ["Sumber energi utama", "Sumber protein", "Sumber lemak"], "answer": "Sumber energi utama"},
        {"question": "Apa itu protein?", "options": ["Penyusun sel", "Sumber energi", "Zat pewarna"], "answer": "Penyusun sel"},
        {"question": "Apa yang dimaksud dengan metabolisme anaerob?", "options": ["Proses metabolisme tanpa oksigen", "Proses metabolisme dengan oksigen", "Proses metabolisme dengan suhu tinggi"], "answer": "Proses metabolisme tanpa oksigen"},
        {"question": "Apa itu fotosintesis?", "options": ["Proses pembentukan glukosa dari cahaya", "Proses penguraian glukosa", "Proses pembentukan energi dari lemak"], "answer": "Proses pembentukan glukosa dari cahaya"},
        {"question": "Apa yang dimaksud dengan respirasi seluler?", "options": ["Proses penguraian glukosa untuk menghasilkan energi", "Proses pembentukan glukosa", "Proses penguraian lemak"], "answer": "Proses penguraian glukosa untuk menghasilkan energi"},
        {"question": "Apa itu ATP?", "options": ["Molekul penyimpan energi", "Molekul penyimpan lemak", "Molekul penyimpan protein"], "answer": "Molekul penyimpan energi"},
        {"question": "Apa yang dimaksud dengan enzim katalase?", "options": ["Enzim yang menguraikan hidrogen peroksida", "Enzim yang menguraikan glukosa", "Enzim yang menguraikan lemak"], "answer": "Enzim yang menguraikan hidrogen peroksida"},
        {"question": "Apa itu hormon?", "options": ["Zat pengatur dalam tubuh", "Zat penyusun sel", "Zat penyimpan energi"], "answer": "Zat pengatur dalam tubuh"},
        {"question": "Apa yang dimaksud dengan asam lemak?", "options": ["Penyusun lipid", "Penyusun protein", "Penyusun karbohidrat"], "answer": "Penyusun lipid"},
        {"question": "Apa itu glikogen?", "options": ["Cadangan energi pada hewan", "Cadangan energi pada tumbuhan", "Cadangan energi pada bakteri"], "answer": "Cadangan energi pada hewan"},
        {"question": "Apa yang dimaksud dengan sel?", "options": ["Unit dasar kehidupan", "Unit dasar energi", "Unit dasar protein"], "answer": "Unit dasar kehidupan"},
        {"question": "Apa itu biokimia?", "options": ["Ilmu tentang reaksi kimia dalam makhluk hidup", "Ilmu tentang reaksi fisika", "Ilmu tentang reaksi kimia dalam benda mati"], "answer": "Ilmu tentang reaksi kimia dalam makhluk hidup"},
        {"question": "Apa yang dimaksud dengan metabolisme aerob?", "options": ["Proses metabolisme dengan oksigen", "Proses metabolisme tanpa oksigen", "Proses metabolisme dengan suhu tinggi"], "answer": "Proses metabolisme dengan oksigen"},
        {"question": "Apa itu enzim amilase?", "options": ["Enzim yang menguraikan karbohidrat", "Enzim yang menguraikan protein", "Enzim yang menguraikan lemak"], "answer": "Enzim yang menguraikan karbohidrat"},
    ],
    "Fisika": [
        {"question": "Perpindahan, kecepatan, percepatan, dan gaya termasuk besaran?", "options": ["Skalar", "Vektor", "Turunan","Satuan","Utama"], "answer": "Vektor"},
        {"question": "Daya adalah ?", "options": ["Joule/sekon", "Joule.sekon", "Newton/sekon","Newton.sekon","Joule"], "answer": "Joule/sekon"},
        {"question": "Dua lembah dan dua bukit gelombang sama dengan?", "options": ["1/2 lambda", "1 lambda", "1,5 lambda","2 lambda","2,5 lambda"], "answer": "2 lambda"}, 
        {"question": "Diantara besaran dibawah ini, manakah yang termasuk besaran pokok ?", "options": ["Kecepatan", "Percepatan", "Jumlah zat","Kadar","Energi"], "answer": "Kadar"},
        {"question": "Pada kasus benda jatuh, energi yang besarnya semakin berkurang adalah?", "options": ["Energi potensial", "Energi kinetik", "Energi gerak","Energi  gesekan","Energi mekanik"], "answer": "Energi mekanin"},
        {"question": "Usaha yang dilakukan oleh gaya gesek selalu bernilai?", "options": ["Positif", "Negatif", "Tergantung kemiringan","Tergantung sudut","Nol"], "answer": "Nol"},
        {"question": "Penulisan simbol yang benar untuk satuan mililiter yaitu?", "options": ["ml", "mL", "Ml","ML","mLiter"], "answer": "mL"},
        {"question": "Perbandingan massa benda terhada[ volume benda disebut?", "options": ["Berat jenis", "Bobot jenis", "Massa jenis","Massa jenis relative","Specific gravity"], "answer": "Massa jenis"},
        {"question": "Gerak harmonis sederhana memiliki amplitudo yang besarnya?", "options": ["Selalu sama", "Selalu bertambah besar", "Selalu berkurang","Tergantung massa beban","Selalu berubah ubah"], "answer": "Selalu sama"},
        {"question": "Jika gaya berat benda lebih besar dari gaya apung maka benda akan?", "options": ["Terapung seluruhnya", "Terapung sebagian", "Melayang diatas","Melayang ditengah","Tenggelam di dasar"], "answer": "Melayang diatas"},
        {"question": "Pernyataan di bawah ini yang bukan syarat pasangan gaya bisa disebut aksi reaksi yaitu?", "options": ["Berlawanan arah", "Sama besar", "Bekerja pada benda yang sama","Bekerja pada benda yang berbeda","Semua jawaban benar"], "answer": "Sama besar"},
        {"question": "Diantara besarab besaran berikut,manakah yang tidak terkait dengan kinematika?", "options": ["Perpindahan", "Waktu", "Percepatan","Gaya","Kecepatan"], "answer": "Gaya"},
        {"question": "Prinsip.... menyatakan bahwa tekanan yang diberikan pada fluida tertutup akan diteruskan sama besar ke segala arah", "options": ["Pascal", "Bernoulli", "Archimedes","Tegangan permukaan","Viskositas"], "answer": "Pascal"},
        {"question": "Penyeban perubahan gerak benda adalahh?", "options": ["Usaha", "Gaya", "Energi","Percepatan","Kecepatan"], "answer": "Kecepatan"},
        {"question": "Suatu thermometer menunjukan suhu 30 Celcius, berapakah dinyatakan dalam skala fahrenheit?", "options": ["78", "54", "86","77","90"], "answer": "78"}, 
    ]
}

# Halaman Beranda
if menu == "Beranda":
    st.title("🧠 MindTrack")
    st.write("Selamat datang di *MindTrack*, platform latihan soal dan catatan kuliah 👋")
    st.info("Gunakan menu di sebelah kiri untuk mulai belajar.")

elif menu == "Latihan Soal":
    st.title("✏ Latihan Soal")

    # Pilih Mata Kuliah
    matkul = st.selectbox("Pilih Mata Kuliah", ["Spektrofotometri", "Kimia Fisika", "Biokimia","Fisika"])

    # Tampilkan Soal Berdasarkan Mata Kuliah
    st.subheader(f"Soal {matkul}")
    jawaban = []
    for index, soal in enumerate(soal_data[matkul]):
        st.subheader(f"{index + 1}. {soal['question']}")
        jawaban.append(st.radio("Pilih jawaban:", soal["options"], key=f"soal_{matkul}_{index}"))

    # TOMBOL KIRIM
    if st.button("✅ Kirim Jawaban"):
        st.success("Jawaban kamu berhasil dikirim!")
        # Koreksi otomatis
        skor = 0
        for index, soal in enumerate(soal_data[matkul]):
            if jawaban[index] == soal["answer"]:
                skor += 1

        # Tampilkan hasil
        st.markdown(f"### 🏆 Skor Akhir: *{skor}/{len(soal_data[matkul])}*")

#catatan 
if menu == "Catatan Kuliah":
    st.title("📒 Catatan Kuliah")

    # Inisialisasi session_state jika belum ada
    if "selected_matkul_simple" not in st.session_state:
        st.session_state.selected_matkul_simple = None
    if "selected_pertemuan_simple" not in st.session_state:
        st.session_state.selected_pertemuan_simple = None

    # Dropdown Mata Kuliah
    matkul_options = ["Kimia Fisika", "Spektrofotometri", "Biokimia"]
    selected_matkul = st.selectbox("Pilih Mata Kuliah", matkul_options, key="matkul_dropdown_simple")

    # Jika mata kuliah dipilih (saat selectbox berubah)
    if selected_matkul != st.session_state.selected_matkul_simple:
        st.session_state.selected_matkul_simple = selected_matkul
        st.session_state.selected_pertemuan_simple = None # Reset pertemuan jika matkul berubah
        # Tidak perlu st.experimental_rerun() di sini, Streamlit akan reruns secara otomatis

    # Tampilkan tombol pertemuan hanya jika mata kuliah sudah dipilih
    if st.session_state.selected_matkul_simple:
        st.subheader(f"Catatan untuk {st.session_state.selected_matkul_simple}")
        st.markdown("---")
        st.write("Pilih Pertemuan:")
        
        cols = st.columns(3) # Membuat 3 kolom untuk tombol pertemuan
        
        for i in range(1, 4): # Untuk pertemuan 1, 2, 3
            with cols[i-1]:
                # Gunakan on_click callback untuk mengubah session state
                def set_pertemuan_simple(pertemuan_num):
                    st.session_state.selected_pertemuan_simple = pertemuan_num
                
                st.button(f"Pertemuan {i}", key=f"pertemuan_btn_simple_{i}", on_click=set_pertemuan_simple, args=(i,))

        # Menampilkan Konten Pertemuan
        if st.session_state.selected_pertemuan_simple:
            st.markdown("---")
            st.subheader(f"Konten Pertemuan {st.session_state.selected_pertemuan_simple}")
            st.write(f"Ini adalah detail untuk **{st.session_state.selected_matkul_simple}** - **Pertemuan {st.session_state.selected_pertemuan_simple}**.")
            
            # Anda bisa menambahkan logika konten spesifik berdasarkan mata kuliah dan pertemuan di sini
            if st.session_state.selected_matkul_simple == "Kimia Fisika":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Materi Kimia Fisika Pertemuan 1: Pengantar Termodinamika.")
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Materi Kimia Fisika Pertemuan 2: Entropi dan Energi Bebas.")
                elif st.session_state.selected_pertemuan_simple == 3:
                    st.write("Materi Kimia Fisika Pertemuan 3: Kinetika Reaksi.")
            
            elif st.session_state.selected_matkul_simple == "Spektrofotometri":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Materi Spektrofotometri Pertemuan 1: Prinsip Dasar UV-Vis.")
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Materi Spektrofotometri Pertemuan 2: Aplikasi dalam Analisis Kuantitatif.")
                elif st.session_state.selected_pertemuan_simple == 3:
                    st.write("Materi Spektrofotometri Pertemuan 3: Spektrofotometri Serapan Atom (AAS).")
            
            elif st.session_state.selected_matkul_simple == "Biokimia":
                if st.session_state.selected_pertemuan_simple == 1:
                    st.write("Materi Biokimia Pertemuan 1: Struktur Karbohidrat dan Lipid.")
                elif st.session_state.selected_pertemuan_simple == 2:
                    st.write("Materi Biokimia Pertemuan 2: Enzim dan Katalisis Biologis.")
                elif st.session_state.selected_pertemuan_simple == 3:
                    st.write("Materi Biokimia Pertemuan 3: Metabolisme Energi.")
        else:
            st.info("Silakan pilih pertemuan di atas untuk melihat detail.")
    else:
        st.info("Silakan pilih mata kuliah di atas.")# Halaman Riwayat Jawaban
elif menu == "Riwayat Jawaban":
    st.title("🗂 Riwayat Jawaban")
    st.write("Di sini akan ditampilkan jawaban-jawaban soal yang pernah kamu kerjakan.")

# Halaman Tentang
elif menu == "Tentang":
    st.title("ℹ Tentang MindTrack")
    st.write("Website ini dibuat untuk latihan soal dan mencatat materi perkuliahan.")
    st.header("Tentang Pendiri")
    st.write("Zulfikar Syahid")
    st.write("Rizmi Maitri Nurgianti")
    st.write("Nafisah Nailalhusna I.")
    st.write("Jane Lazarina Bora Isu")
