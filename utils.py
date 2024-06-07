from prompt_template import system_template_text,user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_community.llms import Tongyi
from xiaohongshu_model import Xiaohongshu
import os

def generate_xiaohongshu(theme,api_key):
    prompt=ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    # 设置 API-KEY
    os.environ["DASHSCOPE_API_KEY"] = api_key
    # 使用 Tongyi LLM
    llm = Tongyi()
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | llm | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

# print(generate_xiaohongshu("大模型",os.getenv("DASHSCOPE_API_KEY")))

