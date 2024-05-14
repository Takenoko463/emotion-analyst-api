# Emotion-analyst-api
単語をparamに入れて送ると感情の計測値をjson形式で返送するapiです

# Url
[api](https://emotion-analyst-api-image-jjgaumsera-an.a.run.app)

# 使用
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