import time

def ponto_continuo():
    ponto1 = str(".")
    # ponto2 = str("..")
    # ponto3 = str("...")
    while True:
        for i in range(0, 3):
            if i == 0:
                time.sleep(0.5)
                print(ponto1)
            elif i == 1:
                time.sleep(1)
                print(ponto1 + ponto1)
            elif i == 2:
                time.sleep(1)
                print(ponto1 + ponto1 + ponto1)

ponto_continuo()