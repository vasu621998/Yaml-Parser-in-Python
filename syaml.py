# function to validate paranthesis
def check(expression):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []
    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"

# function to handle list 
def handle_list(data):
    for list_ele in data:
        # check whether there is a list inside dict
        if isinstance(list_ele, dict):
            dict_key = list(list_ele.keys())
            # extract key and dict value
            for i in range(len(dict_key)):
                key = dict_key[i]
                value = list_ele.get(key)
                if (i == 0):
                    print("- " + key + " : " + value)
                else:
                    print("  " + key + " : " + value)
            # Printing out the output
        if isinstance(list_ele, str):
            print("- ", list_ele)

# function to handle dict
def handle_dict(data):
    # list inside dict
    for key in data:
        if isinstance(data[key], list):
            print(key + ":")
            #  Print the output in the required format
            for value in data[key]:
                print("\t-" + value)
        else:
            print(key + ":" + data[key])

def print_syaml(data):
    """Print data in SYAML format. Raise an exception if this is not possible"""

    # parse_syaml(data)
    if isinstance(data, dict) or isinstance(data, list):
        print("---")
        # YOUR CODE TO PRINT DATA GOES HERE
        if isinstance(data, list):
            handle_list(data)
        if isinstance(data, dict):
            handle_dict(data)
        print("...")
        
    else:
        # raise exception for invalid input in print
        raise Exception("Input must be list or dictionary")


def parse_syaml(lines):
    """Parse SYAML document. See LEARN for details."""
    if not isinstance(lines, list):
        raise Exception("Expecting a list of strings")
    if not (len(lines) >= 2 and lines[0] == "---\n" and lines[-1] == "...\n"):
        raise Exception("Begin or end document is missing")
    # YOUR CODE GOES HERE
    yaml_lines = lines[1:-1]
    finaldict = {}
    finallist = []
    dict_flag = False
    for j in range(1, len(lines)):
        str_checker = isinstance(lines[j], str)
        # exception to check string format of the input passed
        if not str_checker:
            raise Exception("The given input must be in a string format")
        valid_par = check(lines[j])
        # invalid paranthesis check using check function
        if (valid_par == "Unbalanced"):
            raise Exception("Invalid paranthesis in an input")
        # checking new line 
        if "\n" not in lines[j]:
            raise Exception("Missing new line in the line")
        # checking space after colon
        for i in range(len(lines[j])):
            if(lines[j][i] == ":" and lines[j][i + 1] != " "):
                raise Exception("After : there should be a space in an input")
    for entry in yaml_lines:
        if entry.find(":") == -1:
            finallist.append(entry)
        else:
            dict_flag = True
            key = entry.split(":")[0]
            value = entry.split(":")[1]
            finaldict[key] = value.split("\n")[0]
    if (dict_flag):
        return finaldict
    else:
        for element in finallist:
            return element.split("\n")[0]



# This is a simple test function provided from your convenience
if __name__ == "__main__":
    # d1 = [{"one": "un",
    #        "two": "deux"},
    #       {"one": "uno",
    #        "two": "dos"}]
    # d3 = ['one', 'two', 'three']
    # d4 = {"one": ["un",
    #               "uno"],
    #       "two": ["deux",
    #               "dos"]}
    # d5 = {'one': 'un', 'two': 'deux', 'three': 'trois'}
    # d6 = "one"
    # print_syaml(d3)
    # print_syaml(d1)
    # print_syaml(d4)
    # print_syaml(d5)
    d1 = ["one", "two", "three"]
    print_syaml(d1)

    t1 = ["---\n",
          "one: un\n",
          "two: deux\n",
          "three: trois\n",
          "...\n"]
    d2 = parse_syaml(t1)
    print(d2)
    #print_syaml(d2)

    # t1 = ["---\n",
    #       "one: un\n",
    #       "two: deux\n",
    #       "three: trois\n",
    #       "...\n"]
    # t2 = ["---\n",
    #       "oneun\n",
    #       "twodeux\n",
    #       "threetrois\n",
    #       "...\n"]

    # parse_syaml(t2)
    # parse_syaml(t1)
