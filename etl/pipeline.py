from extract.api_extractor import APIExtractor
from transform.cleaning_transformer import CleaningTransformer
from load.warehouse_loader import WarehouseLoader


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
    pipeline.run()