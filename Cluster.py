import numpy as np
import math

def find_distance(point1, point2):
    # Ensure both points are ordered pairs
    assert isinstance(point1, list)
    assert isinstance(point2, list)
    assert len(point1) == 2
    assert len(point2) == 2
    
    # Find the squared differences of both
    x_value = (point1[0] - point2[0])**2
    y_value = (point1[1] - point2[1])**2
    
    # Find the square root of sum
    return math.sqrt(x_value + y_value)

# Find out which cluster center is closest
def find_alignment(point):
    # Ensure point is an ordered pair
    assert isinstance(point, list)
    assert len(point) == 2
    
    # Calculate distances of point to each center
    distances = [find_distance(point, i) for i in centers]
    
    # Return closest center
    return centers[distances.index(min(distances))]

def create_alignment_lst(points):
    # Ensures only points are passed
    assert isinstance(points, list)
    # Create new dictionary to hold alignment notes
    # Points will be stored as a list for each key
    d = dict()
    
    # Run list through points
    for i in points:
        temp_key = tuple(find_alignment(i))
        # Add new key if key doesn't exist
        if temp_key not in d:
            d[temp_key] = [i]
        # Otherwise, add to existing key
        else:
            d[temp_key].append(i)
    
    return d
    
def define_new_centers(d):
    # Make sure dictionary is inputted
    assert isinstance(d, dict)
    
    # Add all centers to a list
    center_lst = []
    
    for value in d.values():
        # Find average of all x and y coordinates
        x_sum = 0
        y_sum = 0
        for i in value:
            x_sum += i[0]
            y_sum += i[1]
        x_sum, y_sum = x_sum/len(value), y_sum/len(value)
        
        # Add to list
        center_lst.append([x_sum, y_sum])
        
    return center_lst

    
# Provided sample points
pts = [[2.0, 10.0],[2.0, 5.0],[8.0, 4.0],[5.0, 8.0],[7.0, 5.0],[6.0, 4.0],[1.0, 2.0],[4.0, 9.0]]

# Establish center points
centers = [[2.0, 10.0], [5.0, 8.0], [1.0, 2.0]]

# See how points change over time
for i in range(4):     
    point_alignments = create_alignment_lst(pts)
    centers = define_new_centers(point_alignments)
    print(point_alignments)
    print(centers)
