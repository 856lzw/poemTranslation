from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from prompt_poem import system_template_text, user_template_text
from poem_model import Poem
import os

api4 = "sk-jPtA6Ew4ZAMYRDMfFb072784BdB2483d8112851683AcD8Ea"
base4 = "https://api.gpts.vin/v1"


def generate_poem_translation(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    # model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,
    #                    openai_api_base="https://api.aigc369.com/v1")
    model = ChatOpenAI(model="gpt-4", api_key=openai_api_key,
                       openai_api_base=base4)
    output_parser = PydanticOutputParser(pydantic_object=Poem)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result


# res = generate_poem_translation("大漠孤烟直，长河落日圆", api4)
# print(res)

