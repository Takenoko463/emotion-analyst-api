from typing import Union, List
# FastAPIの読み込み
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware # 追加
from . import emotional_analysis

# FastAPIのインスタンスを作成
app = FastAPI()

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

# getメソッドで、/にアクセスした時の処理を記述
@app.get("/")
# asyncで*非同期処理を行う
# *あるタスクを実行している最中に、実行中のタスクを止めることなく、別のタスクを実行できる
async def hello():
    return {"text": "Emotion Analysis!!"}

# getメソッドで、/emotion/{word}にアクセスした時の処理を記述
@app.get("/emotion/{word}")
async def show(word):
    emotion_analysis_json=emotional_analysis.get_analysis_word(word)
    return  emotion_analysis_json

# getメソッドで、/emotions/index/にアクセスした時の処理を記述
@app.get("/emotions/")
async def index(word: List[str] = Query(default=None, max_length=5000)):
    if word:
        emotions_analysis_array=emotional_analysis.get_analysis_words(word)
        return {"words":emotions_analysis_array}
    else:
        return {"text":"error"}