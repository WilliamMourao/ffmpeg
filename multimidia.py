import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'

print('''
Informe os seguintes dados para realizar a conversão de um audio:
            
        

        ''')


caminho_origem = '/home/william_mourao/Imagens'




comando = f'{comando_ffmpeg} -i "{caminho_completo}"  ' \
                  f' {frequencia} {taxa_de_bits} {bitrate_audio} {volume}' \
                  f'  "{arquivo_saida}"'

        os.system(comando)

