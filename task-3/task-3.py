from collections import defaultdict
import argparse

def get_detailed_info(log_type: str, data):
    for detail in data[log_type.upper()]:
        print(f'Деталі логів для рівня {log_type}',detail['date'], ' ', detail['time'], ' -- ', detail['comment'].replace('\n', '', 1))

def get_general_info(data):
    print('Рівень логування | Кількість')

    for key in data.keys():
        print(key, ' | ', len(data[key]))

def main():
    parser = argparse.ArgumentParser(description='Analyze log files')
    parser.add_argument('log_path', type=str, help='Path to the log file')
    parser.add_argument('detailed_info_log', type=str, nargs='?', default='', help='Log type for detailed info')

    args = parser.parse_args()

    with open(args.log_path) as fh:
        data = defaultdict(list)
        for line in fh.readlines():
            date, time, log_type, comment = line.split(' ', 3)
            data[log_type].append({'time': time, 'date': date, 'comment':  comment})

    if args.detailed_info_log:
        get_detailed_info(args.detailed_info_log, data)

    get_general_info(data)

if __name__ == '__main__':
    main()
