from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import OpenAI

# Replace with your actual SQLite/Postgres URI
db = SQLDatabase.from_uri("sqlite:///data/sales.db")
llm = OpenAI(temperature=0)
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)

def query_sales(prompt: str):
    return db_chain.run(prompt)

# Example usage
if __name__ == "__main__":
    print(query_sales("What are the top-selling products?"))
