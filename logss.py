import operator
import re
import argparse

parser = argparse.ArgumentParser(description='find 10 the most popular threads in log')
parser.add_argument('fpath', type=str, help='path to file with log')
args = parser.parse_args()

with open(args.fpath, "r") as logfile:
    read_data = logfile.read()
    pattern_begin = r'\d{4}-\d{2}-\d{2}' + r'\s+' + r'\d{2}:\d{2}:\d{2}' + r'\s+\S*' + r'\s+\S*' + r'\s+\S*'
    threads = set(re.findall(pattern_begin + r'\s+(\S*)', read_data))
    book = {k: len(re.findall(pattern_begin + '\s+' + k + r'\s+', read_data)) for k in threads}
    top = sorted(book.items(), key=operator.itemgetter(1))
    for thread, count in top[:-11:-1]:
        print(thread, count)
