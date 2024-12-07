from psychopy import visual, core, gui
from psychopy.hardware import keyboard
import random
import csv

#initial lists
dogs = ["dog1.jpg","dog2.jpg","dog3.jpg","dog4.jpg","dog5.jpg","dog6.jpg"]
cats = ["cat1.jpg","cat2.jpg","cat3.jpg","cat4.jpg","cat5.jpg","cat6.jpg"]
pos = ['Pleasant', 'Nice', 'Enjoyable', 'Cheerful', 'Satisfying', 'Terrific']
neg = ['Poor', 'Disagreeable', 'Sad', 'Dreadful', 'Awful', 'Wrong']

#full lists for first 2 test
dog_list = random.choices(dogs, k = 16)
cat_list = random.choices(cats, k = 16)
pos_list = random.choices(pos, k = 16)
neg_list = random.choices(neg, k = 16)
animals = dog_list + cat_list
words = pos_list + neg_list

#full lists for other tests
dog_list = random.choices(dogs, k = 8)
cat_list = random.choices(cats, k = 8)
pos_list = random.choices(pos, k = 8)
neg_list = random.choices(neg, k = 8)
all_cats = dog_list + cat_list + pos_list + neg_list

#setting up window, keyboard, and file
kb = keyboard.Keyboard()
win = visual.Window([800, 800], monitor = "testMonitor", color = '#62C6F2')
datafile = open('project_data.csv', 'a', newline = '')
writer = csv.writer(datafile, delimiter = ',')
writer.writerow(["PID", "Allergy", "Pets", "Section", "Trial Number", "Stimulus", "Key", "RT", "Correct?"])

#gui for questions
questions = {"PID": '', "Do you have an allergy to cats and/or dogs?": '', "Do you have any pets at home?": ''}
questions["Do you have an allergy to cats and/or dogs?"] = ("Just cats", "Just dogs", "Both", "Neither")
questions["Do you have any pets at home?"] = ("Just cats", "Just dogs", "Both", "Neither")
gui.DlgFromDict(questions, sortKeys = False)
PID = questions["PID"]
allergy = questions["Do you have an allergy to cats and/or dogs?"]
pets = questions["Do you have any pets at home?"]

#window with instructions on how to do the test
message = visual.TextStim(win, text = "You will complete an Implicit Association Test where you will be asked to sort pictures and words into groups as quickly as possible.", color = "white")
message.draw()
win.flip()
core.wait(5)

#test for animals
def animal_test():
    message.text = "Press 'E' if the animal is a dog, and Press 'I' if the animal is a cat."
    message.draw()
    win.flip()
    core.wait(3)
    dog_picks = []
    for i in range(32):
        press_e = visual.TextStim(win, text = "Press 'E' for", color = "black", height = 0.049, pos = [-0.8, 0.97])
        press_i = visual.TextStim(win, text = "Press 'I' for", color = "black", height = 0.049, pos = [0.8, 0.97])
        dog_cat = visual.TextStim(win, text = "Dog", color = "white", pos = [-0.8, 0.9])
        cat_cat = visual.TextStim(win, text = "Cat", color = "white", pos = [0.8, 0.9])
        animal_choice = random.choice(animals)  
        stim = visual.ImageStim(win, image = animal_choice)
        press_e.draw()
        press_i.draw()
        dog_cat.draw()
        cat_cat.draw()
        stim.draw()
        win.flip()
        kb.clock.reset()
        key_press = kb.waitKeys(keyList = ['e', 'i'])
        key = key_press[0].name
        timing = key_press[0].rt
        correct = True
        if animal_choice in dogs:
            if key_press[0].name == 'i':
                correct = False
                message.text = "Wrong Answer! \nPress 'E' for Dogs."
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.25]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['e'], maxWait = 2)
        else:
            if key_press[0].name == 'e':
                correct = False
                message.text = "Wrong Answer! \nPress 'I' for Cats"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.25]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['i'], maxWait = 2)
        writer.writerow([PID, allergy, pets, "animals", i, animal_choice, key, timing, correct])
        dog_cat.draw()
        cat_cat.draw()
        press_e.draw()
        press_i.draw()
        win.flip()
        core.wait(.25)

#test for words
def word_test():
    message.text = "Press 'E' if the word is positive, and Press 'I' if the word is negative."
    message.draw()
    win.flip()
    core.wait(3)
    for i in range(32):
        press_e = visual.TextStim(win, text = "Press 'E' for", color = "black", height = 0.049, pos = [-0.8, 0.97])
        press_i = visual.TextStim(win, text = "Press 'I' for", color = "black", height = 0.049, pos = [0.8, 0.97])
        good_cat = visual.TextStim(win, text = "Positive", color = "white", pos = [-0.8, 0.9])
        bad_cat = visual.TextStim(win, text = "Negative", color = "white", pos = [0.8, 0.9])
        word_choice = random.choice(words)
        stim = visual.TextStim(win, text = word_choice, color = "white")
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        stim.draw()
        win.flip()
        kb.clock.reset()
        key_press = kb.waitKeys(keyList = ['e', 'i'])
        key = key_press[0].name
        timing = key_press[0].rt
        correct = True
        if word_choice in pos:
            if key_press[0].name == 'i':
                correct = False
                message.text = "Wrong Answer! \nPress 'E' for Positive"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.25]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['e'], maxWait = 2)
        else:
            if key_press[0].name == 'e':
                correct = False
                message.text = "Wrong Answer! \nPress 'I' for Negative"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.25]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['i'], maxWait = 2)
        writer.writerow([PID, allergy, pets, "words", i, word_choice, key, timing, correct])
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        win.flip()
        core.wait(.25)

#test associating dogs w/ good
def good_dog():
    message.text = "Press 'E' if the animal is a dog or the word is positive, and Press 'I' if the animal is a cat or the word is negative."
    message.draw()
    win.flip()
    core.wait(8)
    for i in range(32):
        press_e = visual.TextStim(win, text = "Press 'E' for", color = "black", height = 0.049, pos = [-0.8, 0.97])
        press_i = visual.TextStim(win, text = "Press 'I' for", color = "black", height = 0.049, pos = [0.8, 0.97])
        good_cat = visual.TextStim(win, text = "Positive\n or", color = "white", pos = [-0.8, 0.85])
        bad_cat = visual.TextStim(win, text = "Negative\n or", color = "white", pos = [0.8, 0.85])
        dog_cat = visual.TextStim(win, text = "Dog", color = "white", pos = [-0.8, 0.7])
        cat_cat = visual.TextStim(win, text = "Cat", color = "white", pos = [0.8, 0.7])
        choice = random.choice(all_cats)
        if choice in dogs or choice in cats:
            stim = visual.ImageStim(win, image = choice)
        else:
            stim = visual.TextStim(win, text = choice, color = "white")
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        dog_cat.draw()
        cat_cat.draw()
        stim.draw()
        win.flip()
        kb.clock.reset()
        key_press = kb.waitKeys(keyList = ['e', 'i'])
        key = key_press[0].name
        timing = key_press[0].rt
        correct = True
        if choice in pos or choice in dogs:
            if key_press[0].name == 'i':
                correct = False
                message.text = "Wrong Answer! \nPress 'E' for Positive or Dogs"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.3]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['e'], maxWait = 2)
        else:
            if key_press[0].name == 'e':
                correct = False
                message.text = "Wrong Answer! \nPress 'I' for Negative or Cats"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.3]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['i'], maxWait = 2)
        writer.writerow([PID, allergy, pets, "good+dog", i, choice, key, timing, correct])
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        dog_cat.draw()
        cat_cat.draw()
        win.flip()
        core.wait(.25)

#test associating cats w/ good
def good_cat():
    message.text = "Press 'E' if the animal is a cat or the word is positive, and Press 'I' if the animal is a dog or the word is negative."
    message.draw()
    win.flip()
    core.wait(8)
    for i in range(32):
        press_e = visual.TextStim(win, text = "Press 'E' for", color = "black", height = 0.049, pos = [-0.8, 0.97])
        press_i = visual.TextStim(win, text = "Press 'I' for", color = "black", height = 0.049, pos = [0.8, 0.97])
        good_cat = visual.TextStim(win, text = "Positive\n or", color = "white", pos = [-0.8, 0.85])
        bad_cat = visual.TextStim(win, text = "Negative\n or", color = "white", pos = [0.8, 0.85])
        dog_cat = visual.TextStim(win, text = "Cat", color = "white", pos = [-0.8, 0.7])
        cat_cat = visual.TextStim(win, text = "Dog", color = "white", pos = [0.8, 0.7])
        choice = random.choice(all_cats)
        if choice in dogs or choice in cats:
            stim = visual.ImageStim(win, image = choice)
        else:
            stim = visual.TextStim(win, text = choice, color = "white")
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        dog_cat.draw()
        cat_cat.draw()
        stim.draw()
        win.flip()
        kb.clock.reset()
        key_press = kb.waitKeys(keyList = ['e', 'i'])
        key = key_press[0].name
        timing = key_press[0].rt
        correct = True
        if choice in pos or choice in cats:
            if key_press[0].name == 'i':
                correct = False
                message.text = "Wrong Answer! \nPress 'E' for Positive or Cats"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.3]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['e'], maxWait = 2)
        else:
            if key_press[0].name == 'e':
                correct = False
                message.text = "Wrong Answer! \nPress 'I' for Negative or Dogs"
                message2 = visual.TextStim(win, text = "Press the other key to continue.", color = "white", pos = ([0.0, -0.3]))
                message.draw()
                message2.draw()
                win.flip()
                kb.waitKeys(keyList = ['i'], maxWait = 2)
        writer.writerow([PID, allergy, pets, "good+cat", i, choice, key, timing, correct])
        press_e.draw()
        press_i.draw()
        good_cat.draw()
        bad_cat.draw()
        dog_cat.draw()
        cat_cat.draw()
        win.flip()
        core.wait(.25)

#creating categories for tests
animals_v_words = [animals, words]
cat_shuffle = ["good/dog", "good/cat"]
random.shuffle(animals_v_words)
random.shuffle(cat_shuffle)

#running tests
if animals_v_words[0] == animals:
    animal_test()
    win.flip()
    core.wait(.25)
    word_test()
else:
    word_test()
    win.flip()
    core.wait(.25)
    animal_test()

win.flip()
core.wait(.25)

if cat_shuffle[0] == "good/dog":
    good_dog()
    win.flip()
    core.wait(.25)
    good_cat()
else:
    good_cat()
    win.flip()
    core.wait(.25)
    good_dog()
    
#end of experiment screen
message.text = "Congratulations! You've reached the end of the experiment."
message.draw()
win.flip()
core.wait(3)

#end of test
datafile.close()
win.close()
core.quit()