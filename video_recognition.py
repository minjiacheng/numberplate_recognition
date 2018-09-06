import cv2
from openalpr import Alpr
import sys
import csv

alpr = Alpr("gb", "openalpr.conf", "runtime_data")#give required region in first argument
registration_no = []
#model is region specific e.g. us, eu, au, auwide, gb, kr, mx, sg
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(1) #return top n predictions
alpr.set_default_region("gb")#set region to check if prediction matches expected plate format

cap = cv2.VideoCapture("samples/A.mp4")#specify the video here

while(True):    
    ret, frame = cap.read() 
    
    if ret:        
        cv2.imwrite("img.jpg", frame)

        results = alpr.recognize_file("img.jpg")#try to recognise each frame
        i = 0
        
        for plate in results['results']:
            i += 1
            print("Plate #%d" % i)
            print("   %12s %12s" % ("Plate", "Confidence"))
            for candidate in plate['candidates']:
                prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"

                print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))  
                #save all unique plate numbers detected
                if candidate['plate'] not in registration_no:
                    registration_no.append(candidate['plate'])
    else:
        break;

#save plate numbers to csv
with open('samples/plate_no.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(registration_no)  

# When everything done, release the capture
cap.release()
#alpr.unload()#comment out this line if wish to run program multiple times