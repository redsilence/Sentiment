# These code snippets use an open-source library.
import unirest


def getSentiment(text):
  #print(text)
  response = unirest.get(
      str("https://alchemy.p.mashape.com/text/TextGetTextSentiment?outputMode=json&showSourceText=false&text=" + text),
      headers={
          "X-Mashape-Key": "QudYSp65Jcmsh98Jm0wjHFrL5e3Xp1ALvSMjsn9f2DANpOb8aI",
          "Accept": "text/plain"
      }
      )

  answer = response.body
  value = answer['docSentiment']
  return value

