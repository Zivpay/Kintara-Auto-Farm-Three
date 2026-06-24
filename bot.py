import pyautogui as pg
import time
import math

imageOffset = 25

def get_distance(pos1, pos2):
    """Calculates the distance between two points using the Pythagorean theorem."""
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def click_closest_image(image_path):
    try:
        # 1. Get the current mouse position as the reference point
        current_mouse_pos = pg.position()
        
        # 2. Find ALL matching objects on the screen
        all_matches = list(pg.locateAllOnScreen(image_path, confidence=0.8))
        
        if not all_matches:
            print(f"Could not find any matches for: {image_path}")
            return False

        # 3. Find the object closest to the mouse position
        closest_obj = None
        shortest_distance = float('inf') # Start with infinity

        for obj in all_matches:
            # Calculate the center point of the object for better accuracy
            obj_center = (obj[0] + obj[2]//2, obj[1] + obj[3]//2)
            
            distance = get_distance(current_mouse_pos, obj_center)
            
            if distance < shortest_distance:
                shortest_distance = distance
                closest_obj = obj

        # 4. Click the closest object
        if closest_obj:
            pg.moveTo(closest_obj[0] + imageOffset, closest_obj[1] + imageOffset)
            pg.click()
            print(f"Successfully clicked closest {image_path}! Distance: {int(shortest_distance)}px")
            time.sleep(10)
            return True

    except Exception as e:
        print(f"An error occurred while scanning {image_path}: {e}")
    return False

def checkImage():
    # Storing images in a list to keep the code DRY (Don't Repeat Yourself)
    image_list = ["./image1.jpg", "./image2.jpg", "./image3.jpg"]
    
    for image in image_list:
        click_closest_image(image)

checkImage()