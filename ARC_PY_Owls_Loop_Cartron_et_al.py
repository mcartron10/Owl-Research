import random
import time
import arcpy
from sys import argv
import numpy as np
Num_Owls = 137


def CalculateRandomIntersection(ERU_Boundary="Boundary_WS", Number_of_Random_Points=Num_Owls, ERU_Layer="WesternScreech_ERU_Zones", Habitat_Values="ERUcodeCCVAfinal LIKE '%PJO%' OR ERUcodeCCVAfinal = 'MEW' OR ERUcodeCCVAfinal = 'MPO'"):  # Counting # of Random Intersections

    arcpy.env.parallelProcessingFactor = "80%"
    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True


    # Process: Select (Select) (analysis)
    #print("Select")
    SelectedHabitats = "C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\SelectedHabitat"
    arcpy.analysis.Select(in_features=ERU_Layer.__str__().format(**locals(),**globals()), out_feature_class=SelectedHabitats, where_clause=Habitat_Values.__str__().format(**locals(),**globals()))

    # Process: Create Random Points (Create Random Points) (management)
    #print("Create Points")
    GeneratedPoints = arcpy.management.CreateRandomPoints(out_path="C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb", out_name="RandomGeneratedPoints", constraining_feature_class=ERU_Boundary.__str__().format(**locals(),**globals()), number_of_points_or_field=Number_of_Random_Points.__str__().format(**locals(),**globals()), create_multipoint_output="MULTIPOINT")[0]

    # Process: Intersect (Intersect) (analysis)
    #print("Intersect")
    IntersectingPoints = "C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\\IntersectingPoints"
    arcpy.analysis.Intersect(in_features=[[SelectedHabitats, ""], [GeneratedPoints, ""]], out_feature_class=IntersectingPoints)

    # Process: Get Count (Get Count) (management)
    #print("Get Count")
    Row_Count = arcpy.management.GetCount(in_rows=IntersectingPoints)[0]
    return Row_Count

if __name__ == '__main__':
    # Global Environment settings
    file = open("C:\\Users\Matthieu\Desktop\\Coding\\Western_Screech_OwlCounts.txt", "x")
    numCounted = []
    Outlier_Index = []
    Broken = False
    for i in range(0,500):
        now = time.time()
        with arcpy.EnvManager(scratchWorkspace="C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb", workspace="C:\\Users\Matthieu\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb"):
        
            n = int(CalculateRandomIntersection(*argv[1:]))
        numCounted.append(n)
        print("Loop: ",i+1, " - ", time.time()-now,"s")
        print(type(n))
        mean = np.mean(numCounted)
        sd = np.std(numCounted)
        if n > Num_Owls:
            Broken = True 
            break
        if i > 23:
            if i % 10 == 9:
                print(mean)
                print(sd)
            if (((mean + 3*sd) < n) or ((mean - 3*sd) > n)):
                Outlier_Index.append(i)
    string_list_count = [str(value) for value in numCounted]
    for i in string_list_count:
        file.write(i+',')
    file.close()
    print(Outlier_Index)
    if Broken == True:
        print("Uh oh! Something went wrong!")