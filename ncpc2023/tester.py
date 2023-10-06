

from subprocess import Popen, PIPE, STDOUT
import glob, sys, os


def parse(inp):
    return [i for i in [i.strip() for i in inp.split("\n")] if i]

def main():
    name = sys.argv[1]
    if name[-4:] == ".cpp":
        os.system(f"g++ -o {name[:-4]} -g {name}")
        name = name[:-4]
        commands = [name]
    elif name[-3:] == ".py":
        commands = ["python", name]
    else:
        print("Panicing")
        exit()
    print(f"Testing {name}")
    for filename in glob.glob("input/*"):
        print(f"Test: {filename}")
        file = open(filename, "r")
        dat = file.read()
        file.close()
        output = "output/" + filename.split("/", 2)[1]
        if os.path.isfile(output):
            file = open(output, "r")
            expected = file.read()
            file.close()
        else:
            expected = None
        p = Popen(commands, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=dat.encode())[0]
        if expected is not None:
            exp = parse(expected)
            got = parse(stdout_data.decode())
            #if expected == stdout_data.decode():
            if exp == got:
                print("SUCCESS")
            else:
                print(f"FAILURE")
                print(f"Expected: {[exp]}")
                print(f"Got: {[got]}")
        else:
            print(f"Got output: {stdout_data}")
        print()



if __name__ == '__main__':
    main()
