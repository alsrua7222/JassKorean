# war3 mpq파일 구성 내용
class Config:
    def __init__(self):
        self.filesDictionary = {
            "war3map.w3u": {
                "name": "units",
                "props": {
                    "unam": "name",
                    "upro": "properNames",
                    "uawt": "awakenTip",
                    "utip": "tip",
                    "utub": "uberTip",
                    "utpr": "reviveTip",
                },
                "ignore": ["unsf"],
            },
            "war3map.w3a": {
                "name": "abilities",
                "props": {
                    "anam": "name",
                    "atip": "tip",
                    "aub1": "uberTip",
                    "aret": "researchTip",
                    "arut": "researchUberTip",
                    "aut1": "unTip",
                    "auu1": "unUberTip",
                },
                "ignore": ["ansf", "arhk", "ahky", "auhk"],
            },
            "war3map.w3t": {
                "name": "items",
                "props": {
                    "unam": "name",
                    "utub": "uberTip",
                    "utip": "tip",
                    "ides": "description",
                },
            },
            "war3map.w3h": {
                "name": "buffs",
                "props": {
                    "fnam": "name",
                    "fube": "uberTip",
                    "ftip": "tip",
                },
            },
            "war3map.w3q": {
                "name": "upgrades",
                "props": {
                    "gnam": "name", 
                    "gub1": "uberTip", 
                    "gtp1": "tip",
                },
                "ignore": ["gef1"],
            },
            "war3map.w3b": {
                "name": "destructables",
                "props": {
                    "bnam": "name",
                    "bube": "uberTip",
                    "btip": "tip",
                },
            },
            "war3map.w3d": {
                "name": "doodads",
                "props": {
                    "dnam": "name",
                    "dube": "uberTip",
                    "dtip": "tip",
                },
            },
            "war3map.w3i": {
                "name": "info",
                "toJson": Translator.Info.warToJson,
                "toWar": Translator.Info.jsonToWar,
                "afterParse": False,
                "empty": {},
            },
            "war3map.j": {
                "name": "script",
                "toJson": (lambda b: b),
                "toWar": (lambda b: b),
                "afterParse": False,
                "empty": "",
            },
            "war3mapSkin.txt": {
                "name": "interface",
                "toJson": Interface.toJson,
                "toWar": Interface.toWar,
                "afterParse": False,
                "empty": {},
                "ignore": ["Terrain", "WorldEditMisc", "WorldEditStrings", "CustomSkin"],
            },
            "war3map.wts": {
                "name": "strings",
                "toJson": Translator.Strings.warToJson,
                "toWar": Translator.Strings.jsonToWar,
                "afterParse": False,
                "empty": {},
            },
            "units\\CommandStrings.txt": {
                "name": "commandStrings",
                "toJson": Interface.toJson,
                "toWar": Interface.toWar,
                "afterParse": False,
                "empty": {},
                "ignore": [],
            }
        }
        self.initialize()
        return
    
    def toEntries(self, data: dict):
        for entries in data.values():
            for key in entries.keys():
                info = {}
                for modification in entries[key]:
                    info[modification.id] = info[modification.id] or []
                    info[modification.id].append(modification)
                entries[key] = info
        return
    
    def initialize(self):
        for file in self.filesDictionary.keys():
            if "afterParse" not in self.filesDictionary[file]:
                file.afterParse = self.toEntries
            if "empty" not in self.filesDictionary[file]:
                file.empty = {"custom": {}, "original": {}}
            if "toJson" not in self.filesDictionary[file]:
                file.toJson = Translator.warToJson.bind(None, file["name"])
            if "toWar" not in self.filesDictionary[file]:
                file.toWar = Translator.jsonToWar.bind(None, file["name"])
        return
