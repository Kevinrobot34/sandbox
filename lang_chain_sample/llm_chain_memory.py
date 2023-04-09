from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate)


def llm_chain_with_memory():
    llm = OpenAI()

    template = "You are a chatbot having a conversation with a human.\n" + \
        "\n" + \
        "{chat_history}\n" + \
        "Human: {human_input}\n" + \
        "AI:"
    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], 
        template=template
    )

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt, 
        verbose=True, 
        memory=memory,
    )

    res1 = llm_chain.predict(human_input="Hi there my friend")
    print(res1)
    res2 = llm_chain.predict(human_input="I just talk to you")
    print(res2)


if __name__ == "__main__":
    # https://python.langchain.com/en/latest/modules/chains/getting_started.html
    # https://python.langchain.com/en/latest/modules/memory/examples/adding_memory.html
    
    llm_chain_with_memory()