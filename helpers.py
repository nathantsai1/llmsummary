def college(essay):
    # 0 is the beggining - outside details
    with open('txt/college/college0.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
    # then comes the essay itself
    content += '\\n"' + essay + '"\\n '
    # comprehension on each part
    with open('txt/college/college1.txt', 'r') as file:
        # Read the entire content of the file
        content += file.read()
    return content

def read(essay):
# reads gemini essay and returns jsonify file, and paragraph that goes along with it
    return False