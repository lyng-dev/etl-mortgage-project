import sys
import csv
import os.path
from os import path

# check if file exists
def file_exists(filename):
  return path.exists(filename)

# extract banks from src file
def retrieve_banks(filename):
  with open(filename, newline='') as csvfile:
    table = csv.reader(csvfile, delimiter = ',', quotechar='"')
    banks = []
    for row in table:
      banks.append(row[0])

    return banks

def retrieve_bank_regs(filename):
  with open(filename, newline='') as csvfile:
    table = csv.reader(csvfile, delimiter = ',', quotechar='"')
    bank_regs = {}
    for row in table:
      bank_regs[row[1]] = row[0]

    return bank_regs

# add date to lines
def append_file(lines, filename):
  with open(filename, newline='') as csvfile:
    table = csv.reader(csvfile, delimiter = ',', quotechar='"')
    line_iter = iter(lines)
    for row in table:
      col_count = 0

      for col in list(row)[1:]:
        line = next(line_iter)
        line.append(col if len(col) > 0 else 0)
        col_count += 1

    return lines

def usage():
  print('')
  print('Usage: python3 main.py <src_filename>')
  print('')
  print('Example:')
  print('\tpython3 main.py src_sovensprocent.csv')
  print('Expected output:')
  print('\tNEW FILE: out_src_solvensprocent.csv')

def main():
  # expect input from commandline
  if len(sys.argv) < 2:
    print(f'ERROR: incorrect number of input parameters. ')
    usage()
    exit(1)
  src = sys.argv[1]

  # check if file exists, else fail
  if not file_exists(src): 
    print(f'ERROR: specified file "{src}" does not exist. Check filename and try again.')
    print('Exiting.')
    exit(1)

  # prepare program
  lines = []
  bank_regs = retrieve_bank_regs('bank-reg-nr.csv')
  banks = retrieve_banks(src)
  print(*banks, sep='\n')
  years = range(2000, 2020)

  # iterate all banks and years
  for bank in banks:
    for year in years:
      line = [bank_regs[bank], bank, year]
      lines.append(line)

  # add data
  lines = append_file(lines, src)

  # output to file
  with open("out_" +src, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(lines)

  # complete run
  print('Done.')
  exit(0)

# start executing
if __name__== "__main__":
   main()