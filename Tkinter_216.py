import tkinter as tk  # Import library tkinter untuk membuat GUI
from tkinter import messagebox  # Import messagebox untuk menampilkan pesan kesalahan

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Iterasi untuk setiap input nilai di dalam entries
        for entry in entries:
            nilai = int(entry.get())  # Konversi input menjadi integer
            # Periksa apakah nilai berada di rentang 0 hingga 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Menampilkan prediksi jika semua nilai valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Tampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Inisialisasi aplikasi GUI dengan Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Set judul jendela aplikasi
root.geometry("500x600")  # Tentukan ukuran jendela
root.configure(bg="#f0f0f0")  # Set warna latar belakang

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Tempatkan judul aplikasi di bagian atas dengan padding

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")  
frame_input.pack(pady=10)  # Tempatkan frame untuk input di bawah judul

entries = []  # List untuk menyimpan entry nilai mata pelajaran
for i in range(10):
    # Label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran{i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Tempatkan label di kolom pertama dengan padding
    
    # Entry untuk setiap nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Tempatkan entry di kolom kedua dengan padding
    entries.append(entry)  # Tambahkan entry ke dalam list entries

# Tombol untuk melakukan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Tempatkan tombol di bawah input nilai

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Tempatkan label hasil di bawah tombol

# Jalankan aplikasi
root.mainloop()
