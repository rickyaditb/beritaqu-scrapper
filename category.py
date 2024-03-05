def categorize(string):
  string = string.lower()

  category_words = {
    'Politik': ['coblos', 'megawati', 'demokrasi', 'pemilu', 'kandidat', 'partai politik', 'calon presiden', 'debat', 'kampanye', 'suara rakyat', 'koalisi', 'kontestasi', 'undang-undang', 'parlemen', 'ketua partai', 'kabinet', 'oposisi', 'korupsi', 'reformasi', 'pemungutan suara', 'kampanye hitam', 'pemilih', 'pemimpin', 'ketidaksetujuan', 'kebijakan', 'pengawasan', 'partai', 'dpr', 'anies', 'ganjar', 'prabowo', 'gibran', 'jokowi', 'pdip', 'gerindra', 'pks', 'imin', 'mahfud', 'ppp', 'psi'],
    'Olahraga': ["juara", "skor", "tim", "pelatih", "pemain", "gol", "laga", "turnamen", "klasemen", "rekor", "pertandingan", "penalti", "kiper", "kemenangan", "kekalahan", "seri", "prestasi", "performa", "piala", "medali", "olimpiade", "kejuaraan", "lapangan", "arena", "stadion", "perlengkapan", "pelanggaran", "wasit", "kesehatan", "kebugaran", "latihan", "strategi", "taktik", "skandal", "doping", "transfer", "kontrak", "penghargaan", "cedera", "prestise", "rivalitas", "penggemar", "kompetisi", "pengumuman", "pengundian", "pemilihan"],
    'Teknologi': [ "inovasi", "digitalisasi", "kecerdasan buatan", "big data", "internet of things", "blockchain", "cybersecurity", "cloud computing", "e-commerce", "aplikasi mobile", "siber", "algoritma", "platform", "sensor", "keamanan data", "perangkat keras", "perangkat lunak", "teknologi wearable", "virtual reality", "augmented reality", "5g", "autonomous vehicles", "robotika", "drones", "gadget", "streaming", "gaming", "startup", "sosial media", "eksplorasi ruang angkasa", "teknologi medis", "pengembangan web", "konektivitas", "kecepatan internet", "pemrosesan data", "keberlanjutan teknologi", "kendaraan listrik", "teknologi 3d printing", "keamanan jaringan", "kamera pintar", "google", "apple", "microsoft", "android", "iphone", "youtube", "teknologi", "informasi", "komputer", "internet", "pemrograman", "aplikasi", "sains", "morfologi", "jaringan", "digital", "sistem", "database", "hardware", "software", "elektronik", "komunikasi", "canggih", "otomatisasi", "mobile" ],
    'Ekonomi': ["ekonomi", "bisnis", "pasar", "keuangan", "uang", "investasi", "saham", "obligasi", "inflasi", "deflasi", "resesi", "pertumbuhan", "pdb", "pengangguran", "kemiskinan", "suku bunga", "nilai tukar", "harga", "minyak", "emas", "komoditas", "ekspor", "impor", "neraca perdagangan", "utang", "defisit", "surplus", "bank", "perusahaan", "industri", "sektor", "konsumsi", "produksi", "pengiriman", "laba", "kerugian", "pajak", "subsidi", "regulasi", "kebijakan", "globalisasi", "perdagangan bebas", "krisis", "pemulihan", "inovasi", "teknologi", "infrastruktur", "pembangunan", "berkelanjutan", "kesejahteraan", "gaji"],
    'Kesehatan': ["kesehatan", "penyakit", "virus", "bakteri", "obat", "vaksin", "pandemi", "epidemi", "gejala", "pengobatan", "pencegahan", "dokter", "perawat", "rumah sakit", "klinik", "puskesmas", "bpjs kesehatan", "gizi", "olahraga", "gaya hidup", "mental", "fisik", "stres", "depresi", "kanker", "jantung", "diabetes", "stroke", "alzheimer", "hiv/aids", "tuberkulosis", "malaria", "demam berdarah", "covid-19", "imunitas", "kebersihan", "sanitasi", "air bersih", "polusi", "lingkungan", "genetika", "riset", "teknologi", "inovasi", "kesehatan digital", "telemedicine", "kesehatan ibu dan anak", "lansia", "disabilitas", "covid", "kemenkes"],
    'Internasional': ["internasional", "dunia", "negara", "politik", "diplomasi", "ekonomi", "perang", "damai", "konflik", "krisis", "terorisme", "bencana alam", "hak asasi manusia", "pengungsi", "migran", "lingkungan hidup", "perubahan iklim", "globalisasi", "perdagangan bebas", "pbb", "uni eropa", "nato", "g20", "imf", "bank dunia", "regionalisme", "budaya", "olahraga", "teknologi", "sains", "inovasi", "pandemi", "covid-19", "vaksin", "ekonomi global", "krisis energi", "inflasi", "rantai pasokan", "keamanan pangan", "kesenjangan", "pembangunan berkelanjutan", "demokrasi", "otoritarianisme", "kebebasan", "hak asasi manusia", "keadilan", "kesetaraan", "toleransi", "kerjasama internasional", "perdamaian dunia", "amerika", "china", "rusia", "ukraina", "jerman", "inggris", "prancis", "jepang", "india", "korea", "palestina", "israel", "hamas", "covid", "kemenkes"]
  }

  category_counts = {category: sum(word in string for word in words) for category, words in category_words.items()}

  max_count = max(category_counts.values())
  max_categories = [category for category, count in category_counts.items() if count == max_count]

  if len(max_categories) == 1:
    return max_categories[0]
  else:
    return 'Umum'