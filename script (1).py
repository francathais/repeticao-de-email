import pandas as pd

def main():
    qtnLimite = 4
    dados = pd.read_csv('massa.csv')
    listaEmails = dados.values.tolist()
    dictEmailsDTO = dict()
    for email in listaEmails:
        if str(email) in dictEmailsDTO:
            dictEmailsDTO[str(email)] = dictEmailsDTO[str(email)] + 1
        else:
            dictEmailsDTO[str(email)] = 1
    for email, qtn in dictEmailsDTO.items():
        if qtn >= qtnLimite: 
            print(email)

if __name__ == '__main__':
    main()
