__author__ = 'sharad'

def main():
    FilePath = "../../ResCode/outfile.txt"
    ofr = OpFileReader()
    con = ofr.ReadFileInBuffer(FilePath)
    RegValContr = {"stato":{}, "cont1":{}, "r_in":{}, "cont":{}}
    for line in con:
        linelst = line.strip().split()
        if(len(linelst) == 8):
            for RegName, RegValue in ofr.generatefunc(linelst):
                RegVal = int(RegValue)
                if(RegValContr[RegName]. has_key(int(RegVal))):
                    RegValContr[RegName][RegVal] += 1
                else:
                    RegValContr[RegName][RegVal] = 1

    RegValContr["cont1int"] = {}
    for RegVal in RegValContr["cont1"]:
        RegValContr["cont1int"][ofr.TwoCompl32bits(RegVal)] = RegValContr["cont1"][RegVal]
    print(RegValContr)

class OpFileReader():
    def ReadFileInBuffer(self, FileName):
        """
        Reads a file and returns it in a buffer
        """
        FileH = open(FileName)
        FileCon = []
        for line in FileH:
            FileCon.append(line)
        FileH.close()
        return FileCon

    def TwoCompl32bits(self, val):
        """
        For a given number in 32 bit 2's complement format.
        return the value of it
        """
        numbits = 32
        if( (val & (1<<(numbits - 1))) != 0):
            val = val - (1<<numbits)
        return val

    def generatefunc(self, linelst):
        """
        Generator function which returns 2 elements of a list.
        For b10, each of 4 register name and values is returned in each call
        """
        i = 0
        while(i<4):
            yield linelst[(i*2) + 0], linelst[(i*2) + 1]
            i += 1
        return

if __name__ == "__main__": main()