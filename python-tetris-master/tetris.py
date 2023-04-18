import pygame
import random
from tetris import Tetris

# Inisialisasi Pygame
pygame.init()

# Konstanta game
ukuran_blok = 20
lebar_layar = 10 * ukuran_blok
tinggi_layar = 20 * ukuran_blok
hitam = (0, 0, 0)
putih = (255, 255, 255)
merah = (255, 0, 0)
biru = (0, 0, 255)
hijau = (0, 255, 0)
kuning = (255, 255, 0)
warna_blok = [merah, biru, hijau, kuning]
bentuk_blok = [[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
               [[0, 2, 2], [2, 2, 0], [0, 0, 0]],
               [[3, 3, 0], [0, 3, 3], [0, 0, 0]],
               [[4, 0, 0], [4, 4, 4], [0, 0, 0]],
               [[0, 0, 5], [5, 5, 5], [0, 0, 0]],
               [[0, 6, 0], [6, 6, 6], [0, 0, 0]],
               [[7, 7, 7, 7], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

# Font
font = pygame.font.SysFont(None, 30)

# Membuat layar
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Game Tetris")

# Kelas Blok
class Blok:
    def __init__(self, bentuk, warna):
        self.bentuk = bentuk
        self.warna = warna
        self.x = lebar_layar // 2 - ukuran_blok * len(bentuk[0]) // 2
        self.y = 0
        self.rotasi = 0

    def gambar(self):
        for i in range(3):
            for j in range(3):
                if self.bentuk[self.rotasi][i][j] == 1:
                    pygame.draw.rect(layar, self.warna, (self.x + j * ukuran_blok, self.y + i * ukuran_blok, ukuran_blok, ukuran_blok), 0)

    def jatuh(self):
        self.y += ukuran_blok

# Kelas Papan_Permainan
class Papan_Permainan:
    def __init__(self, lebar, tinggi):
        self.data = [[putih for _ in range(lebar)] for _ in range(tinggi)]
        self.tinggi = tinggi
        self.lebar = lebar

    # Indent the block of code for cek_kolisi function
    def cek_kolisi(self, blok, x=0, y=0):
        for i in range(3):
            for j in range(3):
                if blok.bentuk[blok.rotasi][i][j] == 1:
                    x_pos = blok.x + j * ukuran_blok + x
                    y_pos = blok.y + i * ukuran_blok + y
                    if x_pos < 0 or x_pos > lebar_layar - ukuran_blok or y_pos > tinggi_layar - ukuran_blok or self.data[y_pos // ukuran_blok][x_pos // ukuran_blok] != putih:
                        return True
        return False


# Proses Benturan
    def proses_benturan(self, blok):
        for i in range(3):
            for j in range(3):
                if blok.bentuk[blok.rotasi][i][j] == 1:
                    x_pos = blok.x + j * ukuran_blok
                    y_pos = blok.y + i * ukuran_blok
                    self.data[y_pos // ukuran_blok][x_pos // ukuran_blok] = blok.warna
        self.hapus_baris_penuh()
        self.buat_blok_baru()

    def cek_gameover(self):
        for j in range(self.lebar):
            if self.data[0][j] != putih:
                return True
        return False

    def akhir_permainan(self):
        font = pygame.font.SysFont("comicsansms", 72)
        teks = font.render("Game Over", True, merah)
        layar.blit(teks, (lebar_layar // 2 - teks.get_width() // 2, tinggi_layar // 2 - teks.get_height() // 2))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def jalankan_permainan(self):
        blok = self.buat_blok_baru()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        blok.geser_kiri(self)
                    elif event.key == pygame.K_RIGHT:
                        blok.geser_kanan(self)
                    elif event.key == pygame.K_DOWN:
                        blok.jatuh_cepat(self)
                    elif event.key == pygame.K_UP:
                        blok.putar(self)

            layar.fill(hitam)
            waktu_sekarang = pygame.time.get_ticks()

            if waktu_sekarang - self.waktu_pergerakan >= kecepatan_pergerakan:
                blok.jatuh(self)
                self.waktu_pergerakan = waktu_sekarang

            self.gambar()
            pygame.display.update()

            if self.cek_kolisi(blok):
                self.proses_benturan(blok)
                if self.cek_gameover():
                    self.akhir_permainan()
                blok = self.buat_blok_baru()
            
            waktu_sekarang = pygame.time.get_ticks()
            if waktu_sekarang - self.waktu_pergerakan >= kecepatan_pergerakan:
                self.waktu_pergerakan = waktu_sekarang

if __name__ == '__main__':
    pygame.init()
    tetris = Tetris()
    tetris.jalankan_permainan()

    
