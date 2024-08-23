def college(essay):
    # 0 is the beggining - outside details
    with open('txt/college/college0.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
    # then comes the essay itself
    content += '\\n```' + essay + '```\\n '
    # comprehension on each part
    with open('txt/college/college1.txt', 'r') as file:
        # Read the entire content of the file
        content += file.read()
    with open('txt/college/college2.txt', 'r') as file:
        # Read the entire content of the file
        content += file.read()
    return content

def reads(essay):
# reads gemini essay and returns jsonify file, and paragraph that goes along with it
    """
    returns a list of two strings: the 'JSON' object and the pargraph that was written about the essay
    """
    # m = how many quotation marks there are
    m = 0

    # if there is a j, s, o, n
    j = 0
    s = 0
    o = 0
    n = 0
    l = 0
    # y is a bool for whether characters should be recorded
    y = 0

    json = ""
    paragraph = ""
    # make the json object
    for i in essay:
        if i == "`":
            if m == 2:
                if y == 1:
                    y = 2
                if y == 0:
                    y = 1
                m = 0
            else:
                # not enough ''' to fulfill requirements
                m += 1
        if y == 1:
            if m != 0:
                i = i
            # get json
            elif (j == 1 and s == 1 and o == 1 and n == 1):
                # add i character
                if i != '\\':       
                    json += str(i)
            # see if there is a json
            elif (i == 'j'):
                j = 1
            elif (i == 's'):
                s = 1
            elif (i == 'o'):
                o = 1
            elif (i == 'n'):
                n = 1
        elif y == 2:
            # add to pargraph
            paragraph += i
    element = [json, paragraph]
    return element