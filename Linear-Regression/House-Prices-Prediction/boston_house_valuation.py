import pandas as pd
import numpy as np

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# gather data
boston_dataset = load_boston()
data = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
features = data.drop(['INDUS', 'AGE'], axis=1) # features (indus, age dropped)
log_target = np.log(boston_dataset.target)
target = pd.DataFrame(log_target, columns=['PRICE']) # target (in logs)

# set default values
property_stats = features.mean().values.reshape(1, 11) # average of all instances for each feature

# index to key features
CHAS_IDX = 2
RM_IDX = 4
PTRATIO_IDX = 8
default_ptratio = property_stats[0][PTRATIO_IDX]

# 2021 scale factor
ZILLOW_MEDIAN_PRICE = 659.8
SCALE_FACTOR = ZILLOW_MEDIAN_PRICE / np.median(boston_dataset.target)

reg = LinearRegression().fit(features, target)
fitted_vals = reg.predict(features)
mse = mean_squared_error(target, fitted_vals) # log (prices $)
rmse = np.sqrt(mse) # log (prices $)

def get_log_estimate(rooms, pt_ratio,
                     next_to_river=False, high_confidence=True):
    # config default values
    property_stats[0][RM_IDX] = rooms
    property_stats[0][PTRATIO_IDX] = pt_ratio
    if next_to_river:
        property_stats[0][CHAS_IDX] = 1
    else:
        property_stats[0][CHAS_IDX] = 0
    
    # estimate
    log_estimate = reg.predict(property_stats)[0][0]
    
    # range
    if high_confidence:
        lower_bound = log_estimate - 2*rmse
        upper_bound = log_estimate + 2*rmse
        interval = '95'
    else:
        lower_bound = log_estimate - rmse
        upper_bound = log_estimate + rmse
        interval = '68'
    
    return log_estimate, lower_bound, upper_bound, interval

def get_dollar_estimate(rm, ptratio=default_ptratio, chas=False, large_range=True):
    """
    Estimate the price of a property in the Boston Area in USD.
    It also returns the range of value for the property.
    
    Args:
        rm (int): Indicates the number of rooms in a property.
        ptratio (float): Pupils/teacher ratio at the school in the property area.
        chas (bool): True if the property is next to the Charles River, False otherwise.
        large_range (bool): Indicates the confidence of the the model in determing the range.
    """
    
    if rm < 0 or ptratio < 0:
        print('Invalid arguments.')
        return
    log_est, lower, upper, confidence = get_log_estimate(rooms=rm, 
                                                         pt_ratio=ptratio,
                                                         next_to_river=chas,
                                                         high_confidence=large_range)
    
    dll_est = np.e**log_est * 1000 * SCALE_FACTOR
    dll_low = np.e**lower * 1000 * SCALE_FACTOR
    dll_up = np.e**upper * 1000 * SCALE_FACTOR
    
    round_dll_est = np.around(dll_est, -3)
    round_dll_low = np.around(dll_low, -3)
    round_dll_up = np.around(dll_up, -3)
    
    print(f'The estimated property value is ${round_dll_est}')
    print(f'At {confidence}% confidence the valuation range is:')
    print(f'${round_dll_low} - ${round_dll_up}')