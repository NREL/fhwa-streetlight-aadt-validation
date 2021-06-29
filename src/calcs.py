"""
error calc functions
"""

def calc_aadt_error(aadt_gt, aadt_test):
    return(aadt_test-aadt_gt)

def calc_abs_aadt_error(aadt_gt, aadt_test):
    return abs(calc_aadt_error(aadt_gt, aadt_test))

def calc_pct_aadt_error(aadt_gt, aadt_test):
    assert aadt_gt > 0, "aadt_gt must be >0"
    return(calc_aadt_error(aadt_gt, aadt_test) / aadt_gt)

def calc_abs_pct_aadt_error(aadt_gt, aadt_test):
    assert aadt_gt > 0, "aadt_gt must be >0"
    return(calc_abs_aadt_error(aadt_gt, aadt_test) / aadt_gt)