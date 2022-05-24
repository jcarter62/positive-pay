import os

class PROCESS:
    _account_number: str

    def __init__(self, input_file_name='', output_file_name='', account='') -> None:
        self._account_number = account
        if len(input_file_name) > 0 and len(output_file_name) > 0:
            data = self._load_file(filename=input_file_name)
            parsed = self._parse_data(data)
            self._generate_output_file(parsed, output_file_name)
        super().__init__()

    def _load_file(self, filename) -> []:
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

    def _parse_data(self, data: []) -> []:
        result = []
        for d in data:
            amt = (d[33:13 + 33]).strip()
            alen = len(amt)
            amt = amt[:alen - 2] + '.' + amt[alen - 2:]
            amt_float = float(amt)
            amt = '{:.2f}'.format(amt_float)
            one = {
                'cheque_number': d[15:10 + 15],
                'cheque_date': f'{d[29:2 + 29]}/{d[31:2 + 31]}/{d[25:4 + 25]}',
                'cheque_amount': amt,
                'account_number': self._account_number,
                'payee_name': d[60:80]
            }
            result.append(one)
        return result

    def _generate_output_file(self, data: [], file: str):
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

