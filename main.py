import requests
from const import TRANSLATE_URL
from keys import TRANSLATE_KEY

choose_lang = input("Choose the language you'd like to translated to: ")
user_text = input("Please type what you'd like translated: ")

languages = {
    'spanish' : 'en-es',
    'arabic' : 'en-ar',
    'french' : 'en-fr',
    'portuguese' : 'en-pt'
}

def translate():
    try:
        model_id = languages[choose_lang]
        text = languages[user_text]

        response = requests.get(TRANSLATE_URL, auth=TRANSLATE_KEY,params={

        'text':user_text,
        'model_id':languages[choose_lang]},

        headers={
                    'Accept':'application/json'
                }
            )

        data = response.json()['translations'][0]['translation']
        print(data)
        #print("Your translation: ", data['translations'][0]['translation'])
        #for i in data:
            #print(i['translations'])

        if not response.ok:
            raise ValueError

            #print("Error!", response.ok, response.reason, response.status_code)

    except KeyError:
        print("Error! Language not recognised.")
    #except ValueError:
    #    print("Warning! Words not understood.")


translate()
