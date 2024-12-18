from interactive_story import interactive_narrative

def start_cli():
    print("Welcome to AIStoryCraft - Interactive AI-Powered Storytelling Platform!")
    initial_prompt = input("Enter the beginning of your story: ")
    final_story = interactive_narrative(initial_prompt)
    print("\\nYour completed story:\\n")
    print(final_story)
