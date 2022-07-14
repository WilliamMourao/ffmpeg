import os
import sys
import shutil


if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
    comando_mp2enc = 'mp2enc'

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


print('exemplo: /home/william_mourao/Imagens/')
caminho_origem = str(input('Informe o local onde está a sua midia de audio: '))
codec = str(input('Escolha uma letra do menu codec:'))
frequencia = 48000
taxa_de_bits = str(input('Escolha o tamanho do Bit rate (ex: 24k): '))


midia_2_0_channel = 'std_audio_02_16_bit_depth_2_0_channel.wav'
midia_5_1_channel = 'std_audio_05_16_bit_depth_5_1_channel.wav'


for raiz, pastas, arquivos in os.walk(caminho_origem):
    caminho_completo = os.path.join(raiz)
    nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)


if codec == "A".upper():
    comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

if codec == "B".upper():
    comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

if codec == "C".upper():
    comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

if codec == "D".upper():
    comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel} ' \
              f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '


os.system(comando)
print(comando)

print('=================================================')
print('Exemplo midia gerada: /home/william_mourao/Imagens/audio.mp4')
print('Exemplo midia gerada: /home/william_mourao/Imagens/saida/')
print('=================================================')

src = str(input('Informe o local onde está salvo a mídia gerada: '))
des = str(input('Informe o local para salvar uma cópia da mídia: '))
shutil.copy2(src, des)

print(' =====================================')
print('      Renomear o arquivo gerado: ')
print(' =====================================')

novo_nome = str(input('Informe o nome da mídia: '))
extensao = str(input('Informe o tipo de extensão (ex: mpg,mp1,mp2,mp3,mp4): '))

folder = des

for file_name in os.listdir(folder):
    old_name = folder + file_name
    new_name = folder + novo_nome + '.' + extensao
    os.rename(old_name, new_name)

os.remove(src)

print('*** Mídia Gerada com Sucesso ***')

