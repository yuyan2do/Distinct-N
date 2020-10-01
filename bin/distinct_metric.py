#!/usr/bin/env python3
import argparse
import logging

from distinct_n import distinct_n_sentence_level
from pathlib import Path
#from agenda.metric_helper import write_score

NAME = 'distinct_n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hypothesis', help="predicted text file, one example per line")
    parser.add_argument('-n', dest='n_range', type=int, nargs='+', help="n to use as in distinct-N")
    parser.add_argument('--output_dir')
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    logging.info('loading hypothesis file...')
    with open(args.hypothesis) as f:
        hypothesis = ' '.join([line.strip() for line in f.readlines()])

    output_dir = Path(args.output_dir)
    for n in args.n_range:
        print(distinct_n_sentence_level(hypothesis, n))
