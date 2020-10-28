import sys
import os

if len(sys.argv) < 3:
    print(sys.argv[0] + " <File A> <File B>")
    sys.exit(1)

fileA = sys.argv[1]
fileB = sys.argv[2]

if not os.path.isfile(fileA):
    print(fileA + " is not a file!")
    sys.exit(2)
if not os.path.isfile(fileB):
    print(fileB + " is not a file!")
    sys.exit(2)

with open(fileA) as fa, open(fileB) as fb:
    linesA = [line for line in fa]
    linesB = [line for line in fb]

lx = len(linesA) if len(linesA) < len(linesB) else len(linesB)

for i in range(lx):
    textA, textB = linesA[i], linesB[i]
    if textA == textB: continue
    ly = len(textA) if len(textA) < len(textB) else len(textB)
    # forward
    s = 0
    for j in range(ly):
        if textA[j] != textB[j]:
            s = j
            break
    #backward
    ia, ib = len(textA)-1, len(textB)-1
    while(textA[ia] == textB[ib]):
        ia -= 1
        ib -= 1

    print(f"Line {i+1}\n[A] \"{textA[s:ia]}\"\n[B] \"{textB[s:ib]}\"")

print("")
if len(linesA) != len(linesB):
    print("not equal length!")
