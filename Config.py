import re

class Config:
    
    def __init__(self, _name, _value):
        self.name = _name
        self.value = _value

    def readFromFile(_filePath = ".config.txt"):
        configs = {}
        f = open(_filePath)

        _continue = True
        while _continue == True:
            try:
                _lineRaw = f.readline()
                if(re.search("^\n$", _lineRaw)):
                    _continue = False
                else:
                    if(re.search("^#",_lineRaw)):
                        print("Skipping comment line")
                    else:
                        _line = re.sub("\n", "", _lineRaw)
                        _cfgParts = _line.split("=", 1)
                        _cfgName = _cfgParts[0]
                        _cfgValue = _cfgParts[1]
                        if(_cfgName != None and _cfgValue != None):
                            configs[_cfgName] = Config(_cfgName, _cfgValue)
            except:
                _continue = False

        return configs
        #print(configs)
        
# Testing only
#a = Config.readFromFile()
#print("Configs: {}".format(a))

