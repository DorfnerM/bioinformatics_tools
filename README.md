# bioinformatics_tools
A repository containing some of my tools relevant in everyday use bioinformatic analysis, with a large focus on next-generation sequencing data processing.

-------------------------

### Installation of tools

Option 1: Use [pyinstaller](https://pyinstaller.org/en/stable/) to create a usable package without the need of a Python interpreter and run the tool in your terminal by typing ```./name_of_tool```.

Option 2: Run the tool in your terminal with Python installed by typing ```python ./name_of_tool```.

----------------------------

### reduce_fastq_data.py
A Python CLI tool that reduces fastq files by randomly removing a certain percentage of reads in order to downsize data.

#### Usage
```
positional arguments:
  fastq          path to fastq file.
  value          Reduce fastq file to this percentage [0.00 - 1.00].

options:
  -h, --help     show this help message and exit
  -o , --out     output path and name. Default in current directory.
  -v, --version  show program's version number and exit
```
