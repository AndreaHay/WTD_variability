import numpy as np

# functions to calculate ZWD

def wetRefractivityCalc(air_temp, rel_hum):
    E = saturationVapourPres(air_temp)
    p_wet = partialPressureVapour(rel_hum, E)
    inv_Zw = invZw(p_wet, air_temp)
    N_wet = Nw(p_wet, air_temp, inv_Zw, k2prime, k3)
    return N_wet

def invZw(p_wet, T):
    inv_Zw = 1 + 1650*(p_wet/T**3)*(1-0.01317*(T-273.15) +  (1.75e-4)*(T-273.15)**2 + (1.44e-6)*(T-273.15)**3)
    return inv_Zw

def Nw(p_wet, T, inv_Zw, k2prime, k3):
    N = (k2prime*p_wet*inv_Zw/T) + (k3*p_wet*inv_Zw/(T**2))
    return N

def k2prime(k1, k2, M_w = 18.01528, M_d = 28.9647):
    k2prime = k2 - k1*(M_w/M_d)
    return k2prime

k1 = 77.6900 # K/hPa varies negligibly with atmosphericc carbon dioxide concentration
k2 = 71.2952 # K/hPa
k3 = 375463 # K^2/hPa

# Molar masses are constant up until > 100 km
M_w = 18.01528 # Molar mass of water vapour in g/mol
M_d = 28.9647 # Molar mass of dry air in g/mol
k2prime = k2prime(k1, k2)

def saturationVapourPres(T):
    import numpy as np
    T_cel = T - 273
    E = 6.1078*np.exp((17.1*T_cel)/(235+T_cel))
    return E

def partialPressureVapour(rel_humidity, satVapPres):
    p_w = rel_humidity*satVapPres
    return p_w

# function to get dates in range
def date_range_subdirs(start_date, end_date, directory_path):
    import os
    from datetime import datetime, timedelta
    date_format = "%Y%m%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta = timedelta(days=1)  # Set the interval as needed (1 day in this example)

    subdirs = []

    current_date = start_date
    while current_date <= end_date:
        subdir = current_date.strftime(date_format)
        subdir_path = os.path.join(directory_path, subdir)
        
        if os.path.exists(subdir_path) and os.path.isdir(subdir_path):
            subdirs.append(subdir)
        
        current_date += delta

    return subdirs