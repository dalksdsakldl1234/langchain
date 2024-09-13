from getUserInfo import getUserInformation, makeOcid
from generateText import generatePrompt
from dotenv import load_dotenv
from openai import OpenAI

def getImgUrl(name,style):
    info = generatePrompt(getUserInformation(makeOcid(name)))
    summary_template = f"""
    Draw me a Maple Story character from {style} that contains the information below.
    Observe the following rules:
    1. Include only completed characters in the picture
    2. Do not include information about the equipment worn by the character in the picture
    """ + info

    load_dotenv()
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=summary_template,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return info, response.data[0].url

if __name__ == "__main__":  
    print(getImgUrl('현역복귀','cartoon'))
    





