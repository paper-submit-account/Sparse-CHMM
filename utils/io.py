import sys
sys.path.append('..')

from typing import Optional
from slt.eval import Metric


def write_result(file_path: str,
                 valid_results: Optional[Metric] = None,
                 best_valid_metrics: Optional[Metric] = None,
                 test_metrics: Optional[Metric] = None):
    with open(file_path, 'w') as f:
        if valid_results is not None:
            for i in range(len(valid_results)):
                f.write(f"[Epoch {i + 1}]\n")
                for k in ['precision', 'recall', 'f1']:
                    f.write(f"  {k}: {valid_results[k][i]:.4f}")
                f.write("\n")
        if best_valid_metrics is not None:
            f.write(f"[Best Validation]\n")
            for k in ['precision', 'recall', 'f1']:
                f.write(f"  {k}: {best_valid_metrics[k]:.4f}")
            f.write("\n")
        if test_metrics is not None:
            f.write(f"[Test]\n")
            for k in ['precision', 'recall', 'f1']:
                f.write(f"  {k}: {test_metrics[k]:.4f}")
            f.write("\n")
    return None
