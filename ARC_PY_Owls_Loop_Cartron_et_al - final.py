
import time
import arcpy
from sys import argv
import numpy as np
Num_Owls = k # Insert k number of counts (owl observations) for simulation. Used in CalculateRandomIntersection() function argument

# Habitat_Values argument of CalculateRandomIntersection() function takes ERU habitat codes: e.g. SFF, or Spruce-fir Forest, etc . . .  

def CalculateRandomIntersection(ERU_Boundary = "Boundary", Number_of_Random_Points = Num_Owls, ERU_Layer = "OwlSpecies_ERU_Zones", Habitat_Values = "ERUcodeCCVAfinal = 'SFF' OR ERUcodeCCVAfinal = 'MEW' OR ERUcodeCCVAfinal = 'MPO'"):  # Counting # of Random Intersections

    
    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True


    # Process: Select (Select) (analysis)
    
    SelectedHabitats = "C:\path\to\Selected\Habitat"
    arcpy.analysis.Select(in_features = ERU_Layer.__str__().format(**locals(),**globals()), out_feature_class = SelectedHabitats, where_clause = Habitat_Values.__str__().format(**locals(),**globals()))

    # Process: Create Random Points (Create Random Points) (management)
    #print("Create Points")
    GeneratedPoints = arcpy.management.CreateRandomPoints(out_path = "C:\path\to\arc\project.gdb", out_name = "RandomGeneratedPoints", constraining_feature_class = ERU_Boundary.__str__().format(**locals(),**globals()), number_of_points_or_field=Number_of_Random_Points.__str__().format(**locals(),**globals()), create_multipoint_output="MULTIPOINT")[0]

    # Process: Intersect (Intersect) (analysis)

    IntersectingPoints = "C:\path\to\arc\project.gdb\IntersectingPoints"
    arcpy.analysis.Intersect(in_features = [[SelectedHabitats, ""], [GeneratedPoints, ""]], out_feature_class = IntersectingPoints)

    # Process: Get Count (Get Count) (management)
 
    Row_Count = arcpy.management.GetCount(in_rows = IntersectingPoints)[0]
    return Row_Count

if __name__ == '__main__':
    # Global Environment settings
    file = open("C:\\path\to\text\file\species\OwlCounts.txt", "x") # File where number of intersections of a given owl species is recorded
    numCounted = []
    Broken = False
    for i in range(0,500):
        now = time.time()
        with arcpy.EnvManager(scratchWorkspace="C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb", workspace="C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb"):
            n = int(CalculateRandomIntersection(*argv[1:]))
        numCounted.append(n)
        print("Loop: ",i+1, " - ", time.time()-now,"s") # prints to console time taken in computing most recent iteration
        if n > Num_Owls: # Stops simulation if the number of intersections exceeds the number of points, which indicates incorrect number inputted for NumOwls
            Broken = True 
            break
    string_list_count = [str(value) for value in numCounted] # text file requires appended numbers (intersection counts) to be strings in order for concatenation to work
    for i in string_list_count:
        file.write(i+',')
    file.close()
    if Broken == True:
        print("Uh oh! Something went wrong!")

    # Recommend printing means, standard deviations, and outliers at regular intervals to ensure that the for loop was configured properly. However, this is optional. 
