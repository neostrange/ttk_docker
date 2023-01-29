from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import re
import os


def process(input, dct):

        # List all files in a directory using os.listdir
    basepath = 'data/text2graph'
    print(os.getcwd())
        #open text file
    text_file = open(basepath + "/data.txt", "w")

    print("input: ", input)
    #write string to file
    text_file.write(input)

    #close file
    text_file.close()

    timex = dct
    timex = dct




    if os.path.exists("output.xml"):
        os.remove("output.xml")
    else:
        print("The file does not exist")

    # compose the command to run
    command = 'python tarsqi.py --dct ' + timex +' data/text2graph/data.txt'  + ' output.xml'
    #command = 'python ttk/tarsqi.py --dct ' + timex +' /home/neo/environments/ttk/ttk/data/text2graph/'+entry+' ' + filename+'.xml'
    stream = os.popen(command).read() 


    output = ""
    with open('output.xml','r') as file:
        output = file.read()
    print(output)

    return output


app = Flask(__name__)

@app.route("/annotate", methods=["POST"])
def annotate():
    # Get the input string from the request
    input_string = request.json["input"]
    dct = request.json["dct"]

    output = process(input_string, dct=dct)

    # Perform the annotation
    # root = ET.Element("root")
    # text = ET.SubElement(root, "text")
    # text.text = input_string

    # # Create the XML document
    # #tree = ET.ElementTree(root)
    return output
    # Return the XML document as a string
    #return ET.tostring(tree.getroot(), encoding='utf8').decode()

if __name__ == "__main__":
    app.run(debug=True)
