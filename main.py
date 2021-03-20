import subprocess
from random import randint
subprocess.call('alda up')

# Write alda file
def writeFile():
    f = open("song.txt", "w+")
    f.write(createMelody())
    f.close()

# Write melody
def createMelody():
    notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    melody = "piano: "
    
    # Create 4 measures of 8 notes
    for x in range(4):
        for y in range(8):
            melody += notes[randint(0,len(notes)-1)] + " "
        melody += "\n"
    return melody

# Play alda file
def playFile():
    subprocess.call('alda play --file "song.txt"')

writeFile()
playFile()


# Play alda line
# subprocess.call('alda play -c "piano: a b c d e f"')