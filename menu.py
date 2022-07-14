import audio_mpeg_1
import audio_mpeg_4

def tipo_midia():
    print("*********************************")
    print("*******Escolha uma Opção!*******")
    print("*********************************")

    print('[1] MPEG-1 [2] MPEG-4')

    escolha = int(input('Informe a opção desejada: '))

    if (escolha == 1):
        print('Você escolheu MPEG-1')
        audio_mpeg_1.escolha()
    elif(escolha == 2):
        print('Você escolheu MPEG-4')
        audio_mpeg_4.escolha()

if(__name__ == "__main__"):
    tipo_midia()