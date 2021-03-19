import subprocess

# Write alda file
def writeFile():
    notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    f = open("song.txt", "w+")
    f.write("piano: a b c d e f")
    f.close()

# Play alda file
def playFile():
    subprocess.call('alda play --file "song.txt"')

writeFile()
playFile()


# Play alda line
# subprocess.call('alda play -c "piano: a b c d e f"')