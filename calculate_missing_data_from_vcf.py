"""
calculate_missing_data_from_vcf.py
"""

__version__ = '1.0'
__author__ = 'Marco Dorfner'
__email__ = 'marco.dorfner@ur.de'
__date__ = '2022-12-05'


import argparse
import os
import numpy as np


class calculate_missing_data_from_vcf:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = 'calculate_missing_data_from_vcf.py',
            description = 'Calculate missing data from a multi-locus vcf file.'
        )
        self.CLI()
        self.args = self.parser.parse_args()

        self.run()

    def CLI(self):
        self.parser.add_argument(
            'vcf',
            type = str,
            help = 'Input vcf file.'
        )

        self.parser.add_argument(
            '-v', '--version',
            action = 'version',
            version = __version__
        )

    def run(self):
        loci = []
        missing_data = []

        with open(self.args.vcf) as infile:
            lines = infile.readlines()

            for line in lines:
                columns = line.split('\t')

                if line.startswith('##'):
                    continue # skip header
                elif line.startswith('#CHROM'):
                    samples = columns[9:]
                    sample_count = len(samples)
                else:
                    locus = columns[0]
                    data = [i.strip() for i in columns[9:]]

                    if locus in loci:
                        continue
                    elif locus not in loci:
                        loci.append(locus)

                        missing_data_locus = data.count('.') / sample_count
                        missing_data.append(missing_data_locus)
                    else:
                        print(f'Something went wrong: {line}')
                        break
                
        missing_data = round(np.average(missing_data) * 100, 2)
        print(f'{missing_data}% missing data in vcf {self.args.vcf}')


def main():
    calculate_missing_data_from_vcf()

if __name__ == "__main__":  
    main()
