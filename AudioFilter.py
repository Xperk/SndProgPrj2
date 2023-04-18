import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

class AudioFilter:
    def __init__(self, filename):
        self.filename = filename
        self.signal_data, self.rate = sf.read(filename)
        self.numtaps = 501
        self.nyquist_rate = self.rate / 2.0
        self.cutoff_lp = 5000
        self.cutoff_hp = 1000
        self.cutoff_bp = 2000
        self.cutoff_bsf = 7000

        self.lpf = signal.firwin(self.numtaps, self.cutoff_lp/self.nyquist_rate, window='hamming')
        self.hpf = signal.firwin(self.numtaps, self.cutoff_hp/self.nyquist_rate, pass_zero=False, window='hann')
        self.bpf = signal.firwin(self.numtaps, self.cutoff_bp/self.nyquist_rate, pass_zero=False, window='blackman')
        self.bsf = signal.firwin(self.numtaps, self.cutoff_bsf/self.nyquist_rate, pass_zero=False, window='hamming')

        self.filter_signal_lpf = signal.convolve(np.ravel(self.signal_data), self.lpf, mode='same')
        self.filter_signal_hpf = signal.convolve(np.ravel(self.signal_data), self.hpf, mode='same')
        self.filter_signal_bpf = signal.convolve(np.ravel(self.signal_data), self.bpf, mode='same')
        self.filter_signal_bsf = signal.convolve(np.ravel(self.signal_data), self.bsf, mode='same')
        self.eq_out = self.lpf + self.hpf + self.bpf + self.bsf
        self.filter_signal_eq = signal.convolve(np.ravel(self.signal_data), self.eq_out, mode='same')

        self.frequencies_lpf, self.power_spectrum_lpf = signal.welch(np.ravel(self.signal_data), self.rate, nperseg=1024)
        self.filtered_frequencies_lpf, self.filtered_power_spectrum_lpf = signal.welch(np.ravel(self.filter_signal_lpf), self.rate,nperseg=1024)

        self.frequencies_hpf, self.power_spectrum_hpf = signal.welch(np.ravel(self.signal_data), self.rate, nperseg=1024)
        self.filtered_frequencies_hpf, self.filtered_power_spectrum_hpf = signal.welch(np.ravel(self.filter_signal_hpf), self.rate, nperseg=1024)

        self.frequencies_bpf, self.power_spectrum_bpf = signal.welch(np.ravel(self.signal_data), self.rate, nperseg=1024)
        self.filtered_frequencies_bpf, self.filtered_power_spectrum_bpf = signal.welch(np.ravel(self.filter_signal_bpf), self.rate, nperseg=1024)

        self.frequencies_bsf, self.power_spectrum_bsf = signal.welch(np.ravel(self.signal_data), self.rate, nperseg=1024)
        self.filtered_frequencies_bsf, self.filtered_power_spectrum_bsf = signal.welch(np.ravel(self.filter_signal_bsf), self.rate, nperseg=1024)

        self.frequencies_eq, self.power_spectrum_eq = signal.welch(np.ravel(self.signal_data), self.rate, nperseg=1024)
        self.filtered_frequencies_eq, self.filtered_power_spectrum_eq = signal.welch(np.ravel(self.filter_signal_eq), self.rate, nperseg=1024)
    def plot_waveform(self,filter_type):
        fig, ax = plt.subplots(2, 1, figsize=(12, 8))
        ax[0].plot(np.ravel(self.signal_data))
        ax[0].set_title("Tín hiệu dạng sóng thời gian trước khi lọc")
        ax[1].plot(np.ravel(filter_type))
        ax[1].set_title("Tín hiệu dạng sóng thời gian sau khi lọc")
        plt.tight_layout()
        plt.show()

    def plot_power_spectrum(self,prefre,prepow,lastfre,lastpow):
        fig, ax = plt.subplots(2, 1, figsize=(12, 8))
        ax[0].semilogy(np.ravel(prefre), prepow)
        ax[0].set_title("Đồ hình phổ biên độ trước khi lọc")
        ax[0].set_xlabel("Tần số (Hz)")
        ax[0].set_ylabel("Cường độ")
        ax[1].semilogy(np.ravel(lastfre), lastpow)
        ax[1].set_title("Đồ hình phổ biên độ sau khi lọc")
        ax[1].set_xlabel("Tần số (Hz)")
        ax[1].set_ylabel("Cường độ")
        plt.tight_layout()
        plt.show()

    def save_filtered_audio(self, output_filename, data):
        sf.write(output_filename, data, self.rate)


