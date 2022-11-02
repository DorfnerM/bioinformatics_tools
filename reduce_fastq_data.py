"""reduce fastq.py
A CLI tool to randomly reduce reads in fastq files
in order to produce smaller datasets for analysis."""

__version__ = '0.1'
__author__ = 'Marco Dorfner'
__email__ = 'marco.dorfner@ur.de'
__date__ = '2022-11-02'


import argparse
import os
import random
import numpy as np


class reduce_fastq:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = 'reduce_fastq.py',
            description = 'Reduces fastq data by randomly removing reads'
        )
        self.CLI()
        self.args = self.parser.parse_args()

        self.run()

    def CLI(self):
        self.parser.add_argument(
            'fastq',
            type = str,
            help = 'path to fastq file.'
        )

        self.parser.add_argument(
            'value',
            type = float,
            help = 'Reduce fastq file to this percentage [0.00 - 1.00].'
        )

        self.parser.add_argument(
            '-o', '--out',
            metavar = '',
            type = str,
            default = os.path.join(os.path.abspath(os.getcwd()), 'reduced_fastq.fastq'),
            help = 'output path and name. Default in current directory.'
        )

        self.parser.add_argument(
            '-v', '--version',
            action = 'version',
            version = __version__
        )

    def fastq_to_ndarray(self):
        '''Transforms the input fastq file into a 2D ndarray.'''
        fastq = self.args.fastq
        fastq_reads = np.array([])
        
        with open(fastq) as infile:
            for line in infile:
                fastq_reads = np.append(fastq_reads, line)
        
        fastq_reads = fastq_reads.reshape(
            int(len(fastq_reads) / 4), 
            4
        )
        return fastq_reads

    def rm_reads(self, reads):
        '''Randomly removes reads from the fastq_to_ndarray() ndarray.
        reads: 2D ndarray of fastq reads'''
        
        filtered_reads = random.sample(
            list(reads), 
            k = round(len(reads) * self.args.value)
        )
        
        filtered_reads = np.ravel(filtered_reads)

        return filtered_reads

    def write_to_file(self, filtered_reads):
        '''Writes the filtered reads to outfile.
        filtered_reads: 1D ndarray return of rm_reads()'''
        
        if os.path.exists(self.args.out):
            os.remove(self.args.out)
        with open(self.args.out, 'x') as outfile:
            for line in filtered_reads:
                outfile.write(line)

    def run(self):
        reads_arr = self.fastq_to_ndarray()
        filtered_reads_arr = self.rm_reads(reads_arr)
        filtered_reads_arr = np.asarray(filtered_reads_arr)
        self.write_to_file(filtered_reads_arr)


def main():
        reduce_fastq()

if __name__ == "__main__":  
    main()
