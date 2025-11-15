from huggingface_hub import  login
from smolagents import CodeAgent, tool, DuckDuckGoSearchTool, InferenceClientModel
import datetime

login()


@tool
def suggest_menu(occasion: str) -> str:
    """Suggest a menu based on the given occasion.
    
    Args:
        occasion: The type of occasion for the party. Allowed values are:
                  - "casual": Menu for casual party.
                  - "formal": Menu for formal party.
                  - "superhero": Menu for superhero party.
                  - "custom": Custom menu.
    """
    
    if occasion == "casual":
        return "Casual Party Menu: Finger foods, sliders, nachos, soft drinks."
    elif occasion == "formal":
        return "Formal Party Menu: Appetizers, main course with sides, desserts, wine."
    elif occasion == "superhero":
        return "Superhero Party Menu: Themed cupcakes, hero sandwiches, power punch."
    elif occasion == "custom":
        return "Custom Party Menu: Please specify your preferences."
    else:
        return "Invalid occasion type. Please choose from casual, formal, superhero, or custom."


agent = CodeAgent(tools = [DuckDuckGoSearchTool(), suggest_menu], model = InferenceClientModel(), additional_authorized_imports = ["datetime"])

agent.run("""
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """)

