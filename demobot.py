from lib2to3.pgen2 import token
import pandas as pd
import time
import requests
import telegram
from datatime import datetime
import calender

#chat_id=''
#bot=telegram.Bot(token='')

#for i in range(0,20):
symbol='BTCUSDT'
tick_interval = '5'
#ticktime=5

now = datetime.utcnow()
unixtime = calender.timegm(now.utctimetuple())
since = unixtime
start=str(since-60*60*10)
url = 'https://api.bybit.com/public/linear/kline?symbol='+symbol+'&interval='+tick_interval+'&from='+str(start)

data = requests. get(url) . json()
D = pd.Dataframe(data['result'])

# 39 marketprice = 'https'
# res = requests.get(marketprice)
# data = res.json()

period=14
df=D
df['close'] = df['close'].astype(float)
df2=df['close'].to_numpy()

df2 = pd.DataFrame(df2, columns = ['close'])
delta = df2.diff()
up, down = delta.copy(), delta.copy()
up[up < 0] = 0
down [down > 0] = 0

#line 53 54
# _gain = up.ewm(com=(period - 1), min_periods= )
# _loss = down.abs(). ewm(com=(period - 1), min_)

RS = _gain / _loss
rsi=100 - (100 / (1 + RS))
rsi=rsi['close'] .iloc[-1]
rsi=round(rsi,1)

if rsi>70: # should be 80
    text='Bybit ' +symbal+ ' RSI: '+str(rsi)

    print(text)
    bot.sendMessage(chat_id=chat_id, text=text)
    print('RSI:', rsi)
time.sleep(1)