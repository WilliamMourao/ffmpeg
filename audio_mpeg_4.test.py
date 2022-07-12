import os
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'

print('''
Informe os seguintes dados para realizar a conversão de uma mídia de audio:
            ________________________

            Midia de referência: std_audio_02_16_bit_depth_2_0_channel.wav ou std_audio_05_16_bit_depth_5_1_channel.wav
            Caminho de entrada: /home/login_usuário/pasta/
            Caminho de saída: /home/login_usuário/pasta/

            Exemplos:
            taxa de bits = 23k, 24K, 64k, 65K

            Menu Codec:

            [A] - MPEG-4 LC L2 
            [B] - MPEG-4 LC L4 
            [C] - MPEG-4 HE L2
            [D] - MPEG-4 HE L4


           __________________________


           ''')

# [E] - MPEG-4 HEv2 L2
# [F] - AC-3, E-AC-3
# [G] - AC-4

codec = str(input('Escolha uma letra do menu codec:'))
frequencia = 48000
taxa_de_bits = str(input('Escolha o tamanho da mídia (ex: 24k): '))

midia_2_0_channel = 'std_audio_02_16_bit_depth_2_0_channel.wav'
midia_5_1_channel = 'std_audio_05_16_bit_depth_5_1_channel.wav'
caminho_origem = '/home/william_mourao/Imagens/'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    caminho_completo = os.path.join(raiz)
    nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

if codec == "A".upper():
    comando = f' docker run -v {caminho_completo}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio1.mp4 '

if codec == "B".upper():
    comando = f' docker run -v {caminho_completo}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel}' \
              f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio2.mp4 '

if codec == "C".upper():
    comando = f' docker run -v {caminho_completo}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio3.mp4 '

if codec == "D".upper():
    comando = f' docker run -v {caminho_completo}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/midia4.mp4 '

    os.system(comando)
print(comando)