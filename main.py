from fastapi import FastAPI

app = FastAPI()

#ここにアクセスがあったら、async以下のコードを実行される。
#@から始まる行はデコレーター。条件されたものが実行されたら以下の関数も実行される。
#asyncは非同期処理、他の作業と並列処理ができる。
@app.get("/")
async def index():
    return {"message": "This is japan"}

#上記が書けたらターミナルにて、uvicorn main:app --reload　と入力。
#返された値のhttp://127.0.0.1:8000にアクセスするとreturn で返されたものが文面で表示される。
#URLの後に/redoc(又は/docs)を付ければ、APIドキュメント生成されたページに移動できる。



#http://127.0.0.1:8000/hello の様にURL以降/helloにしたら
#returnのメッセージが返される。
@app.get("/hello")
async def index():
    return {"message": "hello version"}


#http://127.0.0.1:8000/hello の様にURL以降/helloにしたら
#returnのメッセージが返される。
#@デコレーションの{}で引数と扱うことできる。
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}
#型ヒントはdef関数の所で定義


#クエリパラメータ、URLにある"?"以降のもの
#例えば、
#https://www.facebook.com/search/top/?q=football

#デコレーターの｛｝無しに、関数の引数を設定すると、引数のものはURL入力時に?以降で指定できる。
#http://127.0.0.1:8000/countries_deco/でアクセスすると、
#文面には"country_name": Japan,"country_no"  : 1　が返ってくる
#http://127.0.0.1:8000/countries_deco/?country_name=Amaerica&country_no=3でアクセスすると
#文面には"country_name": America,"country_no"  : 3　が返ってくる
@app.get("/countries_deco/")
async def country(country_name: str = "Japan", country_no: int = 1):
    return {"country_name": country_name,
            "country_no"  : country_no
            }



#パスパラメーターとクエリパラメーターの組み合わせ
@app.get("/countries_mix/{country_name}")
async def country(country_name: str = "Japan", city_name: str = "Tokyo"):
    return {"country_name": country_name,
            "city_name"  : city_name
            }
#URL検索候補としては以下がある。
#http://127.0.0.1:8000/countries_mix/Japan
#http://127.0.0.1:8000/countries_mix/America?city_name=Newyork



#必須ではないオプションパラメータにする方法

from typing import Optional

@app.get("/countries_option/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {"country_name": country_name,
            "country_no"  : country_no
            }
#http://127.0.0.1:8000/countries_option/で検索するとエラーは発生しない。
#{"country_name":null,"country_no":null}と返ってくる。












    
