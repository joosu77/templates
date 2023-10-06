

from subprocess import Popen, PIPE, STDOUT
import glob, sys, os


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
            if expected == stdout_data.decode():
                print("SUCCESS")
            else:
                print(f"FAILURE")
                print(f"Expected: {[expected]}")
                print(f"Got: {[stdout_data.decode()]}")
        else:
            print(f"Got output: {stdout_data}")
        print()



if __name__ == '__main__':
    main()
