#spreadSheet only with addition operation
class Spreadsheet(object):
    def __init__(self, rows):
        self.sheet=[[0]*26 for _ in range(rows)]
    def setCell(self, cell, value):
        col=ord(cell[0])-ord('A')
        row=int(cell[1:])-1
        self.sheet[row][col]=value        
    def resetCell(self, cell):
        col=ord(cell[0])-ord('A')
        row=int(cell[1:]) -1
        self.sheet[row][col]=0
    def getValue(self, formula):
        formula=formula[1:]
        num1,num2=formula.split('+')
        if num1.isdigit():
            x=num1
        else:
            col=ord(num1[0])-ord('A')
            row=int(num1[1:])-1
            x=self.sheet[row][col]
        if num2.isdigit():
            y=num2
        else:
            col=ord(num2[0])-ord('A')
            row=int(num2[1:])-1
            y=self.sheet[row][col]
        return int(x)+int(y)
print("********* Welcome to Spreadsheet *********")
print("Commands: Spreadsheet <rows>, setCell <cell> <value>, resetCell <cell>, getValue <formula>, x to exit")
flag = True
obj = None
while flag:
    cmd = input("Enter command: ")
    if cmd == "x":
        flag = False
    else:
        parts = cmd.split(' ')
        if parts[0] == "Spreadsheet":
            obj = Spreadsheet(int(parts[1]))
            print("null")
        elif parts[0] == "setCell":
            obj.setCell(parts[1], int(parts[2]))
            print("null")
        elif parts[0] == "resetCell":
            obj.resetCell(parts[1])
            print("null")
        elif parts[0] == "getValue":
            print(obj.getValue(parts[1]))