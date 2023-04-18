from AudioFilter import AudioFilter

if __name__ == '__main__':
    audio = AudioFilter("1.wav")
    while(True):
        print("1.LPF")
        print("2.HPF")
        print("3.BPF")
        print("4.BSF")
        print("5.EQ")
        print("6.OUT")
        lc = int(input("Nhap lua chon: "))
        match lc:
            case 1:
                audio.plot_waveform(audio.filter_signal_lpf)
                audio.plot_power_spectrum(audio.frequencies_lpf, audio.power_spectrum_lpf,audio.filtered_frequencies_lpf,
                                          audio.filtered_power_spectrum_lpf)
                audio.save_filtered_audio("lpf.wav", audio.filter_signal_lpf)
            case 2:
                audio.plot_waveform(audio.filter_signal_hpf)
                audio.plot_power_spectrum(audio.frequencies_hpf, audio.power_spectrum_hpf,audio.filtered_frequencies_hpf,
                                          audio.filtered_power_spectrum_hpf)
                audio.save_filtered_audio("hpf.wav", audio.filter_signal_hpf)

            case 3:
                audio.plot_waveform(audio.filter_signal_bpf)
                audio.plot_power_spectrum(audio.frequencies_bpf, audio.power_spectrum_bpf, audio.filtered_frequencies_bpf,
                                          audio.filtered_power_spectrum_bpf)
                audio.save_filtered_audio("bpf.wav", audio.filter_signal_bpf)
            case 4:
                audio.plot_waveform(audio.filter_signal_bsf)
                audio.plot_power_spectrum(audio.frequencies_bsf, audio.power_spectrum_bsf,audio.filtered_frequencies_bsf,
                                          audio.filtered_power_spectrum_bsf)
                audio.save_filtered_audio("bsf.wav", audio.filter_signal_bsf)
            case 5:
                audio.plot_waveform(audio.filter_signal_eq)
                audio.plot_power_spectrum(audio.frequencies_eq, audio.power_spectrum_eq, audio.filtered_frequencies_eq,
                                          audio.filtered_power_spectrum_eq)
                audio.save_filtered_audio("eq.wav", audio.filter_signal_eq)
            case 6:
                print("Bye")
                break
