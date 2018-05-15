
class ToCsv:

    def save_on_csv(self, path, classifier_result):
        classifier_result.to_csv('./CsvResult/' + path, sep='\t', encoding='utf-8', index=False)
