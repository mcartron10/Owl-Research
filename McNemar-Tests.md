---
title: "McNemar Tests"
author: "Jean-Luc Cartron, Matthieu Cartron, Hunter Thompson"
date: "2023-11-25"
output: 
  html_document:
    keep_md: true
    toc: true
    toc_depth: 3
    toc_float: true
---




## Codes for McNemar tests

- cw = within habitat/buffer under current conditions; co = outside habitat/buffer under current conditions; pw = within habitat/buffer under projected future conditions; po – outside habitat/buffer under projected future conditions

## General McNemar Format


```r
OwlSpecies <- matrix(c(cw,co,pw,po),
              nrow = 2,
              dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))

mcnemar.test(OwlSpecies)
```

## Data and specific codes, McNemar test of paired proportions (2 groups)

\

### McNemar tests with the buffer:
  

1. **Flammulated Owl** 
  
|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |114|164|
| Outside buffer/current         |0  |13 |

*McNemar's chi-squared = 162.01, df = 1, p-value < 2.2e-16*


2. **Western Screech-Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |31|42|
| Outside buffer/current         |0|64 |

*McNemar's chi-squared = 40.024, df = 1, p-value = 2.509e-10*


3. **Whiskered Screech-Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |6|106|
| Outside buffer/current         |0|0|  
  
*McNemar's chi-squared = 104.01, df = 1, p-value < 2.2e-16*

4. Great Horned Owl

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |133|5|
| Outside buffer/current         |0|10 |  

*McNemar's chi-squared = 3.2, df = 1, p-value = 0.07364*

5. **Northern Pygmy-Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |37|33|
| Outside buffer/current         |0|1  |

*McNemar's chi-squared = 31.03, df = 1, p-value = 2.54e-08*

6. **Long-Eared Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |12|6|
| Outside buffer/current         |0|5 |

*McNemar's chi-squared = 4.1667, df = 1, p-value = 0.04123*

7. **Boreal Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |14|6|
| Outside buffer/current         |0|0 |

*McNemar's chi-squared = 4.1667, df = 1, p-value = 0.04123*

8. **Northern Saw-Whet Owl**

|          | Within buffer/projected| Outside buffer/projected| 
|:----------:|:----------:|:----------:|
| Within buffer/current          |15|13|
| Outside buffer/current         |0|6  |

*McNemar's chi-squared = 11.077, df = 1, p-value = 0.0008741*

### R code for individual contingency tables and tests:

1. **Boreal Owl**


```r
BorealOwl1 <- matrix(c(14,0,6,0), 
                     nrow = 2,
                     dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))

print(BorealOwl1)
```

```
##          Projected
## Current   Within Outside
##   Within      14       6
##   Outside      0       0
```

```r
mcnemar.test(BorealOwl1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  BorealOwl1
## McNemar's chi-squared = 4.1667, df = 1, p-value = 0.04123
```
2. **Flammulated Owl**


```r
FlammulatedOwl1 <- matrix(c(114,0,164,13), 
                          nrow = 2,
                          dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))

print(FlammulatedOwl1)
```

```
##          Projected
## Current   Within Outside
##   Within     114     164
##   Outside      0      13
```

```r
mcnemar.test(FlammulatedOwl1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  FlammulatedOwl1
## McNemar's chi-squared = 162.01, df = 1, p-value < 2.2e-16
```
3. **Northern saw-whet owl**


```r
SawwhetOwl1 <- matrix(c(15,0,13,6), 
                      nrow = 2, 
                      dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(SawwhetOwl1)
```

```
##          Projected
## Current   Within Outside
##   Within      15      13
##   Outside      0       6
```

```r
mcnemar.test(SawwhetOwl1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  SawwhetOwl1
## McNemar's chi-squared = 11.077, df = 1, p-value = 0.0008741
```

4. **Long Eared Owl**


```r
LongEaredOwl1 <- matrix(c(12,0,6,5),
                        nrow = 2,
                        dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(LongEaredOwl1)
```

```
##          Projected
## Current   Within Outside
##   Within      12       6
##   Outside      0       5
```

```r
mcnemar.test(LongEaredOwl1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  LongEaredOwl1
## McNemar's chi-squared = 4.1667, df = 1, p-value = 0.04123
```

5. **Great Horned Owl**


```r
GreatHornedOwl1 <- matrix(c(133,0,5,10), 
                          nrow = 2,
                          dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(GreatHornedOwl1)
```

```
##          Projected
## Current   Within Outside
##   Within     133       5
##   Outside      0      10
```

```r
mcnemar.test(GreatHornedOwl1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  GreatHornedOwl1
## McNemar's chi-squared = 3.2, df = 1, p-value = 0.07364
```

6. **Western Screech Owl**


```r
WesternScreech1 <- matrix(c(31,42,0,64),
                          nrow = 2,
                          dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(WesternScreech1)
```

```
##          Projected
## Current   Within Outside
##   Within      31       0
##   Outside     42      64
```

```r
mcnemar.test(WesternScreech1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  WesternScreech1
## McNemar's chi-squared = 40.024, df = 1, p-value = 2.509e-10
```

7. **Whiskered Screech Owl**


```r
Whiskered1 <- matrix(c(6,0,106,0),
                     nrow=2,
                     dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(Whiskered1)
```

```
##          Projected
## Current   Within Outside
##   Within       6     106
##   Outside      0       0
```

```r
mcnemar.test(Whiskered1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  Whiskered1
## McNemar's chi-squared = 104.01, df = 1, p-value < 2.2e-16
```
8. **Northern Pygmy-Owl**


```r
Pygmy1 <- matrix(c(37,33,0,1),
                     nrow=2,
                     dimnames = list("Current" = c("Within", "Outside"), "Projected" = c("Within", "Outside")))
print(Pygmy1)
```

```
##          Projected
## Current   Within Outside
##   Within      37       0
##   Outside     33       1
```

```r
mcnemar.test(Pygmy1)
```

```
## 
## 	McNemar's Chi-squared test with continuity correction
## 
## data:  Pygmy1
## McNemar's chi-squared = 31.03, df = 1, p-value = 2.54e-08
```


### Results of McNemar tests without the buffer

- Computed just as the above tests, though with different matrix values. 

1. BOOW (8,0,9,3) McNemar's chi-squared = 7.1111, df = 1, p-value = 0.007661
2. NSWO (4,0,18,12) McNemar's chi-squared = 16.056, df = 1, p-value = 6.151e-05
3. NOPO (9,0,38,22) McNemar's chi-squared = 36.026, df = 1, p-value = 1.947e-09
4. FLOW (23,0,225,43) McNemar's chi-squared = 223, df = 1, p-value < 2.2e-16
5. WHSO (1,0,62,49) McNemar's chi-squared = 69.014, df = 1, p-value < 2.2e-16
6. GHOW (115,0,10,23) McNemar's chi-squared = 8.1, df = 1, p-value = 0.004427
7. WESO (5,0,29,103) McNemar's chi-squared = 27.034, df = 1, p-value = 1.999e-07
8. LEOW (7,0,7,9) McNemar's chi-squared = 5.1429, df = 1, p-value = 0.02334









