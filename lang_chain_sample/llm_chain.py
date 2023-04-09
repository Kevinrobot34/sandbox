from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate)


def sample_llm():
    llm = OpenAI(temperature=0.9)
    print(llm)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    res = chain.run('colorful socks')
    print(res)


def sample_chat():
    chat = ChatOpenAI(temperature=0.9)
    print(chat)

    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="What is a good name for a company that makes {product}?",
            input_variables=["product"],
        )
    )
    chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt_template, verbose=True)
    res = chain.run("colorful socks")
    print(res)


if __name__ == "__main__":
    # https://python.langchain.com/en/latest/modules/chains/getting_started.html
    print('sample llm_chain')
    sample_llm()

    print('sample llm_chain with ChatOpenAI')
    sample_chat()

