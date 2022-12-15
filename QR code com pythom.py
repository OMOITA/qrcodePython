import qrcode

data = 'Teste de Qrcode' # insere o texto na variavel
img = qrcode.make(data)#cria o qrcode
img.save('D:/Programação/Python/Portifólio/qrcode/meuqrcode.png')#diretório de salvamento 