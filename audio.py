import os
import fnmatch
import sys



if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'


print('''
Informe os seguintes dados para realizar a conversão de um audio:
            ________________________
            frequência = 48000
            taxa de bits = entre 24k e 64k 
            Bitrate_audio exemplos = -c:a ac3,mp3,wmav2,e-ac3.
            volume = 1 a 100
            
            comando para consultar formatos de codec:
             ffmpeg -codecs
             ffmpeg -formats
           __________________________

        ''')

frequencia = str(input('Escolha uma frequência:'))
taxa_de_bits = str(input('Escolha o tamanho da midia: '))
bitrate_audio = str(input('Escolha um tipo de audio:'))
volume = str(input('Informe o volume:'))


caminho_origem = '/home/william_mourao/Imagens'


for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:

        if not fnmatch.fnmatch(arquivo, '*.wav'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}"  ' \
                  f' -ar {frequencia} -b:a {taxa_de_bits} -c:a {bitrate_audio} -vol {volume}' \
                  f'  "{arquivo_saida}"'

        os.system(comando)

