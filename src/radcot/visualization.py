import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_error_distribution(errors, title="Error Distribution by Type"):
    """
    Plot distribution of errors by type.
    
    Args:
        errors (list): List of errors with type information
        title (str): Plot title
    """
    error_types = [error["type"] for error in errors]
    error_counts = pd.Series(error_types).value_counts()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=error_counts.index, y=error_counts.values)
    plt.title(title)
    plt.xlabel("Error Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt.gcf()

def plot_performance_comparison(standard_metrics, radcot_metrics, models):
    """
    Plot performance comparison between standard prompting and RadCoT.
    
    Args:
        standard_metrics (dict): Metrics for standard prompting
        radcot_metrics (dict): Metrics for RadCoT
        models (list): List of model names
    """
    metrics = ["precision", "recall", "f1"]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, metric in enumerate(metrics):
        standard_values = [standard_metrics[model][metric] for model in models]
        radcot_values = [radcot_metrics[model][metric] for model in models]
        
        x = np.arange(len(models))
        width = 0.35
        
        axes[i].bar(x - width/2, standard_values, width, label='Standard')
        axes[i].bar(x + width/2, radcot_values, width, label='RadCoT')
        
        axes[i].set_title(f"{metric.capitalize()}")
        axes[i].set_xticks(x)
        axes[i].set_xticklabels(models)
        axes[i].legend()
    
    plt.tight_layout()
    
    return fig

def plot_reasoning_patterns(pattern_data):
    """
    Plot reasoning pattern correlations and distribution.
    
    Args:
        pattern_data (dict): Data about reasoning patterns
    """
    patterns = ["Cross-sectional Correlation", "Sequential Verification", "Confidence Assessment"]
    correlations = [0.91, 0.72, 0.68]  # From the paper
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(patterns, correlations)
    plt.ylabel("Correlation with Performance (r)")
    plt.title("RadCoT Reasoning Patterns")
    plt.ylim(0, 1.0)
    
    # Add correlation values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'r={height:.2f}', ha='center', va='bottom')
    
    plt.tight_layout()
    
    return plt.gcf()