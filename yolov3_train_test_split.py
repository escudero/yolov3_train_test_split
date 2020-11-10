from glob import glob
from sklearn.model_selection import train_test_split
from collections import Counter, defaultdict
import sys, getopt


def show_result(y_train, y_test):
  y_train_objs = '-'.join(y_train).split('-')
  y_test_objs = '-'.join(y_test).split('-')

  y_total = defaultdict(lambda: 0)

  y_train_objs_counter = Counter(y_train_objs)
  y_test_objs_counter = Counter(y_test_objs)

  for k, v in y_train_objs_counter.items():
    y_total[k] += v
  for k, v in y_test_objs_counter.items():
    y_total[k] += v

  print(',-------,-----------,----------,--------,')
  print('| LABEL | TRAIN (%) | TEST (%) | TOTAL  |')
  print('|-------|-----------|----------|--------|')
  for k, total in y_total.items():
    train_percent = round((y_train_objs_counter[k] * 100) / total, 2)
    test_percent = round((y_test_objs_counter[k] * 100) / total, 2)
    print(f'| {k:<5} | {train_percent:<9} | {test_percent:<8} | {total:<6} |')
  print('`-------\'-----------\'----------\'--------´')


def split(data_file, train_file, test_file, test_size=0.2, random_state=None, debug=False):
  with open(data_file, 'r') as f:
    values = []
    target = []
    for line in f:
      line = line.strip()
      values.append(line)
      klass = '-'.join(sorted(set([o.split(',')[-1] for o in line.split(' ')[1:]])))
      if len(klass) == 0:
        klass = 'X'
      target.append(klass)

  X_train, X_test, y_train, y_test = train_test_split(values, target, test_size=debug, random_state=random_state)

  with open(train_file, 'w') as filehandle:
    filehandle.writelines(f"{line}\n" for line in X_train)
  with open(test_file, 'w') as filehandle:
    filehandle.writelines(f"{line}\n" for line in X_test)

  if debug:
    show_result(y_train, y_test)


if __name__ == '__main__':
    command_help = 'yolov3_train_test_split.py --data_file <datafile> --train_file <trainfile> --test_file <testfile> --test_size <float> --random_state <integer> --debug <1 or 0>'
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'h', ['data_file=', 'train_file=', 'test_file=', 'test_size=', 'random_state=', 'debug='])
    except getopt.GetoptError:
        print(command_help)
        sys.exit(2)
    data_file, train_file, test_file, test_size, random_state, debug = [None, None, None, None, None, None]
    for opt, arg in opts:
        if opt == '-h':
            print(command_help)
            sys.exit()
        elif opt in ("--data_file"):
            data_file = arg
        elif opt in ("--train_file"):
            train_file = arg
        elif opt in ("--test_file"):
            test_file = arg
        elif opt in ("--test_size"):
            test_size = float(arg)
        elif opt in ("--random_state"):
            random_state = int(arg)
        elif opt in ("--debug"):
            debug = int(arg)
        
        debug = True if debug is None or debug == 1 else False
        
    if None in [data_file, train_file, test_file, test_size, random_state, debug]:
        print(command_help)
        sys.exit()

    split(data_file, train_file, test_file, test_size, random_state, debug)
