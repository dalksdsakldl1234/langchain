from getUserInfo import getUserInformation, makeOcid
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv

def generatePrompt(info):
    summary_template = """
    given the information about a character from maplestory {information},
    I want you to create:
    1. A short summary about this maplestory character
    """
    load_dotenv()
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template = summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    return chain.invoke(input={"information":info})['text']

if __name__ == "__main__": 
    print(generatePrompt(getUserInformation(makeOcid('현역복귀'))))
