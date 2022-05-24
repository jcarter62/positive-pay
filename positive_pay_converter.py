import os
import getopt
import sys
from reg import REG

input_file: str = ''
output_file: str = ''
account_number: str = '032005231'

def get_file_name(batch):
    global input_file
    global output_file
    input_file = f'u:\\positive_pay\\mas500\\PosPayBatchNo{batch}.ext'
    output_file = f'U:\\positive_pay\\treasurynow\\{batch}.csv'
    return

def load_file(filename) -> []:
    result = []
    f = open(filename, 'r')
    count = 0
    for line in f:
        count += 1
        row = line.strip()
        if row[0] == '1':
            result.append(row)
    f.close()
    return result

def parse_data(data: []) -> []:
    global account_number
    result = []
    for d in data:
        amt = (d[33:13+33]).strip()
        alen = len(amt)
        amt = amt[:alen-2] + '.' + amt[alen-2:]
        amt_float = float(amt)
        amt = '{:.2f}'.format(amt_float)
        one = {
            'cheque_number': d[15:10+15],
            'cheque_date': f'{d[29:2+29]}/{d[31:2+31]}/{d[25:4+25]}',
            'cheque_amount': amt,
            'account_number': account_number,
            'payee_name': d[60:80]
        }
        result.append(one)
    return result

def generate_output_file(data: [], file: str):
    qt = '"'
    qtc = qt + ','
    f = open(file, 'w')
    for line in data:
        s = ''
        s = s + qt + line['cheque_number'] + qtc
        s = s + qt + line['cheque_date'] + qtc
        s = s + qt + line['cheque_amount'] + qtc
        s = s + qt + line['account_number'] + qtc
        s = s + qt + line['payee_name'] + qtc
        s = s + qt + 'I' + qt + '\n'
        os.linesep
        f.writelines(s)
    f.close()
    return

def print_report():
    global input_file
    global output_file
    print('Conversion completed')
    print( f'Input file: {input_file}')
    print( f'Output file: {output_file}')
    return

if __name__ == '__main__':
    r = REG()
    batch = r.get_batch_no()

    batch = str(input(f'Please enter batch #, or press enter to accept #{batch} :') or batch)

    batch = batch.strip()
    get_file_name(batch=batch)
    data1 = load_file(input_file)
    data2 = parse_data(data1)
    generate_output_file(data2, output_file)
    print_report()
    r.save_batch_no(batch)
    print('Completed ... press enter')
    x = input()
