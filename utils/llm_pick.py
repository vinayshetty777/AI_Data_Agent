
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

def pick_llm(level: str):
    """
    Picks the appropriate LLM based on the level of the question.

    Args:
        level (str): The level of the question, can be "low", "medium", or "high".

    Returns:
        ChatAnthropic: The LLM instance to be used.
    """
    if level.lower() == "low":
        llm = ChatAnthropic(model_name="claude-haiku-4-5", temperature=0)

    elif level.lower() == "medium":
        llm = ChatAnthropic(model_name="claude-haiku-4-5", temperature=0)

    elif level.lower() == "high":
        llm = ChatAnthropic(model_name="claude-haiku-4-5", temperature=0)
        
    elif level.lower() == "claude":
        llm = ChatAnthropic(model_name="claude-sonnet-5")
    else:
        raise ValueError(f"Unsupported level: {level}")

    return llm

if __name__ == "__main__":
    llm_obj = pick_llm("low")  
    print(llm_obj.invoke("What is the capital of France?"))