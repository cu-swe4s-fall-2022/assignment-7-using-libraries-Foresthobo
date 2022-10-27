# Your code to create majestic plots goes in here!
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    # Boxplot
    iris_df = pd.read_csv('iris.data', sep=',', header=None)
    iris_df.columns = ['sepal_width', 'sepal_length',
                       'petal_width', 'petal_length',
                       'species']
    measurement_names = ['sepal_length','sepal_width','petal_width','petal_length']
    fig_box, ax_box = plt.subplots(1,1)
    ax_box.boxplot(iris_df[measurement_names], labels=measurement_names)
    ax_box.set_ylabel('length (cm)')
    plt.savefig('iris_boxplot.png')
    
    # Scatter plot
    fig_scat, ax_scat = plt.subplots(1,1)
    for species in set(iris_df['species']):
        mask = iris_df[iris_df['species'] == species]
        ax_scat.scatter(mask['petal_length'],mask['petal_width'], label=species, alpha=.5)
    ax_scat.set_ylabel('width (cm)')
    ax_scat.set_xlabel('length (cm)')
    ax_scat.set_title('Petal length vs Petal width')
    ax_scat.legend()
    plt.savefig('petal_width_v_length_scatter.png')
    
    # Multi-panel
    fig, axes = plt.subplots(1,2)
    fig.set_size_inches(10,5)
    
    # Left Plot
    axes[0].boxplot(iris_df[measurement_names], labels=measurement_names)
    axes[0].set_ylabel('length (cm)')
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    
    # Right Plot
    for species in set(iris_df['species']):
        mask = iris_df[iris_df['species'] == species]
        axes[1].scatter(mask['petal_length'],mask['petal_width'], label=species, alpha=.5)
    axes[1].set_ylabel('width (cm)')
    axes[1].set_xlabel('length (cm)')
    axes[1].set_title('Petal length vs Petal width')
    axes[1].legend()
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    plt.savefig('multi_panel_figure.png')

if __name__ == '__main__':
    main()