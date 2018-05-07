import pandas as pd


class ToCsv:

    def save_on_csv(self, path, classifier_result):
        pd.DataFrame(classifier_result).to_csv('CsvResult/' + path, sep='\t', encoding='utf-8')
