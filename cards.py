from reportlab.lib.pagesizes import letter, A4, A4, A5
from reportlab.lib.units import inch, cm, mm
from reportlab.pdfgen import canvas
    
verticalCells = 5
horizontalCells = 2
pdfSize = A4
    
barWidth = 5
includeBars = True
barColour = "blue"

marking = "A" #A string that will be displayed at the bottom right of each card
includeMarkings = False
markingColor = "black"
spaceFromLeftBorder = 0.95 #the horizontal Starting Position of the String, as a Scalar of the cell width, so if the String is longer, this might need to be decreased
spaceFromBottomBorder = 0.05 #the vertical Starting Position, also a scalar starting from the bottom border of the Cell

generateBlankBackside = True
generateTemplates=False
templateColours = ["white", "silver", "gray", "black", "red", "maroon", "yellow", "olive", "lime", "green", "aqua", "teal", "blue", "navy", "fuchsia", "purple", "brown", "violet"]

def printPage(colour = "blue", title = ""):
    fileName = colour+"_"+str(includeBars)+"_"+str(barWidth)+"_"+str(horizontalCells)+"x"+str(verticalCells)
    if includeMarkings:
        fileName += "_"+marking
    fileName += "_card_Template.pdf"   
    
    if len(title) != 0:
        fileName = title+"_"+str(horizontalCells)+"x"+str(verticalCells)+"_card_Template.pdf"
        
    c = canvas.Canvas(fileName, pagesize=pdfSize)
    width, height = pdfSize
   
    for i in range(horizontalCells):
        c.line(i*width/horizontalCells ,0, i*width/horizontalCells, height)
            
    for i in range(verticalCells):
        c.line(0,i*height/verticalCells,width,i*height/verticalCells)

    #draw border:
    c.line(0,0,width,0) #bottom horizontal
    c.line(0,height,width,height) #top horizontal
    c.line(0,0,0,height) #left vertical
    c.line(width,0,width,height) #right vertical

    #draw Coloured Stripes:
    c.setStrokeColorRGB(0,0,0)
    c.setFillColor(colour)

    if includeBars:
        for i in range(horizontalCells):
            horizontalPos = width*(i/horizontalCells)
            c.rect(width*(i/horizontalCells)+barWidth,0,barWidth,height, fill=1)
            
    if includeMarkings:
        c.setFillColor(markingColor)
        
        for y in range(verticalCells):
            for x in range(horizontalCells):
                horizontalPos = width*(x/horizontalCells)+(width/horizontalCells)*spaceFromLeftBorder
                c.drawString(horizontalPos, y*height/verticalCells+ height/verticalCells*spaceFromBottomBorder, marking)
    c.save()
    print("done with "+ str(colour))
    
printPage(barColour)
if generateTemplates:
    for colour in templateColours:
        printPage(colour)
if generateBlankBackside:  
    includeBars = False
    includeMarkings = False
    printPage("white", "Blank_Backside")