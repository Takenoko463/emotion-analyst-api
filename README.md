# Emotion-analyst-api
単語をparamに入れて送ると感情の計測値をjson形式で返送するapiです

# Url
[https://emotion-analyst-api-image-jjgaumsera-an.a.run.app](https://emotion-analyst-api-image-jjgaumsera-an.a.run.app)

# 利用方法
## requestを送るpath
```python
https://emotion-analyst-api-image-jjgaumsera-an.a.run.app/emotion/悲しい
```

## response
```json
{"word":"悲しい","emotions":[{"aware":1},{"shape":0},{"anger":0},{"unpleasant":0},{"fear":0},{"surprise":0},{"love":0},{"excitement":0},{"cheap":0},{"pleasant":0}]}
```

## requestを送るpath
```python
https://emotion-analyst-api-image-jjgaumsera-an.a.run.app/emotions/?word=悲しい&word=楽しい
```

## response
```json
{
  "words":
  [
    {
      "word":"悲しい",
      "emotions":[
        {"aware":1},{"shape":0},{"anger":0},{"unpleasant":0},{"fear":0},{"surprise":0},{"love":0},{"excitement":0},{"cheap":0},{"pleasant":0}
                ]
    },
    {
      "word":"楽しい",
      "emotions":[
        {"aware":0},{"shape":0},{"anger":0},{"unpleasant":0},{"fear":0},{"surprise":0},{"love":0},{"excitement":0},{"cheap":1},{"pleasant":2}
        ]
    }
  ]
}
```

# アプリケーションを作成した背景
私がこのapiを開発した目的は、文章から大まかな感情判定を行うことで運営に支障をきたすユーザーを見つけ出すためです。  
現在、インターネットが発達し匿名投稿者による誹謗中傷が相次いでいます。X(twitter)では運営が処理しきれないほど開示請求を行われています。
webアプリ運営は有料化、ユーザー規制などにより誹謗中傷対策を行わなければなりません。非常に時間と手間を取られます。  
そこで、このapiが役立ちます。コメント内容をこちらのアプリで分析し、極端に負の感情、怒り（anger）、嘆き（aware）が大きいものを重点的に割り出しておけるのです。  
開示請求や、多数のユーザーの要望を受ける前からIP規制等をかける対象者を絞ることができるため、運営はより効率的にwebサイト管理を行えます。  
ユーザーではなくIPで管理している自分のアプリ[Prompter](https://github.com/Takenoko463/prompter)にも導入予定です。

# 開発環境
- バックエンド:fastapi python3
- インフラ　Docker
- サーバー Google Cloud Platform


