#!/usr/bin/python
# Version 1.0 Cobbled together by kipper

import sys

def main():
  #if len(sys.argv) != 2:
  #  print("Invalid args")
  #  return
  #DataPath = sys.argv[1]
  DataPath = "draft_info.json"
  NewData = ""
  with open(DataPath, 'r') as file:
    data = file.read()
    file.close()
    sentences = data.split(">[")
    for sentence in sentences:
        sentence = " " + sentence
        sentence = sentence.replace(" it'll ", " it will ").replace(" wanna ", " want to ").replace(" gonna ", " going to ").replace(" um ", " ").replace(" uh ", " ").replace(" ah ", " ").replace(" so ", " ").replace(" you know ", " ").replace(" like ", " ").replace(" well ", " ")  .replace(" wanna]<", " want to]<").replace(" gonna]<", " going to]<").replace(" um]<", "]<").replace(" uh]<", "]<").replace(" ah]<", "]<").replace(" so]<", "]<").replace(" you know]<", "]<").replace(" like]<", "]<").replace(" well]<", "]<")
        sentence = sentence.strip()
        MyCap = sentence[0]
        MyCap = MyCap.upper()
        sentence = MyCap + sentence[1:]
        NewData += sentence + ">["

    NewData = NewData[:-2]
    with open(DataPath, 'w') as file2:
        file2.write(NewData)
    print("complete!")

if __name__ == "__main__":
  main()

