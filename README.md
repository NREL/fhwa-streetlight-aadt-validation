# fhwa-streetlight-aadt-validation

## Overview:  
The National Renewable Energy Laboratory (NREL) was enlisted to conduct an independent validation of annual average daily traffic (AADT) estimates from the commercial data provider, Streetlight Data. This repo contains the code developed for this effort, as is documented in the publicly-available report, _Validation of Non-Traditional Approaches to Average Annual Daily Traffic (AADT) Volume Estimation_. **This software is provided as-is without dedicated support**. The programming environment for this study may be reproduced with conda (installed via the Anaconda [website](https://docs.anaconda.com/anaconda/install/)):

`conda env create -f environment.yml`

To activate the environment:  
  
`conda activate nrel-fhwa-validation`

## Project Organization:  
  
```
fhwa-streetlight-aadt-validation/
├── figs/                                             <- plots and figures
|   ├── comp-errors/                                  <- comparison error plots
|   |   ├── cdfs/                                     <- cumulative distribution function plots
|   |   |   ├── abs-error/                            <- absolute error plots
|   |   |   |   ├── by-aadt-bin-narrow/               <- group by narrow roadway AADT bin (10 bins total)
|   |   |   |   ├── by-aadt-bin-wide/                 <- group by wide roadway AADT bin (4 bins total)
|   |   |   |   ├── by-data-source/                   <- group by data source - TMAS, toll
|   |   |   |   ├── by-state/                         <- group by state
|   |   |   |   ├── by-urban/rural/                   <- group by urban/rural designation
|   |   |   |   ├── all_comparisons.png               <- plot all comparisons
|   |   |   |
|   |   |   ├── error/                                <- (signed) error plots
|   |   |       ├── ...
|   |   |
|   |   ├── histograms/                               <- histogram plots
|   |   |   ├── abs-error/    
|   |   |   |   ├── ...
|   |   |   |
|   |   |   ├── abs-pct-error/                        <- absolute percent error plots  
|   |   |   |   ├── ...
|   |   |   |
|   |   |   ├── error/                     
|   |   |   |   ├── ...
|   |   |   |
|   |   |   ├── pct-error/                            <- percent error plots  
|   |   |       ├── ...
|   |   |
|   |   ├── q-q-plots/                                <- quantile-quantile plots
|   |   |   ├── ...
|   |   |
|   |   ├── scatterplots/                             <- scatterplots
|   |       ├── ...
|   |   
|   ├── comp-summaries/                               <- data set summary plots
|       ├── data_source_pie.png                       <- "ground truth" comparisons distribution - TMAS vs. toll
|       ├── total_comparisons_by_aadt_bin_narrow.png  <- comparisons by narrow "ground truth" AADT bin
|       ├── total_comparisons_by_aadt_bin_wide.png    <- comparisons by wide "ground truth" AADT bin
|       ├── total_comparisons_by_state.png            <- comparisons by state
|       ├── urban_rural_pie.png                       <- comparisons by urban/rural designation
|
├── inpt_data/
|   ├── nrel_aadt_results_06022021.csv                <- NREL-processed AADT comparisons
|
├── nbs/                                              <- Jupyter notebooks
|   ├── analyze_aadt_estimates.ipynb                  <- nb for results generation
|
├── src/                                              <- Python source code
    ├── calcs.py                                      <- error functions
    ├── helpers.py                                    <- helper functions
    ├── visualize.py                                  <- plotting functions
```
  
## Additional Information:  
**Title**: *Validation of Non-Traditional Approaches to Average Annual Daily Traffic (AADT) Volume Estimation*  
  
**Abstract**: Over the last decade, new technologies and data have matured to the extent that several vendors have developed commercial traffic volume products based on passive data sources. These passive data may originate from vehicle-based sensors, smartphone-based GPS and location-based services (LBS) data, cell tower data, or Bluetooth detection. Additionally, improvements in cloud-based data storage and computing resources have enabled these technologies and data to be processed and made available at a scale that would have been unimaginable even a decade ago. Reliable traffic volume estimates obtained from passive data sources could reduce costs and improve efficiency for State Departments of Transportation (DOTs), Metropolitan Planning Organizations (MPOs), and local agencies. To evaluate the potential for using passive data sources to estimate annual average daily traffic (AADT), the National Renewable Energy Lab (NREL) conducted an independent validation of estimates from a commercial data provider, Streetlight Data. NREL’s research found that the AADT estimates derived from passive data sources are highly correlated with ground truth data obtained from permanently installed counters, though nonnegligible errors were observed. The findings suggest that passive data sources can play an important role in a comprehensive approach to traffic monitoring. Depending on specific agency needs, estimates from passive data collection may supplement or replace existing data sources, potentially reducing the cost of data collection and increasing coverage.

## Citation:  
`Forthcoming`  
  
## License:  
This code is licensed for use under the terms of the Berkeley Software Distribution 3-clause (BSD-3) license; see **LICENSE**.
