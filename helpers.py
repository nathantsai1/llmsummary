def temp():
    # doesn't do anything
    return 1

def college(essay):
    with open('/txt/college/college0.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
    content += essay
    with open('/txt/college/college0.txt', 'r') as file:
        # Read the entire content of the file
        content += file.read()