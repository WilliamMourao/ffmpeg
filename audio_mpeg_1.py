import os
import sys


if sys.platform == 'linux':
    comando_mp2enc = 'mp2enc'


def menu_mpeg1():

        print("*********************************")
        print("***Você escolheu MPEG-1***")
        print("*********************************")

        print(''' Menu Codec:
        
                [A] - MPEG-1 Audio Layer 1 (mpg,mp1,mp2)
                [B] - MPEG-1 Audio Layer 2 (mpg,mp1)
                    
            ''')

def entrada_de_dados():
    print('Exemplo: /home/william_mourao/Imagens/')
    caminho_origem = str(input('Informe o local onde está a sua mídia de audio:'))
    codec = str(input('Escolha uma letra do menu codec:'))
    print(''' Tipos de frequência: 
    
                                    [A] - 32000
                                    [B] - 48000
                                    [C] - 44100
                ''')
    frequencia = str(input('Escolha o tipo de frequência: '))
    if frequencia.upper() == "A":
        frequencia = '32000'
    elif frequencia.upper() == "B":
        frequencia = '48000'
    elif frequencia.upper() == "C":
        frequencia = '44100'

    taxa_de_bits = str(input('Escolha o tamanho do Bit rate (ex: 32):'))

    print('''Tipos de extensão: 

                                [A] - MP1
                                [B] - MP2
                                [C] - MPG
                                
            ''')

    extensao = str(input('Escolha o tipo de extensão: '))

    if extensao.upper() == "A":
        extensao = 'mp1'
    elif extensao.upper() == "B":
        extensao = 'mp2'
    elif extensao.upper() == "C":
        extensao = 'mpg'

    print('Exemplo: /home/william_mourao/Imagens/saida/')
    saida = str(input('Informe o local onde será salva a mídia: '))

    midia_2_0_channel_mpeg1 = 'std_audio_02_16_bit_depth_2_0_channel_for_mpeg1_audio.wav'

    for raiz, pastas, arquivos in os.walk(caminho_origem):
        caminho_completo = os.path.join(raiz)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

    if codec.upper() == "A":
        comando = f' {comando_mp2enc} -o {saida}teste.{extensao}' \
                  f' -b {taxa_de_bits} -r {frequencia} -l 1 < {caminho_origem}{midia_2_0_channel_mpeg1} '

    elif codec.upper() == "B":
        comando = f' {comando_mp2enc} -o {saida}teste.{extensao}' \
                  f' -b {taxa_de_bits} -r {frequencia} -l 2 < {caminho_origem}{midia_2_0_channel_mpeg1} '


    novo_nome = str(input('Informe o nome da mídia: '))

    print('*** Mídia Gerada com Sucesso ***')

    os.system(comando)
    print(comando)

    folder = saida

    for file_name in os.listdir(folder):
        old_name = folder + file_name
        new_name = folder + novo_nome + '.' + extensao
        os.rename(old_name, new_name)






