# Impossible Technology

## David Martin Carl, Tjalfe Jon Klarskov Møller, Anton Kornholt & Kasper Ravn Breindal

### Dataset

[Coin API](https://www.coinapi.io/?gclid=Cj0KCQiA_JTUBRD4ARIsAL7_VeVq1VpdI3iIWcKh00m6zOVqIqf3kVKoUOblxW49gkfQIKJx5h-uiQoaAqTREALw_wcB)

### Dependencies & how to run

The following dependencies should be installed in your system, either via `conda install` or `pip install`

```python
import pandas
import matplotlib
import numpy
```

Clone from git repository, `cd Assignment7` and run the project from command promt with the command line:

`python run.py`

Or by opening the run file in your chosen environment and running the file.

The size column in the CSV file was renamed because otherwise pandas would not function correctly. It was renamed from 'size' to 'sizetransfer'

### Images

#### Question 2
![Question 2](img/question_2.png)


### Questions

Question 1: What is the transaction with the highest volume in the timespan?

Question 2: What is the average number of transactions per hour (would look nice like a graph)?

Question 3: What is the most favourite; selling or buying?

Question 4: What is the average sale and buy price per day for the most bought currency?

Question 5: What is the total volume per day (graph)?

### Answers

1. The transaction with the highest volume is 29.38 - equivalent to just around 1.2 million DKK as of todays date.

2. The hours with the most transactions can be seen in the bar plot with the title 'Question 2'.

3. 5075 bought and 4925 sold. So buying was the favorite.

4. 6627.70 for both buying and selling, makes sense since whatever someone is selling - another one is buying.

5. The total volume is 2909.73. There is no graph, since there only is data for one day. From this result we can gather that the bulk of transactions are on very small amounts of currency, since there is 10k transactions, but only ~3k in volume. But of course, bitcoin is worth quite a lot, so this does make sense.
