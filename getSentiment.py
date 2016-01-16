# These code snippets use an open-source library.
import unirest

aa="i hate sam"
response = unirest.get("https://alchemy.p.mashape.com/text/TextGetTextSentiment?outputMode=json&showSourceText=false&text=i+hate+sam",
  headers={
    "X-Mashape-Key": "QudYSp65Jcmsh98Jm0wjHFrL5e3Xp1ALvSMjsn9f2DANpOb8aI",
    "Accept": "text/plain"
  }
)

value = response.body
value1 = value['docSentiment']['score']
print(value1)