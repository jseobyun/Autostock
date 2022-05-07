import numpy as np

def closest_date_index(sources, target):
    if target in sources.axes[0].date:
        index = np.where(sources.axes[0].date == target)[0][0]
        print('')
    else:
        date_diff = np.abs(sources.axes[0].date - target)
        index = np.argmin(date_diff)
        if date_diff[index].days >= 3:
            print(f"{target} does not exist. Wrong date.")
            return None
        print(f"{target} is a holiday. The result of the closest day is returned.")
    return index

