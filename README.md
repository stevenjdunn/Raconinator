# Raconinator
**A tool for hands free, iterative Racon polishing of a fasta assembly using ONT reads.**

## Dependencies
- Python 3
- Minimap2
- Racon

## Quick start
    raconinator.py -i /path/to/input.fasta -l /path/to/long/reads.fastq -o /path/to/output_directory/
    
## Usage:     
    usage: raconinator.py [-h] -i [INPUT] -l [LONGREADS] [-n [NUMBER]] -o [OUTPUT]

    Hands free iterative polishing of long read assemblies with Racon

    optional arguments:
      -h, --help            show this help message and exit
      -i [INPUT], --input [INPUT]
                            FASTA file to be polished
      -l [LONGREADS], --longreads [LONGREADS]
                            Long reads to be used for polishing
      -n [NUMBER], --number [NUMBER]
                            Number of rounds of polishing (default=1)
      -o [OUTPUT], --output [OUTPUT]
                            Output directory

## Why?
I use it to polish long read assemblies from something like Canu or Miniasm to correct for errors and misassemblies. The maximum number of Racon rounds the script will perform is 5, the default is 1.

## Output contig ID's are stuffed
Use sed:

    sed -i 's/Consensus_//g' assembly_Rn.fasta
