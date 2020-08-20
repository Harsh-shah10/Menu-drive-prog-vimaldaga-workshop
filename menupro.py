import os
paint = "mspaint"
wordpad = "write"
control = "start control"
word = "start winword"
ppt = "start powerpnt"
while True:
    print("Sir, which program would you like me to open for you: ",end='')
    p = input()
    if (("bring" in p)or("chrome" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("chrome" in p):
     os.system("chrome")
    elif (("bring" in p)or("notepad" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("notepad" in p):
     os.system("notepad")
    elif (("bring" in p)or("msconfig" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("msconfig" in p):
      os.system("msconfig")
    elif (("bring" in p)or("paint" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("paint" in p):
      os.system(paint)
    elif (("bring" in p)or("wordpad" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("wordpad" in p):
      os.system(wordpad)
    elif (("bring" in p)or("controlp" in p)or("control panel" in p)or("control" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("controlp" in p)or("control panel" in p)or("control" in p):
      os.system(control)
    elif (("ms word" in p)or("msword" in p)or("word" in p)or("bring" in p)or("controlp" in p)or("control panel" in p)or("control" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("ms word" in p)or("msword" in p)or("word" in p):
      os.system(word)
    elif (("ms powerpoint" in p)or("powerpoint" in p)or("mspowerpoint" in p)or("ms ppt" in p)or ("bring" in p)or("controlp" in p)or("control panel" in p)or("control" in p)or("run" in p)or("execute" in p)or("open" in p)or("enforce" in p)or("stsrt" in p)or("begin" in p)or("launch" in p)or("initiate" in p)or("fire up" in p)or("fire" in p)or("call" in p))and("ms word" in p)or("msword" in p)or("word" in p)or("powerpoint" in p):
      os.system(ppt)
    elif (("bring" in p)or("exit" in p)or("stop" in p)or("terminate" in p)or("switch off" in p)or("close" in p)or("end" in p)):
      break
    else:
     print('Sorry, But we still dont support this feature')
