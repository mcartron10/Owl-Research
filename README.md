# Owl Research

## McNemar Tests
[McNemar tests](https://github.com/mcartron10/Owl-Research/blob/main/McNemar-Tests.md)

## Model Validation


### Description
The Owl Counts code was used to validate the statistics from the paper "Climate Change Habitat Model Forecasts for Eight Owl Species in the Southwestern U.S." (Cartron et al.). It utilizes several ArcGIS layers and model functions to generate a specified number of points and calculate the number of intersections with our target habitats.

#### ArcGIS Layers
* ERU_Boundary
  * This is the layer of the owl species as created in ArcGIS Pro 3.1.x. It is a single polygon of the Ecoregion for the given species. It was built using a combination of `Select (Analysis Tool)`, `Clip (Analysis Tool)`, and `Dissolve (Data Management Tool)`
* ERU_Layer
  * This is a layer consisting of all potential ERU zones as polygons. Each polygon contains the corresponding ERU values.


#### Other Variables
* Num_Owls
  * This is an integer value corresponding with the number of observed owls for the selected species. Using the function `CreateRandomPoints`, we can generate these points across our constraining layer, `ERU_Boundary`.
* Habitat_Values
  * This is a query statement checking our expected habitat for the given owl species. From our `ERU_Layer`, we select these ERU values and count the number of intersecting points from the points we generated.
 

#### Model Workflow - ArcGIS & Python (ArcPy)
* Using `Select (Analysis Tool)` and `Clip (Analysis Tool)`, create a layer to be used for the boundary layer.
* `Dissolve (Data Management Tool)` the created layer into the `ERU_Boundary` layer.
* Within the `.py`, adjust the number of observations using `Num_Owls`, and set the target habitats in `Habitat_Values`.
* Ensure the write file, and the Workspace/Geodatabase are pathed correctly.
* Run the program and record the results

### Z-tests (results)
* One-sided Z-tests were performed to test whether the habitat model performed better than the simulations, or random model. The simulation randomly generates points across eco regions (regions in which a given owl species **could** be found) relevant to the given owl species. The link to the Z-tests can be found here: [Z-tests for each owl species](https://github.com/mcartron10/Owl-Research/blob/main/Model_Validation_Z_tests.md)  
