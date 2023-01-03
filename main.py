import io
import sys
import urllib.request as requisicao

BUFF_SIZE = 1024

def download_length(response, output, length):
    qtdPacotes = length
    if length % BUFF_SIZE > 0:
        qtdPacotes += 1
    for qtd in range(qtdPacotes):
        output.write(response.read(BUFF_SIZE))
        print("Download %d" % (((qtd * BUFF_SIZE)/length)*100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(butes=total_downloaded))

def main():
    response = requisicao.urlopen(sys.argv[1])
    out_file = io.FileIO('saida.zip', mode="w")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()
    print("Finalizado")

if __name__ == '__main__':
    main()
