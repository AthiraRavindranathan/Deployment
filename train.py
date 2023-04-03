import random

import nltk
import pandas as pd
from simpletransformers.classification import ClassificationModel
from simpletransformers.config.model_args import ClassificationArgs

from document_parser.utils import preprocess_text

model_args = ClassificationArgs()
model_args.num_train_epochs = 5

# Create a TransformerModel
model = ClassificationModel('roberta', 'roberta-base',  num_labels=2, args=model_args)

positive_data = pd.read_csv('../train.csv', nrows=800)
negative_data = pd.read_csv("../data1.csv")
positive_data.dropna(inplace=True)
negative_data.dropna(inplace=True)

pc = [(preprocess_text(text), 1) for text in positive_data["text"]]
ne = [(text, 0) for text in negative_data["text"]]
data = pc + ne
random.shuffle(data)
random.shuffle(data)

df = pd.DataFrame(data, columns=["text", "labels"])
df.dropna(inplace=True)

print(df)
# Train the model
model.train_model(df)
