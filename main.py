from cyclomatic_complexity import CyclomaticComplexity
from halsted import HalsteadMetric
from loc import LOC
import sys

def main (file):
    cyclomatic_complexity = CyclomaticComplexity(file)
    halstead_metrics = HalsteadMetric(file)
    loc = LOC(file)

    print('\n\t\t Cyclomatic Complexity \t\t')
    print('-'*70)
    cyclomatic_complexity.display_complexity()

    print('\n\n\t\t Halstead Metrics \t\t')
    print('-'*70)
    halstead_metrics.display_matrix()

    print('\n\n\t\t LOC Calculation \t\t')
    print('-'*70)
    loc.display_metrics()

if __name__ == "__main__":
    file = sys.argv[-1]
    main(file)
