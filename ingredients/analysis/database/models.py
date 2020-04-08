from typing import List, Optional


class AdditiveInfo:
    """
    Data model from JSON
    """

    def __init__(self):
        self.names: List[str] = []
        self.cas_id: str = ""
        self.fema_num: str = ""
        self.technical_effs: List[str] = []
        self.scogs_conclusion: Optional[int] = None

    def to_dict(self):
        return {
            "names": self.names,
            "cas_id": self.cas_id,
            "fema_num": self.fema_num,
            "technical_effects": self.technical_effs,
            "scogs_conclusion": self.scogs_conclusion
        }

    @classmethod
    def from_dict(cls, data):
        item = AdditiveInfo()
        item.names = data["names"]
        item.cas_id = data["cas_id"]
        item.fema_num = data["fema_num"]
        item.technical_effs = data["technical_effects"]
        item.scogs_conclusion = data["scogs_conclusion"]
        return item