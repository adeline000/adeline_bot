{refered to https://create.withcode.uk/python/BXv}
--pls erase--

print("Title of program: Encouragement bot")
print()
while True:
  description = input("How do you feel? Describe it in one sentence.")
  
  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("keep up the positive attitude")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("cheer up and your day would be a bit better")
      counter += 1 
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("find something to take your mind off your disappointment and remember there are always more chances to succeed")
      counter += 1

  if counter == 0:
    
      output = "Sorry, I do not understand you. Can you please use different words?"
  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)" 

  else:
    
    
