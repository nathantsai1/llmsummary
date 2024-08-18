def college(essay):
    with open('txt/college/college0.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
    content += '\\n"' + essay + '"\\n '
    with open('txt/college/college.txt', 'r') as file:
        # Read the entire content of the file
        content += file.read()
    return content

def read(essay):
# reads gemini essay and returns jsonify file, and paragraph that goes along with it
    return False