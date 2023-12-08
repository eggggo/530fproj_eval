## ROUGE

### Definition

ROUGE is a common suite of evaluation metrics for text summarization and machine translation. ROUGE measures the overlap between the ground truth and prediction texts. The included script measures the average ROUGE-1, ROUGE-2, and ROUGE-L between a set of predictions and standard answers. ROUGE-N measures matching n-grams, such that ROUGE-1 measures unigram overlap, ROUGE-2 measures bigram overlap, and so on. Formally, this can be defined as:

$ROUGE - N = \frac{\sum_{S \in ReferenceSummaries} \sum_{gram_n \in S} Count_{match}(gram_n)}{\sum_{S\in ReferenceSumamries} \sum_{gram_n \in S} Count(gram_n)}$

where $n$ is the gram size and $Count_{match}(gram_n)$ is the number of n-grams that appear in both the prediction and reference summaries.

ROUGE-L measures the longest common subsequence between the prediction and reference summaries. This is defined as:

$R_{lcs} = \frac{LCS(X, Y)}{m}$

$P_{lcs} = \frac{LCS(X, Y)}{n}$

$F_{lcs} = \frac{(1 + \beta^2)R_{lcs}P_{lcs}}{R_{lcs} + \beta^2P_{lcs}}$

where $LCS(X, Y)$ is the length of the longest common subsequence between $X$ and $U$, $m$ is the length of $X$, and $n$ is the length of $Y$.

Overall, the higher the ROUGE score, the more similar the prediction is to the reference and hence the better the prediction is.

### Usage

To run the provided ROUGE script, the PyPI package `rouge-score` needs to be installed. This can be done with:

```pip install rouge-score```

Then, to output the average ROUGE-1, ROUGE-2, and ROUGE-L scores between a prediction file and a reference file, run:

```python rouge.py --p <prediction_file> --r <reference_file>```

The prediction and reference files should be formatted with a single entry on each line, ordered the same way.

For example, with a prediction file `predictions.txt` with the following content:

```
The quick brown fox jumped over the lazy dog.
The product was very good. I enjoyed it.
```

and a reference file `references.txt` with the following content:

```
The quick brown dog jumped on the log.
The product was good.
```

Running the script with:

```python rouge.py --p predictions.txt --r references.txt```

will output:

```
rouge1:  0.6862745098039216
rouge2:  0.33333333333333337
rougeL:  0.6274509803921569
```

## References

- [ROUGE: A Package for Automatic Evaluation of Summaries](https://www.aclweb.org/anthology/W04-1013.pdf)
