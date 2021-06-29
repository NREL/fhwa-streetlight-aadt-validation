# fhwa-streetlight-aadt-validation

## Overview:  
Code produced for [     ] validation study to compare AADT estimates from [      ] to [      ]. For this study, [     ] were treated as "ground truth". The study's findings are documented in the publicly-available report, "[    ]". **This software is provided as-is without dedicated support**. The programming environment for this study may be reproduced with conda (installed via the Anaconda [website](https://docs.anaconda.com/anaconda/install/)):

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

## Citation:  
`Forthcoming`  
  
## License:  
This code is licensed for use under the terms of the Berkeley Software Distribution 3-clause (BSD-3) license; see **LICENSE**.
