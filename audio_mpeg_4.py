import os
import sys
import shutil

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'


def menu_mpeg4():

        print('''
        
             *********************************
               ***Você escolheu MPEG-4***
             *********************************

        Informe os seguintes dados para realizar a conversão de uma mídia de audio:
                    
        Midia de referência: std_audio_02_16_bit_depth_2_0_channel.wav ou std_audio_05_16_bit_depth_5_1_channel.wav
        Caminho de entrada: /home/login_usuário/pasta/
        Caminho de saída: /home/login_usuário/pasta/
        
                ________________________
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

        # =================
        # DADOS DE ENTRADA
        # =================

def dados_de_entrada():
        print('exemplo: /home/william_mourao/Imagens/')
        caminho_origem = str(input('Informe o local onde está a sua midia de audio: '))
        codec = str(input('Escolha uma letra do menu codec:'))
        frequencia = 48000
        print('''taxa de Bit rate: 
        
                    [A] - 23k
                    [B] - 24k
                    [C] - 64k
                    [D] - 65k   
        
        ''')
        taxa_de_bits = str(input('Escolha o tamanho do Bit rate: '))

        if taxa_de_bits.upper() == "A":
            taxa_de_bits = '23k'
        elif taxa_de_bits.upper() == "B":
            taxa_de_bits = '24k'
        elif taxa_de_bits.upper() == "C":
            taxa_de_bits = '64k'
        elif taxa_de_bits.upper() == "D":
            taxa_de_bits = '65k'

        midia_2_0_channel = 'std_audio_02_16_bit_depth_2_0_channel.wav'
        midia_5_1_channel = 'std_audio_05_16_bit_depth_5_1_channel.wav'

        for raiz, pastas, arquivos in os.walk(caminho_origem):
            caminho_completo = os.path.join(raiz)
            nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

        # ==================================
        # CONVERTENDO MÍDIAS USANDO FFMPEG
        # ==================================

        if codec.upper() == "A":
            comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
                      f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

        elif codec.upper() == "B":
            comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel} ' \
                      f' -c:a libfdk_aac -profile:a aac_low -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

        elif codec.upper() == "C":
            comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_2_0_channel} ' \
                      f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

        elif codec.upper() == "D":
            comando = f' docker run -v {caminho_origem}:/opt/tmp/ --rm ffmpeg {comando_ffmpeg} -stream_loop 1 -i /opt/tmp/{midia_5_1_channel} ' \
                      f' -c:a libfdk_aac -profile:a aac_he -b:a {taxa_de_bits} -ar {frequencia} -latm 1 /opt/tmp/audio.mp4 '

        os.system(comando)
        print(comando)

        # =====================================
        # RENOMEANDO MÍDIAS E SALVANDO
        # =====================================

def renomear():

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

        print('''tipo de extensão: 

                            [A] - MP3
                            [B] - ZIP
                            [C] - PNG
                            [D] - ASD
                            [E] - MP4

                ''')

        extensao = str(input('Informe o tipo de extensão: '))

        if extensao.upper() == "A":
            extensao = 'mp3'
        elif extensao.upper() == "B":
            extensao = 'zip'
        elif extensao.upper() == "C":
            extensao = 'png'
        elif extensao.upper() == "D":
            extensao = 'asd'
        elif extensao.upper() == "E":
            extensao = 'mp4'

        folder = des

        for file_name in os.listdir(folder):
            old_name = folder + file_name
            new_name = folder + novo_nome + '.' + extensao
            os.rename(old_name, new_name)

        os.remove(src)

        print('*** Mídia Gerada com Sucesso ***')

