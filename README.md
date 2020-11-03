# YOLOv3 Train Test Split
Intelligently split YOLOv3 file into train and test subsets.

## Example:
yolov3_train_test_split.py --data_file &lt;datafile&gt; --train_file &lt;trainfile&gt; --test_file &lt;testfile&gt; --test_size &lt;float&gt; --random_state &lt;integer&gt; --debug &lt;1 or 0&gt;

python .\yolov3_train_test_split.py --data_file datasets\iris\data.txt --train_file datasets\iris\data_train.txt --test_file datasets\iris\data_test.txt --test_size 0.2 --random_state 2 --debug 1

## Debug example
<pre>,-------,-----------,----------,--------,
| LABEL | TRAIN (%) | TEST (%) | TOTAL  |
|-------|-----------|----------|--------|
| 0     | 73.8      | 26.2     | 271    |
| 1     | 73.76     | 26.24    | 202    |
| 10    | 78.26     | 21.74    | 138    |
| 2     | 76.92     | 23.08    | 338    |
| 3     | 75.26     | 24.74    | 190    |
| 4     | 78.39     | 21.61    | 310    |
| 5     | 74.71     | 25.29    | 174    |
| 6     | 78.52     | 21.48    | 284    |
| 7     | 74.19     | 25.81    | 217    |
| 8     | 79.93     | 20.07    | 274    |
| 9     | 80.65     | 19.35    | 186    |
| 11    | 85.54     | 14.46    | 166    |
| 12    | 80.65     | 19.35    | 124    |
| 13    | 81.4      | 18.6     | 129    |
| 22    | 85.19     | 14.81    | 27     |
| X     | 83.02     | 16.98    | 212    |
| 15    | 75.0      | 25.0     | 16     |
| 19    | 75.56     | 24.44    | 90     |
| 14    | 84.09     | 15.91    | 44     |
| 17    | 88.89     | 11.11    | 9      |
| 23    | 91.67     | 8.33     | 12     |
| 18    | 66.67     | 33.33    | 9      |
| 20    | 75.0      | 25.0     | 24     |
| 21    | 69.23     | 30.77    | 13     |
| 16    | 85.71     | 14.29    | 7      |
`-------'-----------'----------'--------´</pre>