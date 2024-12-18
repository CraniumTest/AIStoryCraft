from story_generator import generate_story

def interactive_narrative(initial_story):
    story = initial_story
    continue_story = True
    while continue_story:
        print(f"\\nCurrent Story: {story}\\n")
        user_choice = input("Do you want the AI to continue this story? (yes/no): ").strip().lower()

        if user_choice == "yes":
            story_piece = generate_story(story)
            story += f" {story_piece}"
        else:
            continue_story = False
    
    return story
