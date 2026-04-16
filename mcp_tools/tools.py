import pandas as pd
import numpy as np
import os

# --- PATH CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LOG_FILE = os.path.join(DATA_DIR, 'predictions.csv')
REF_FILE = os.path.join(MODELS_DIR, 'reference_data.csv')

def get_recent_predictions(limit: int = 50) -> list:
    """
    MCP Tool: Fetches the most recent predictions made by the system.
    Returns a list of dictionaries.
    """
    if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0:
        return []
    
    try:
        df = pd.read_csv(LOG_FILE)
        return df.tail(limit).to_dict(orient='records')
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []

def get_ref_data_stats() -> dict:
    """
    MCP Tool: Returns statistics (mean, std) of the 'Healthy' training data.
    """
    if not os.path.exists(REF_FILE) or os.stat(REF_FILE).st_size == 0:
        return {"error": "Reference data not found. Please upload a dataset first."}
    
    try:
        df = pd.read_csv(REF_FILE)
        stats = {}
        target_names = ['target', 'healthy', 'label', 'class', 'output', 'y']
        for col in df.columns:
            if col.lower() in target_names: continue
            stats[col] = {
                "mean": float(df[col].mean()),
                "std": float(df[col].std())
            }
        return stats
    except Exception as e:
        return {"error": str(e)}

def get_current_model_health() -> dict:
    """
    MCP Tool: Calculates basic health metrics from recent logs.
    """
    recents = get_recent_predictions(limit=100)
    if not recents:
        return {"status": "No data"}
    
    try:
        df = pd.DataFrame(recents)
        
        # Calculate Average Confidence
        avg_conf = 0.0
        if 'confidence' in df.columns:
            avg_conf = float(df['confidence'].mean())
        
        # Calculate Accuracy if Ground Truth exists
        accuracy = None
        if 'ground_truth' in df.columns and 'prediction' in df.columns:
            df_gt = df.dropna(subset=['ground_truth'])
            if not df_gt.empty:
                correct = df_gt[df_gt['prediction'] == df_gt['ground_truth'].astype(int)]
                accuracy = float(len(correct) / len(df_gt))
            
        return {
            "samples_analyzed": len(df),
            "avg_confidence": avg_conf,
            "estimated_accuracy": accuracy
        }
    except Exception as e:
        return {"error": str(e)}

def check_feature_drift(recent_window: int = 30) -> dict:
    """
    MCP Tool: Compares recent live traffic mean vs reference mean.
    """
    ref_stats = get_ref_data_stats()
    if "error" in ref_stats: 
        return ref_stats
    
    recents = get_recent_predictions(limit=recent_window)
    if not recents: 
        return {"status": "Not enough data"}
        
    try:
        df_live = pd.DataFrame(recents)
        drift_report = {}
        
        for feature, stats in ref_stats.items():
            if feature not in df_live.columns: 
                continue
            
            live_mean = df_live[feature].mean()
            ref_mean = stats['mean']
            ref_std = stats['std']
            
            if ref_std == 0: 
                ref_std = 0.001
            
            deviation = abs(live_mean - ref_mean) / ref_std
            
            drift_report[feature] = {
                "drift_score": float(deviation),
                "is_drifting": bool(deviation > 2.0)
            }
            
        return drift_report
    except Exception as e:
        return {"error": str(e)}
