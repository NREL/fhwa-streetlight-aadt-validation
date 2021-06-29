"""
plotting functions
"""

import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Color Pallettes
vol_range_narrow_color_dict = {'<500': '#277da1',
                               '500-\n1,999': '#577590',
                               '2,000-\n4,999': '#4d908e',
                               '5,000-\n9,999': '#43aa8b',
                               '10,000-\n19,999': '#90be6d',
                               '20,000-\n34,999': '#f9c74f',
                               '35,000-\n54,999': '#f9844a',
                               '55,000-\n84,999': '#f8961e',
                               '85,000-\n124,999': '#f3722c',
                               '125,000+': '#f94144'}

vol_range_wide_color_dict = {'<500 \n(very low)': '#277da1',
                             '500-\n4,999 \n(low)': '#43aa8b',
                             '5,000-\n54,999 \n(med)': '#f9844a',
                             '55,000+ \n(high)': '#f94144'}

urban_rural_color_dict = {'urban': '#7A9E9F',
                          'rural': '#FACC6B'}

data_source_color_dict = {'tmas': '#AE1E4E',
                          'toll': '#DACC3E'}

def create_state_color_palette(state_comparisons_df):
    state_color_dict = {}
    for state, color in zip(state_comparisons_df['state'],
                            sns.color_palette('husl',len(state_comparisons_df))):
        state_color_dict[state] = color
    
    return state_color_dict

def plot_urban_rural_pie(aadt_valid_df, show=True, outpath=False):
    pie_df = aadt_valid_df['urban_rural'].value_counts().reset_index()
    pie, ax = plt.subplots(figsize=[5,4])
    
    lbls = pie_df['index']
    colors = [urban_rural_color_dict[src.lower()] for src in lbls]
    
    ax.pie(pie_df['urban_rural'], 
           colors=colors,
           labels=lbls.apply(lambda x: x.capitalize()),
           autopct='%1.1f%%', 
           explode=[0, 0.02],
           textprops={'fontsize': 10})
    plt.title("AADT comparisons by urban/rural designation", fontsize=11)
    
    if outpath != False:
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()
        
def plot_data_source_pie(aadt_valid_df, show=True, outpath=False):
    pie_df = aadt_valid_df['agg_source'].value_counts().reset_index()
    pie, ax = plt.subplots(figsize=[5,4])
    
    lbls = pie_df['index']
    colors = [data_source_color_dict[src.lower()] for src in lbls]
    
    ax.pie(pie_df['agg_source'], 
           colors=colors,
           labels=lbls,
           autopct='%1.1f%%', 
           explode=[0, 0.02],
           textprops={'fontsize': 10})
    
    plt.title("AADT comparisons by data source", fontsize=11)
    
    if outpath != False:
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()
        
def plot_state_comparisons_bar(state_comparisons_df, state_palette, show=True, outpath=False):
    plt.figure(figsize=(7,3))
    for i, row in state_comparisons_df.iterrows():
        state, n = row.state, row.n
        plt.bar(i, n, color=state_palette[state], zorder=2)

    plt.xticks(range(len(state_comparisons_df)), state_comparisons_df['state'], fontsize=9)
    plt.yticks(fontsize=9)
    plt.title("AADT comparisons by state", fontsize=10)
    plt.xlabel('State', fontsize=9)
    plt.ylabel('# of Comparisons', fontsize=9)
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    if outpath != False:
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()
        

def plot_vol_bin_bar(aadt_valid_df, bin_type, gt_col, show=True, outpath=False):
    assert bin_type in ['narrow', 'wide'], "bin_type must be in ['narrow', 'wide']."
    
    if bin_type == 'wide':
        plt.figure(figsize=(5,3))
        aadt_bins = aadt_valid_df.sort_values(gt_col)['aadt_vol_bin_wide'].unique()
        for i, aadt_bin in enumerate(aadt_bins):
            aadt_valid_bin_df = aadt_valid_df[aadt_valid_df.aadt_vol_bin_wide==aadt_bin]
            plt.bar(i, len(aadt_valid_bin_df), color=vol_range_wide_color_dict[aadt_bin], zorder=2)

        plt.title("AADT comparisons by volume bin - wide", fontsize=10)
        plt.xlabel('AADT bin', fontsize=9)
        plt.ylabel('# of Comparisons', fontsize=9)
        plt.xticks(range(len(aadt_bins)), aadt_bins, fontsize=9)
        plt.grid(axis='y', linestyle='--', alpha=0.5)

        if outpath != False:
            plt.savefig(outpath, 
                        dpi=150, 
                        bbox_inches='tight')
                
    elif bin_type == 'narrow':
        plt.figure(figsize=(8,4))
        aadt_bins = aadt_valid_df.sort_values(gt_col)['aadt_vol_bin_narrow'].unique()
        for i, aadt_bin in enumerate(aadt_bins):
            aadt_valid_bin_df = aadt_valid_df[aadt_valid_df.aadt_vol_bin_narrow==aadt_bin]
            plt.bar(i, len(aadt_valid_bin_df), color=vol_range_narrow_color_dict[aadt_bin], zorder=2)

        plt.title("AADT comparisons by volume bin - narrow", fontsize=10)
        plt.xlabel('AADT bin', fontsize=9)
        plt.ylabel('# of Comparisons', fontsize=9)
        plt.xticks(range(len(aadt_bins)), aadt_bins, fontsize=9)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        
        if outpath != False:
            plt.savefig(outpath, 
                        dpi=150, 
                        bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()
        
def plot_aadt_error_scatter(aadt_valid_df, gt_col, test_col, show=True, outpath=False):
    sns.set(rc={'figure.figsize':(5,5)})
    sns.set_style("whitegrid", {'grid.linestyle': '--'})
    max_val = max(list(aadt_valid_df[gt_col]) + list(aadt_valid_df[test_col]))
    g = sns.JointGrid()
    ax = sns.regplot(data=aadt_valid_df, x=gt_col, y=test_col, ax=g.ax_joint, marker='+', color='k')
    ax.set_xlim(0, max_val)
    ax.set_ylim(0, max_val)
    bins = np.arange(0, math.ceil(max_val / 4000) * 4000 + 4000, 4000)
    sns.histplot(data=aadt_valid_df, x=gt_col, ax=g.ax_marg_x, bins=bins, color='k')
    sns.histplot(data=aadt_valid_df, y=test_col, ax=g.ax_marg_y, bins=bins, color='k')
    g.ax_joint.plot([0, max_val], [0, max_val], linestyle='--', c='firebrick', linewidth=1.5)
    g.set_axis_labels('Ground truth AADT', 'Streetlight AADT', fontsize=11)
    
    if outpath != False:
        plt.savefig(outpath, dpi=150, bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()