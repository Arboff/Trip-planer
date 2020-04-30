import treepoem
import random
import string
from reportlab.pdfgen import canvas
import datetime




now = datetime.datetime.now()

def randomString(stringLength=10):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

generated = randomString(10)
print ("Generatin report for trip#" + generated)

canvas = canvas.Canvas('Trip ' + generated + '.pdf')

image = treepoem.generate_barcode(
    barcode_type = 'code39',
    data = generated


)

image.convert('1').save('barcode.png')
print('Done.')

canvas.setFont("Helvetica", 35)
canvas.drawCentredString(300, 750,'TRIP#' + generated,)
canvas.setFont("Helvetica", 6)
canvas.drawCentredString(300, 735,'Generated on ' + str(now),)
canvas.drawInlineImage('barcode.png', 110, 50)

canvas.showPage()
canvas.save()
