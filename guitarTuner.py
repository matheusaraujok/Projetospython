import numpy as np
import sounddevice as sd
import tkinter as tk
from tkinter import messagebox

# Frequências padrão das cordas do violão
GUITAR_FREQUENCIES = {
    "E (Mi Baixo)": 82.41,
    "A (Lá)": 110.00,
    "D (Ré)": 146.83,
    "G (Sol)": 196.00,
    "B (Si)": 246.94,
    "E (Mi Agudo)": 329.63,
}

# Parâmetros do áudio
SAMPLE_RATE = 44100
DURATION = 1  # Duração da captura (segundos)

class GuitarTunerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Afinador de Violão 🎸")
        
        # Interface gráfica
        self.label_freq = tk.Label(root, text="Frequência Detectada: -- Hz", font=("Arial", 16))
        self.label_freq.pack(pady=10)
        
        self.label_note = tk.Label(root, text="Corda Sugerida: --", font=("Arial", 16))
        self.label_note.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Iniciar Captura", command=self.start_tuning, font=("Arial", 14))
        self.start_button.pack(pady=20)

    def detect_frequency(self, audio_data):
        """Detecta a frequência dominante no áudio."""
        fft_result = np.fft.rfft(audio_data)
        freqs = np.fft.rfftfreq(len(audio_data), d=1/SAMPLE_RATE)
        magnitude = np.abs(fft_result)
        peak_idx = np.argmax(magnitude)
        return freqs[peak_idx]

    def get_closest_string(self, freq):
        """Retorna a corda mais próxima da frequência detectada."""
        closest_string = min(GUITAR_FREQUENCIES, key=lambda note: abs(GUITAR_FREQUENCIES[note] - freq))
        return closest_string, GUITAR_FREQUENCIES[closest_string]

    def start_tuning(self):
        """Captura áudio e exibe a afinação em tempo real."""
        try:
            audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float64')
            sd.wait()
            freq = self.detect_frequency(audio_data.flatten())

            if freq > 20:  # Ignorar ruídos baixos
                closest_string, target_freq = self.get_closest_string(freq)
                self.label_freq.config(text=f"Frequência Detectada: {freq:.2f} Hz")
                self.label_note.config(text=f"Corda Sugerida: {closest_string} ({target_freq:.2f} Hz)")

                if abs(freq - target_freq) < 1:
                    messagebox.showinfo("Afinador", "Afinação Correta!")
                else:
                    ajuste = "abaixar" if freq > target_freq else "subir"
                    messagebox.showinfo("Ajuste Necessário", f"Ajuste para {ajuste} a tensão.")
            else:
                messagebox.showerror("Erro", "Som não detectado. Tente novamente.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao capturar áudio: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarTunerApp(root)
    root.mainloop()
