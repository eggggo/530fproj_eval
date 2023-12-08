import sys, getopt
from rouge_score import rouge_scorer

# calculates avg rouge score between prediction and ground truth file inputs
def rouge_score(prediction, ground_truth):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(prediction, ground_truth)
    return scores

if __name__ == '__main__':
    # read in prediction and ground truth files
    opts, args = getopt.getopt(sys.argv[1:], "hp:r:")
    for opt, arg in opts:
        if opt == '-h':
            print('rouge.py -p <prediction_file> -r <reference_file>')
            sys.exit()
        if opt == '-p':
            prediction = arg
        elif opt == '-r':
            ref_file = arg
    # calculate avg rouge1, rouge2, rougeL fscores
    predictions = open(prediction, 'r').readlines()
    refs = open(ref_file, 'r').readlines()
    rouge1 = 0
    rouge2 = 0
    rougeL = 0
    for i in range(len(predictions)):
        scores = rouge_score(predictions[i], refs[i])
        rouge1 += scores['rouge1'].fmeasure
        rouge2 += scores['rouge2'].fmeasure
        rougeL += scores['rougeL'].fmeasure
    rouge1 /= len(predictions)
    rouge2 /= len(predictions)
    rougeL /= len(predictions)
    print('rouge1: ', rouge1)
    print('rouge2: ', rouge2)
    print('rougeL: ', rougeL)