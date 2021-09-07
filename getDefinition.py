import requests
from pprint import pprint as print

URL = 'https://api.dictionaryapi.dev/api/v2/entries/'

def getDefinition(word, lang = 'en'):

    url = URL
    url += lang + '/' + word
    r = requests.get(url)

    if 'message' in r.json():
        return False
    else:
        ans = {}
        defs = []
        for wd in r.json()[0]['meanings'][0]['definitions']:
            defs.append(' 🔸   ' + wd['definition'])

        ans['word'] = r.json()[0]['word']
        ans['transcription'] = r.json()[0]['phonetics'][0]['text']
        if r.json()[0]['phonetics'][0]['audio']:
            ans['audio'] = r.json()[0]['phonetics'][0]['audio']
        ans['definition'] = '\n'.join(defs)
        if r.json()[0]['meanings'][0]['definitions'][0]['synonyms']:
            ans['synonyms'] = ', '.join(r.json()[0]['meanings'][0]['definitions'][0]['synonyms'])

        return ans

if __name__ == '__main__':
    ans = ''
    out = getDefinition('hello')
    ans += f"🇬🇧 Word : {out['word']} \n\n"
    ans += f"🇬🇧 Transcription : {out['transcription']} \n\n"
    ans += f"🇬🇧 Definition : {out['definition']} \n\n"
    ans += f"🇬🇧 Synonyms : {out['synonyms']}"
    print(ans)

