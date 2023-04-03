# # load trained model
# import nltk
# from simpletransformers.classification import ClassificationModel
#
# from document_parser.utils import detect_model_version
#
# print("Downloading NLTK Data from main file..................")
# # essential entity models downloads
# nltk.downloader.download('stopwords')
# nltk.downloader.download('maxent_ne_chunker')
# nltk.downloader.download('words')
# nltk.downloader.download('treebank')
# nltk.downloader.download('maxent_treebank_pos_tagger')
# nltk.downloader.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
#
# model_path = detect_model_version()
#
# trained_model = ClassificationModel(
#     "roberta",
#     model_path,
#     num_labels=2,
#     use_cuda=False
# )
