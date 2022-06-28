import os
import fnmatch
import sys



if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'arquivo_aula_yt_2019-06-12\arquivo_aula_yt_2019-06-12.exe'

print('''
            FFMPEG Audio:
            ________________________
            frequência = -ar 48 khz
            taxa de bits = -b:a 640k 
            Bitrate_audio = -c:a ac3 
           __________________________

        ''')


'''frequencia = str(input('Escolha uma frequência:'))'''
taxa_de_bits = str(input('Escolha o tamanho da midia: '))
bitrate_audio = str(input('Escolha um tipo de audio:'))


taxa_de_bits = '-b:a ' + taxa_de_bits
bitrate_audio = '-c:a ' + bitrate_audio

caminho_origem = '/home/william_mourao/Imagens'
caminho_destino = '/home/william_mourao/Imagens/saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:

        if not fnmatch.fnmatch(arquivo, '*.wav'):
            print(arquivos)
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}"  ' \
                  f' {taxa_de_bits} {bitrate_audio}' \
                  f'  "{arquivo_saida}"'

        os.system(comando)

