

notes_input = input("Enter notes,separated by spaces: ")
notes = [int(note) for note in notes_input.split()]
def analyze_notes(*notes):
    # Calculating necessary metrics
    num_notes = len(notes)
    highest_score = max(notes) if notes else None
    class_average = sum(notes) / num_notes if num_notes > 0 else 0

    # Determining the situation based on the class average
    if class_average > 12:
        situation = "Good"
    elif class_average < 9.5:
        situation = "Weak"
    else:
        situation = "Reasonable"

    # Returning the result as a dictionary
    return {
        "Number of notes": num_notes,
        "Highest score": highest_score,
        "Class average": class_average,
        "Situation": situation
    }


# Example usage

result = analyze_notes(*notes)
print(result)
