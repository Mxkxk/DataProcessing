
class mathProcess(object):
    """class for math processing"""
    @staticmethod
    def mu(data):
        return sum(data)/len(data)
    @staticmethod
    def sigma(data):
        mu = mathProcess.mu(data)        
        return (sum([(i-mu)**2 for i in data])/len(data))**0.5
    @staticmethod
    def median(data):
        if len(data)%2 == 1:
            return data[int(len(data)/2)]
        else:
            return (data[int(len(data)/2)]+data[int(len(data)/2)-1])/2
    @staticmethod
    #Method return mode
    def mode(data):
        #
        dData = {i:0 for i in data}
        for i in data:
            dData[i] = dData[i]+1
        print(list(dData.keys()), list(dData.values()).index(max(dData.values())))

        
        

