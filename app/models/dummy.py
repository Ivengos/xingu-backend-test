from beanie import Document


class Dummy(Document):
    test: str

    class Settings:
        collection = "dummy_collection"
