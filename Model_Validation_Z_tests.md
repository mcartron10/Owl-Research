Model Validation Z-tests
================
Jean-Luc Cartron, Matthieu Cartron, Hunter Thompson
2023-11-25

# Model Validation Z-tests

## Requisite Packages

``` r
library(readxl)
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.2 ──
    ## ✔ ggplot2 3.4.0      ✔ purrr   0.3.5 
    ## ✔ tibble  3.1.8      ✔ dplyr   1.0.10
    ## ✔ tidyr   1.2.1      ✔ stringr 1.4.1 
    ## ✔ readr   2.1.3      ✔ forcats 0.5.2 
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()

## Read in Data

``` r
Owl_data <- read_excel('D:\\Data\\Owl_Simulations_Final.xlsx')
```

## Variable Assignment

``` r
LEOW_intersections <- Owl_data$Long_eared_Intersections
WESO_intersections <- Owl_data$Western_Screech_Intersections
WHSO_intersections <- Owl_data$Whiskered_Screech_Intersections
NSWO_intersections <- Owl_data$Saw_Whet_Intersections
PO_intersections <- Owl_data$Northern_Pygmy_Intersections
BOOW_intersections <- Owl_data$Boreal_Intersections
GHO_intersections <- Owl_data$Great_horned_Intersections
FO_intersections <- Owl_data$Flammulated_Intersections
```

## Z-tests

1.  **Boreal Owl**

``` r
BOOW_mean_prop <- mean(BOOW_intersections)/23
BOOW_mean_prop
```

    ## [1] 0.1289565

``` r
prop.test(17, 23, p = BOOW_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## Warning in prop.test(17, 23, p = BOOW_mean_prop, alternative = c("greater"), :
    ## Chi-squared approximation may be incorrect

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  17 out of 23, null probability BOOW_mean_prop
    ## X-squared = 70.899, df = 1, p-value < 2.2e-16
    ## alternative hypothesis: true p is greater than 0.1289565
    ## 95 percent confidence interval:
    ##  0.5466515 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.7391304

2.  **Whiskered Screech Owl**

``` r
WHSO_mean_prop <- mean(WHSO_intersections)/112
WHSO_mean_prop
```

    ## [1] 0.6430714

``` r
prop.test(71, 112, p = WHSO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  71 out of 112, null probability WHSO_mean_prop
    ## X-squared = 0.010681, df = 1, p-value = 0.5412
    ## alternative hypothesis: true p is greater than 0.6430714
    ## 95 percent confidence interval:
    ##  0.5521765 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.6339286

3.  **Western Screech Owl**

``` r
WESO_mean_prop <- mean(WESO_intersections)/137
WESO_mean_prop
```

    ## [1] 0.192219

``` r
prop.test(34, 137, p = WESO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  34 out of 137, null probability WESO_mean_prop
    ## X-squared = 2.414, df = 1, p-value = 0.06013
    ## alternative hypothesis: true p is greater than 0.192219
    ## 95 percent confidence interval:
    ##  0.1894562 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.2481752

4.  **Long Eared Owl**

``` r
LEOW_mean_prop <- mean(LEOW_intersections)/23
LEOW_mean_prop
```

    ## [1] 0.3945217

``` r
prop.test(14, 23, p = LEOW_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  14 out of 23, null probability LEOW_mean_prop
    ## X-squared = 3.5655, df = 1, p-value = 0.0295
    ## alternative hypothesis: true p is greater than 0.3945217
    ## 95 percent confidence interval:
    ##  0.4178019 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.6086957

5.  **Northern Saw-whet Owl**

``` r
NSWO_mean_prop <- mean(NSWO_intersections)/34
NSWO_mean_prop
```

    ## [1] 0.3053529

``` r
prop.test(22, 34, p = NSWO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  22 out of 34, null probability NSWO_mean_prop
    ## X-squared = 17.14, df = 1, p-value = 1.736e-05
    ## alternative hypothesis: true p is greater than 0.3053529
    ## 95 percent confidence interval:
    ##  0.4913291 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.6470588

6.  **Northern Pygmy Owl**

``` r
PO_mean_prop <- mean(PO_intersections)/69
PO_mean_prop
```

    ## [1] 0.3916812

``` r
prop.test(47, 69, p = PO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  47 out of 69, null probability PO_mean_prop
    ## X-squared = 23.067, df = 1, p-value = 7.821e-07
    ## alternative hypothesis: true p is greater than 0.3916812
    ## 95 percent confidence interval:
    ##  0.5760566 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.6811594

7.  **Flammulated Owl**

``` r
FO_mean_prop <- mean(FO_intersections)/291
FO_mean_prop
```

    ## [1] 0.2856976

``` r
prop.test(248, 291, p = FO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  248 out of 291, null probability FO_mean_prop
    ## X-squared = 454.91, df = 1, p-value < 2.2e-16
    ## alternative hypothesis: true p is greater than 0.2856976
    ## 95 percent confidence interval:
    ##  0.8129122 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.8522337

8.  **Greated horned owl**

``` r
GHO_mean_prop <- (mean(GHO_intersections)/148) - 1e-10
GHO_mean_prop
```

    ## [1] 1

``` r
prop.test(125, 148, p = GHO_mean_prop, alternative = c("greater"), conf.level = 0.95, correct = TRUE)
```

    ## Warning in prop.test(125, 148, p = GHO_mean_prop, alternative = c("greater"), :
    ## Chi-squared approximation may be incorrect

    ## 
    ##  1-sample proportions test with continuity correction
    ## 
    ## data:  125 out of 148, null probability GHO_mean_prop
    ## X-squared = 3.4206e+10, df = 1, p-value = 1
    ## alternative hypothesis: true p is greater than 1
    ## 95 percent confidence interval:
    ##  0.7857401 1.0000000
    ## sample estimates:
    ##         p 
    ## 0.8445946

Note: Subtraction of arbitrarily small number from the Great horned owl
proportion of intersections was made because prop.test() requires
probabilities to be greater than zero and less than 1. The proportion of
intersection should be 100%, and thus the p-value should be 1.
Subtracting the arbitrarily small value allows for the test to be
performed without changing the value of p.
