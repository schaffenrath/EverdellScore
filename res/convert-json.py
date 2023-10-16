import sys

if sys.argv[1] == None or sys.argv[1] == "":
    sys.exit("Specify file to convert as arg")

with open(sys.argv[1], 'r') as rfile:
    out = "{\n"
    for line in rfile:
        line = line.strip()
        if line.startswith("'"):
            out += line.replace("'", '"')
        elif line.startswith('name'):
            continue
        elif line.startswith('}') or line.startswith(']'):
            print('in except case with: ' + line)
            out += line
        else:
            parti = line.partition(':')
            out += "\"" + parti[0] + "\": "
            if parti[2].partition(',')[0].isdigit():
                out += parti[2]
            else:
                out += "\""+parti[2].partition(',')[0].strip()+"\",\n"
    out += "}\n";
    with open('out.json','w') as wfile:
        wfile.write(out)
    # print(out)


