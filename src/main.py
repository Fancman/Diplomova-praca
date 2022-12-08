import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

red   = (0,0,255)
green = (0,255,0)
blue  = (255,0,0)
black = (0,0,0)
white = (255, 255, 255)

# Geometric figures settings
thickness = 3
circle_radius = 6
fill = -1 # to fill the geometric figure

# Text settings
text_thickness = 1
text_size = 0.4
title_thickness = 2
title_size = 1
title = 'Threat detection'
font = cv2.FONT_HERSHEY_SIMPLEX # or cv2.FONT_HERSHEY_PLAIN

best_weights_path = "./data/trained_weights.pt"

model = torch.hub.load('ultralytics/yolov5', 'custom', path=best_weights_path)

def collision_detection(frame, object_name, valid_persons, object_predictions_xyxy, collision_detections):
    
    best_detection = ()
    best_confidence = 0
        
    for n in range( len( object_predictions_xyxy ) ):
        
        #print(object_predictions_xyxy['confidence'][n])
        
        confidence = round(float(object_predictions_xyxy['confidence'][n]), 2) 

        if len(valid_persons) == 0:
            break

        # Object threshold
        if confidence < 0.2:
            continue
            
        if confidence < best_confidence:
            continue

        x_min = int(object_predictions_xyxy['xmin'][n])
        y_min = int(object_predictions_xyxy['ymin'][n])
        x_max = int(object_predictions_xyxy['xmax'][n])
        y_max = int(object_predictions_xyxy['ymax'][n]) 
        
        best_detection = (x_min, y_min, x_max, y_max)
        best_confidence = confidence            

        w = x_max - x_min
        h = y_max - y_min

        for valid_person in valid_persons:
            person_x_min = valid_person[0]
            person_y_min = valid_person[1]
            person_x_max = valid_person[2]
            person_y_max = valid_person[3]

            person_w = person_x_max - person_x_min
            person_h = person_y_max - person_y_min

            if (x_min < person_x_min + person_w) and (x_min + w > person_x_min) and (y_min < person_y_min + person_h) and (y_min + h > person_y_min):
                print("collision detected")
                
                if object_name in collision_detections:
                    continue
                    
                collision_detections.append(object_name)
                
    if best_detection:
         # Let's draw the bounding box  
        x_min = best_detection[0]
        y_min = best_detection[1]
        x_max = best_detection[2]
        y_max = best_detection[3]        
        
        # Let's draw the bounding box
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), red, thickness);
        cv2.putText(frame, object_name + " " + str(best_confidence), (x_min-3, y_min-5), font, text_size, green, text_thickness);

cap = cv2.VideoCapture("./data/DSCF0018.avi")

while cap.isOpened():

    # Capture the frame
    ret, frame = cap.read()

    # If we correctly captured the frame
    if ret == True:
        
        # Let's define a variable to save all the heights
        heights = 0

        # Predictions
        results = model(frame)

        # We extract the needed informations: xyxy, xywh
        predictions_xyxy = results.pandas().xyxy[0]
        predictions_xywh = results.pandas().xywh[0]

        # Let us consider only the 'person' label
        person_predictions_xyxy = predictions_xyxy[predictions_xyxy['name']=='person']
        person_predictions_xywh = predictions_xywh[predictions_xywh['name']=='person']
        
        knife_predictions_xyxy = predictions_xyxy[predictions_xyxy['name']=='knife']
        bandana_predictions_xyxy = predictions_xyxy[predictions_xyxy['name']=='bandana']
        baklava_predictions_xyxy = predictions_xyxy[predictions_xyxy['name']=='baklava']
        medical_mask_predictions_xyxy = predictions_xyxy[predictions_xyxy['name']=='medical mask']

        # Let's adjust the indeces (they might be not good since we considered just the 'person' label)
        person_predictions_xyxy.index = range(len(person_predictions_xyxy))
        person_predictions_xywh.index = range(len(person_predictions_xywh)) 
        knife_predictions_xyxy.index = range(len(knife_predictions_xyxy))
        bandana_predictions_xyxy.index = range(len(bandana_predictions_xyxy))
        baklava_predictions_xyxy.index = range(len(baklava_predictions_xyxy))
        medical_mask_predictions_xyxy.index = range(len(medical_mask_predictions_xyxy))
        
        valid_persons = []
        
        best_person_detection = ()
        best_person_confidence = 0 

        # For every person in the frame:
        for n in range(len(person_predictions_xyxy)):           
            
            confidence = round(float(person_predictions_xyxy['confidence'][n]), 2)
            
            #print(confidence, best_person_confidence)
            
            # Person threshold
            if confidence < 0.3:
                continue
                
            if confidence < best_person_confidence:
                continue
            
            # Save the coordinates of the box
            x_min = int(person_predictions_xyxy['xmin'][n])
            y_min = int(person_predictions_xyxy['ymin'][n])
            x_max = int(person_predictions_xyxy['xmax'][n])
            y_max = int(person_predictions_xyxy['ymax'][n])     
            
            valid_persons.append((x_min, y_min, x_max, y_max))
            
            best_person_detection = (x_min, y_min, x_max, y_max)
            best_person_confidence = confidence

            # and the coordinates of the center of each box
            x_center = int(person_predictions_xywh['xcenter'][n])
            y_center = int(person_predictions_xywh['ycenter'][n])           

            # and a blue dot to represent the center of the box
            #cv2.circle(frame, (x_center, y_center), circle_radius, blue, fill)
            
        if best_person_detection:
             # Let's draw the bounding box  
            person_x_min = best_person_detection[0]
            person_y_min = best_person_detection[1]
            person_x_max = best_person_detection[2]
            person_y_max = best_person_detection[3]
            
            cv2.rectangle(frame, (person_x_min, person_y_min), (person_x_max, person_y_max), red, thickness)
            cv2.putText(frame, 'Person' + str(best_person_confidence), (person_x_min-3, person_y_min-5), font, text_size, red, text_thickness)
            
            
        collision_detections = []           

        collision_detection(frame, 'bandana', valid_persons, bandana_predictions_xyxy, collision_detections)
        collision_detection(frame, 'knife', valid_persons, knife_predictions_xyxy, collision_detections)
        collision_detection(frame, 'baklava', valid_persons, baklava_predictions_xyxy, collision_detections)
        collision_detection(frame, 'medical mask', valid_persons, medical_mask_predictions_xyxy, collision_detections)
        
        for idx, collision in enumerate(collision_detections):
            cv2.putText(frame, collision + ' collision detected', (50,(50 * idx) + 50), font, title_size, white, title_thickness)
            
        # Show everything: frame, boxes, centers, average height
        cv2.imshow(title, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # If we did not capture correctly the frame we exit
    else:
        break

# Close everything in the end
cap.release()
cv2.destroyAllWindows()
