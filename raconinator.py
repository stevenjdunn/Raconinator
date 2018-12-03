#!/usr/bin/env python
import subprocess
import argparse
import os
import sys

# Version
_version_ = "0.1"

# Argparse argument setup
parser = argparse.ArgumentParser(description="Hands free iterative polishing of long read assemblies with Racon")
parser.add_argument("-i", "--input", required=True, nargs='?', help="FASTA file to be polished")
parser.add_argument("-l", "--longreads", required=True, nargs='?', help="Long reads to be used for polishing")
parser.add_argument("-n", "--number", required=False, const=1, default=1, type=int, nargs='?', help="Number of rounds of polishing (default=1)")
parser.add_argument("-o", "--output", required=True, nargs='?', help="Output directory")
args = parser.parse_args()

# Colour set up
class colours:
    warning = '\033[91m'
    blue = '\033[94m'
    invoking = '\033[93m'
    bold = '\033[1m'
    term = '\033[0m'

# Five round warning
if args.number > 5:
    print(colours.warning)
    print('ERROR:')
    print('')
    print("The maximum number of rounds is limited to 5.")
    print('', colours.term)
    sys.exit(1)

# Welcome
print('')
print(colours.blue, colours.bold)
print('######################')
print('Welcome to Raconinator!')
print('######################',colours.term)

# Orientation
invoked_from = os.getcwd()
if not os.path.exists(args.output):
    os.mkdir(args.output)
    print('')
    print('Output directory created.')
    print('')
os.chdir(args.output)
output = os.getcwd()
os.chdir(invoked_from)

# Variable set up
fasta_in = args.input
reads = args.longreads
outdir = output + '/'
prefix = os.path.basename(fasta_in).replace('.fasta','')
round_one = outdir + prefix + '_R1'
round_two = outdir + prefix + '_R2'
round_three = outdir + prefix + '_R3'
round_four = outdir + prefix + '_R4'
round_five = outdir + prefix + '_R5'
fasta_one = round_one + '.fasta'
fasta_two = round_two + '.fasta'
fasta_three = round_three + '.fasta'
fasta_four = round_four + '.fasta'
fasta_five = round_five + '.fasta'
map_target = outdir + 'mapping.paf'


#  Messages
def goodbye():
    print('Done!','\n')
    print('Author: www.github.com/stevenjdunn','\n','\n')
    print(colours.bold)
    print('#########')
    print('Finished!')
    print('#########', colours.term)

def roundend():
    print(colours.bold)
    print('##############')
    print('Round Finished')
    print('##############', colours.term)
    print('')
    print('')
# Round One
print(colours.bold)
print('#########')
print('Round One')
print('#########', colours.term)
print('')

# Minimap2
print(colours.invoking)
print('Mapping reads to assembly...', colours.term)
print('')
minimapR1 = ['minimap2', '-x', 'map-ont', fasta_in, reads]
with open(map_target, "wb") as outfile:
    try:
        subprocess.call(minimapR1, stdout=outfile)
        print('')
        print(colours.bold, colours.blue,'Done!', colours.term)
        print('')
        print('')
    except Exception as e:
        print(colours.warning, 'Minimap2 failed!')
        print(e)
        print('')
        print('Check input reads.')
        print('')
        print('Exiting...', colours.term)

# Racon
print(colours.invoking)
print('Polishing assembly with Racon...', colours.term)
subprocess.call(['racon', reads, map_target, fasta_in, fasta_one])
print('')
print(colours.bold, colours.blue,'Done!', colours.term)
print('')
print('')
os.remove(map_target)
roundend()

# Exit if n = 1
if args.number == 1:
    goodbye()
    sys.exit(1)

# Round Two
print(colours.bold)
print('#########')
print('Round Two')
print('#########', colours.term)
print('')

# Minimap2
print(colours.invoking)
print('Mapping reads to assembly...', colours.term)
print('')
minimapR2 = ['minimap2', '-x', 'map-ont', fasta_one, reads]
with open(map_target, "wb") as outfile:
    try:
        subprocess.call(minimapR2, stdout=outfile)
        print('')
        print(colours.bold, colours.blue,'Done!', colours.term)
        print('')
        print('')
    except Exception as e:
        print(colours.warning, 'Minimap2 failed!')
        print(e)
        print('')
        print('Check input reads.')
        print('')
        print('Exiting...', colours.term)
# Racon
print('Polishing assembly with Racon...', colours.term)
subprocess.call(['racon', reads, map_target, fasta_one, fasta_two])
print('')
print(colours.bold, colours.blue,'Done!', colours.term)
print('')
print('')
os.remove(map_target)
roundend()

# Exit if n = 2
if args.number == 2:
    goodbye()
    sys.exit(1)

# Round Three
print(colours.bold)
print('############')
print('Round Three')
print('############', colours.term)
print('')

# Minimap2
print(colours.invoking)
print('Mapping reads to assembly...', colours.term)
print('')
minimapR3 = ['minimap2', '-x', 'map-ont', fasta_two, reads]
with open(map_target, "wb") as outfile:
    try:
        subprocess.call(minimapR3, stdout=outfile)
        print('')
        print(colours.bold, colours.blue,'Done!', colours.term)
        print('')
        print('')
    except Exception as e:
        print(colours.warning, 'Minimap2 failed!')
        print(e)
        print('')
        print('Check input reads.')
        print('')
        print('Exiting...', colours.term)
# Racon
print('Polishing assembly with Racon...', colours.term)
subprocess.call(['racon', reads, map_target, fasta_two, fasta_three])
print('')
print(colours.bold, colours.blue,'Done!', colours.term)
print('')
print('')
os.remove(map_target)
roundend()

# Exit if n = 3
if args.number == 3:
    goodbye()
    sys.exit(1)

# Round Four
print(colours.bold)
print('##########')
print('Round Four')
print('##########', colours.term)
print('')

# Minimap2
print(colours.invoking)
print('Mapping reads to assembly...', colours.term)
print('')
minimapR4 = ['minimap2', '-x', 'map-ont', fasta_three, reads]
with open(map_target, "wb") as outfile:
    try:
        subprocess.call(minimapR4, stdout=outfile)
        print('')
        print(colours.bold, colours.blue,'Done!', colours.term)
        print('')
        print('')
    except Exception as e:
        print(colours.warning, 'Minimap2 failed!')
        print(e)
        print('')
        print('Check input reads.')
        print('')
        print('Exiting...', colours.term)
# Racon
print('Polishing assembly with Racon...', colours.term)
subprocess.call(['racon', reads, map_target, fasta_three, fasta_four])
print('')
print(colours.bold, colours.blue,'Done!', colours.term)
print('')
print('')
os.remove(map_target)
roundend()

# Exit if n = 4
if args.number == 4:
    goodbye()
    sys.exit(1)

# Round Five
print(colours.bold)
print('##########')
print('Round Five')
print('##########', colours.term)
print('')

# Minimap2
print(colours.invoking)
print('Mapping reads to assembly...', colours.term)
print('')
minimapR5 = ['minimap2', '-x', 'map-ont', fasta_four, reads]
with open(map_target, "wb") as outfile:
    try:
        subprocess.call(minimapR5, stdout=outfile)
        print('')
        print(colours.bold, colours.blue,'Done!', colours.term)
        print('')
        print('')
    except Exception as e:
        print(colours.warning, 'Minimap2 failed!')
        print(e)
        print('')
        print('Check input reads.')
        print('')
        print('Exiting...', colours.term)
# Racon
print('Polishing assembly with Racon...', colours.term)
subprocess.call(['racon', reads, map_target, fasta_four, fasta_five])
print('')
print(colours.bold, colours.blue,'Done!', colours.term)
print('')
print('')
os.remove(map_target)
roundend()

# Exit
goodbye()
sys.exit(1)
