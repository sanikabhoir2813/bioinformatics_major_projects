from pathlib import Path
import pandas as pd
import numpy as np

file_path = Path(__file__).parent / "data" / "biological_samples.csv"
df = pd.read_csv(file_path)
results_dir = Path(__file__).parent / "results"
results_dir.mkdir(parents=True, exist_ok=True)

print("ORIGINAL BIOLOGICAL DATA")
print(df)

print("\nDATASET INFORMATION")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column names:", df.columns.tolist())

print("\nMISSING VALUES")
print(df.isnull().sum())

df["Length"] = df["Length"].fillna(
    df["Length"].median()
)

df["GC_Content"] = df["GC_Content"].fillna(
    df["GC_Content"].mean()
)

df = df.drop_duplicates()

average_length = np.mean(df["Length"])
average_gc = np.mean(df["GC_Content"])

print("\nBIOLOGICAL DATA STATISTICS")
print("Average length:", round(average_length, 2))
print("Average GC content:", round(average_gc, 2), "%")

high_gc = df[df["GC_Content"] > 50]

print("\nHIGH GC CONTENT SAMPLES")
print(high_gc)

df.to_csv(results_dir / "cleaned_biological_samples.csv", index=False)

high_gc.to_csv(results_dir / "high_gc_samples.csv", index=False)
    
print("\nAnalysis completed successfully!")
print("Files saved in results folder.")