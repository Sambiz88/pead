"""

class ETLPipeline:
    def __init__(self):
        self.extractor = APIExtractor(endpoint="https://example.com/data")
        self.transformer = CleaningTransformer()
        self.loader = WarehouseLoader(table="sales")

    def run(self):
        raw = self.extractor.extract()
        cleaned = self.transformer.transform(raw)
        self.loader.load(cleaned)


if __name__ == "__main__":
    pipeline = ETLPipeline()
    pipeline.run()"""

import extractor, transformer, storage

extractor.extract()
transformer.transform()
