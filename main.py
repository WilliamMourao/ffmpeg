 


import os
import fnmatch
import sys



if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'



print('''
Informe os seguintes dados para realizar a conversão de um Video:
            
          _____________________________
            codec de video exemplo = libx264,h264_nvenc,
            crf = 23
            Resolução = 1280:720
            Perfil de codificação = 4.1
            
            comando para consultar formatos de codec:
             ffmpeg -codecs
             ffmpeg -formats
          ______________________________  
            
        ''')

codec_video = str(input('Escolha um codec de video:'))
crf = str(input('Escolha um crf:'))
scale = str(input('Escolha um resolução de video:'))
perfil_codificacao = str(input('Escolha um perfil de codificação:'))


caminho_origem = '/home/william_mourao/Imagens'


for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:

        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)


        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        arquivo_saida = os.path.join(raiz, nome_novo_arquivo)

        comando = f'{comando_ffmpeg} -i "{caminho_completo}"  ' \
            f' -c:v {codec_video} -crf {crf} -vf scale={scale} -profile:v high -level:v {perfil_codificacao}'\
            f'  "{arquivo_saida}"'


        os.system(comando)

