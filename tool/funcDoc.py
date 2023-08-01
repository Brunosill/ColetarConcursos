import datetime
import os
import pandas as pd

from tool.funcPage import extraiPagina

date = datetime.date.today().strftime("%Y-%m-%d")

def salvaArquivoCSV(path, name, dataFrame):

    if not os.path.exists(path):
        os.makedirs(path)

    return dataFrame.to_csv(path + name, index=False)


def extraiCargoPath():
  
    url = "https://www.pciconcursos.com.br/provas/"
    filePath = "dados/path_officers/"

    officersLinkList = []

    page = extraiPagina(url)

    for tag in page.find_all("a", title=True):

        office = tag.text
        link = tag["href"]

        officersLinkList.append([office,  link])

    officersLink = pd.DataFrame(officersLinkList, columns=['office','link'])

    salvaArquivoCSV(filePath, f'path_office_{date}.csv', officersLink )


def lerCargoPath():
   
    OfficersLink = pd.read_csv(f'dados/path_officers/path_office_{date}.csv')

    return OfficersLink.values[0:2] #limitador


def estraiDadosCargo():

  
    for office, link in lerCargoPath():
        name = link.split('/')[-1]+'_'+date

        office = office.replace(" ","_")
        path = f'dados/data_officers/{office}/'

        ExportDF = pd.DataFrame()
        page = extraiPagina(link)

        NPage = int(page.find_all("span")[1].text.split()[-1])

        if NPage != 1:

            for n in range(1, NPage + 1):
                linkPage = f'{link}/{n}'

                page = extraiPagina(link)

                PageDF = pd.read_html(link, header = 0, extract_links='all')[0]
                ExportDF = pd.concat([ExportDF, PageDF])

            salvaArquivoCSV(path, name+".csv", ExportDF)

        else:
            ExportDF = pd.read_html(link, header = 0, extract_links='all')[0]


            salvaArquivoCSV(path, name+".csv", ExportDF)


