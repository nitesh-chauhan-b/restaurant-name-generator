from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain_groq import ChatGroq
import os
from api_key import GROQ_API_KEY
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()
# #Setting up API_KEY
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

#Creating llm model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.6,
    max_retries=2
)

#Function to get restaurant name and menu_items
def get_res_details(cuisine):

    # Creating a prompt template for restaurant and menu_items using sequential chain


    # prompt 1
    prompt_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open {cuisine} Food Restaurant. Please Suggest me a great name. Just one name.Nothing else(without double quotes)"
    )
    # chain 1
    name_chain = LLMChain(llm=llm, prompt=prompt_name, output_key="restaurant_name")

    # prompt 2
    prompt_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest me some amazing menu items for {restaurant_name}. Please provide it as a comma separated list.,just return menu items."
    )
    # chain 2
    food_items = LLMChain(llm=llm, prompt=prompt_items, output_key="menu_items")


    # Creating a sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_items],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    # Running the chain
    response = chain({"cuisine": cuisine})

    return response
