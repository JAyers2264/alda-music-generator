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

    # Set starting note
    note = randint(0, len(notes)-1)
    octave = randint(0, 8)

    # Set instrument to piano, set octave
    melody = "piano: o" + str(octave) + " "
    
    # Create 4 measures of 8 notes
    for x in range(4):
        for y in range(8):
            print_octave = False
            step = 3

            # Add or subtract 3 from note
            note += randint(-step,step)

            # Wrap note around if above or below
            if note > 6:
                if octave < 8:
                    octave += 1
                    print_octave = True
                note -= 7
            elif note < 0:
                if octave > 0:
                    octave -= 1
                    print_octave = True
                note += 7

            # If octave changed, print it
            if print_octave:
                melody += "o" + str(octave) + " "

            melody += notes[note] + " "
        melody += "\n"

    return melody

# Play alda file
def playFile():
    subprocess.call('alda play --file "song.txt"')

# Export as midi
def exportFile():
    subprocess.call('alda export -f "song.txt" -o "song.mid"')

# Write and play file
writeFile()
#playFile()
exportFile()
