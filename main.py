from fastapi import FastAPI

app = FastAPI()

#ここにアクセスがあったら、async以下のコードを実行される。
#デコレーター
#asyncは非同期処理、他の作業と並列処理ができる。
@app.get("/countries/japan")
async def japan():
    return {"message": "This is japan"}

#上記が書けたらターミナルにて、uvicorn main:app --reload　と入力。
#返された値のhttp://127.0.0.1:8000にアクセスするとreturn で返されたものが表示される。
#URLの後に/redoc(又は//docs)を付ければ、APIドキュメント生成されたページに移動できる。

@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}
