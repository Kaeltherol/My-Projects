import requests
import pandas as pd
from datetime import datetime
from pprint import pprint
import json

def rep_dict(dframe,report_name,*args):
  # rep_dict(dataframe, string,*strings)
  # Questa funzione genera un elenco di criptovalute in formato dizionario a partire da un dataframe già filtrato. E' possibile aggiungere
  # altre caratteristiche dalle colonne del dataframe come argomento opzionale.
    list_id = dframe.index
    dict_output = {
        report_name : {
        dframe['name'][id] : dict({
            'id' : id,
            'symbol' : dframe['symbol'][id]
            },
             **{arg: dframe[arg][id]for arg in args
             }) for id in list_id
             }}
    return dict_output

def create_report(*args):
  #create_report(*dictionaries):
  #questa funzione genera un report in formato dizionario a partire da uno o più dizionari in input.
    report_dict = {}
    for arg in args:
        report_dict.update(arg)
    return report_dict

def report_to_json(input_dict):
  #report_to_json(dictionary):
  #questa funzione genera un file json a partire da un dizionario in input. il nome file è una data e corrisponde al momento
  #in cui il programma scarica il database dalla piattaforma di scambio.
    date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
    name_file = date_time + ".json"
    with open(name_file,'w',encoding='utf-8') as f:
        try:
          json.dump(input_dict,f, sort_keys=False,indent=4)
          print('Report saved in ' + name_file)
        except:
          print('error!')

#definizione parametri

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',
}

#download dati dalla fonte

try:
  r = requests.get(url=url, headers = headers, params=parameters).json()
  data = r['data']
  now = datetime.now()
except:
  print('error!')

#generazione dataframe a partire dai dati. 

df1 = [currency['id'] for currency in data]
df2 = [currency['symbol'] for currency in data]
df3 = [currency['name'] for currency in data]
df4 = [currency['quote']['USD'] for currency in data]
df = pd.DataFrame()
df['id'] = df1
df['symbol'] = df2
df['name'] = df3
df5 = pd.DataFrame(df4)
df = pd.concat([df,df5],axis=1)
df.set_index('id',inplace=True)
pd.to_datetime(df['last_updated'])

#Creazione reportistica in 3 passaggi:
# a) definizione filtro e creazione dataframe filtrato
# b) definizione parametri di interesse nel report
# b) creazione report come dizionario

#1)La criptovaluta con il volume maggiore (in $) delle ultime 24 ore

df_temp = df.sort_values('volume_24h',ascending=False).head(1)
top_volume = rep_dict(df_temp,'top_volume', 'volume_24h')

#2) Le migliori e peggiori 10 criptovalute

df_temp = df.sort_values('percent_change_24h',ascending=False).head(10)
top_percent= rep_dict(df_temp,'top_percent','percent_change_24h')
df_temp = df.sort_values('percent_change_24h',ascending=True).head(10)
flop_percent = rep_dict(df_temp,'flop_percent','percent_change_24h')

#3) La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute

df_temp = df.sort_values('market_cap',ascending=False).head(20)
top_crypto = rep_dict(df_temp,'top_crypto','price')
money = df.sort_values('market_cap',ascending=False).head(20)['price'].sum()
money_top20 = {'money_top20': money}

#4)La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$

df_temp = df[df['volume_24h']>76000].sort_values('volume_24h',ascending = False)
top_vol_more = rep_dict(df_temp,'top_vol_more','name','price','volume_24h')
money = df[df['volume_24h']>76000]['price'].sum()
money_vol = {'money_vol': money}

#5)La percentuale di guadagno o perdita che avreste realizzato se aveste comprato
#  una unità di ciascuna delle prime 20 criptovalute* il giorno prima (ipotizzando che la classifca non sia cambiata)

df_temp = df.sort_values('market_cap',ascending=False).head(20)[['name','symbol','price','percent_change_24h']]

df_temp['profit_24h'] = df_temp.apply(lambda row: row['percent_change_24h']/(row['percent_change_24h']+100)*row['price'],axis=1)
df_temp['price_24h'] = df_temp.apply(lambda row: -row['profit_24h']+row['price'],axis=1)

top_profit=rep_dict(df_temp,'top_profit','price','percent_change_24h')

profit = df_temp['profit_24h'].sum()/df_temp['price_24h'].sum()*100
tot_profit = {'tot_profit': profit}


#creazione report

output = create_report(top_volume, top_percent, flop_percent,  money_top20, money_vol, top_profit)

#salvataggio report su file

report_to_json(output)


