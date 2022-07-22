from audio_mpeg_1 import menu_mpeg1, entrada_de_dados
from audio_mpeg_4 import dados_de_entrada, renomear, menu_mpeg4


def tipo_midia():
    print("*********************************")
    print("*******Escolha uma Opção!*******")
    print("*********************************")

    print('[A] MPEG-1 [B] MPEG-4')

    escolha = str(input('Informe a opção desejada: '))

    if escolha.upper() == "A":
        menu_mpeg1(),entrada_de_dados()

    elif escolha.upper() == "B":
        menu_mpeg4(),dados_de_entrada(),renomear()

if (__name__ == "__main__"):
    tipo_midia()
