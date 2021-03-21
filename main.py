import subprocess
from random import randint
subprocess.call('alda up')

# Write alda file
def writeFile():
    f = open("song.txt", "w+")
    f.write(createMelody())
    f.close()

# Get the composition key
def determineKey():
    full_notes = ['c', 'c+', 'd', 'd+', 'e', 'f', 'f+', 'g', 'g+', 'a', 'a+', 'b']
    major_scale = [2, 2, 1, 2, 2, 2, 1]
    minor_scale = [2, 1, 2, 2, 1, 2, 2]
    scale = []
    scale_text = ""
    front_notes = []
    back_notes = []

    #key_note = randint(0, len(full_notes)-1)
    #scale_int = randint(0, 1)	

    if scale_int == 0:
        scale = major_scale
        scale_text = "major"
    else:
        scale = minor_scale
        scale_text = "minor"

    print("Key: " + full_notes[key_note] + " " + scale_text)

    # Add first note to key
    looped = False

    # Add notes to scale pieces
    for x in range(len(scale)):
        key_note += scale[x]
        if key_note > (len(full_notes)-1):
            key_note -= len(full_notes)
            looped = True

        if looped:
            front_notes.append(full_notes[key_note])
        else:
            back_notes.append(full_notes[key_note])

    # Combine scale pieces into one note scale
    notes = front_notes + back_notes
    
    print(notes)

    return notes

# Write melody
def createMelody():
    notes = determineKey()

    # Set starting note
    note = randint(0, len(notes)-1)
    octave = randint(0, 8)

    # Set instrument to piano, set octave
    melody = "piano: o" + str(octave) + " "
    
    # Create 4 measures
    for x in range(4):

        # Set measure length to 16 sixteenth notes
        measure_length = 16
        note_lengths = [16, 8, 4, 2, 1]

        while measure_length > 0:

            # Only use notes that still fit within the remaining measure capacity
            current_note_lengths = []
            for length in note_lengths:
                if 16/length <= measure_length:
                    current_note_lengths.append(length)

            print_octave = False
            step = 3

            # Pick a note length that fits
            note_length = current_note_lengths[randint(0, len(current_note_lengths)-1)]
            measure_length -= 16/note_length

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

            melody += notes[note] + str(note_length) + " "
        melody += "| "

    return melody

# Play alda file
def playFile():
    subprocess.call('alda play --file "song.txt"')

# Export as midi
def exportFile():
    subprocess.call('alda export -f "song.txt" -o "song.mid"')

# Write and play file
writeFile()
playFile()
exportFile()
