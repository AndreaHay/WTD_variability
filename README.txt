==============
ABOUT
==============

The zipped files "SWOT_troposphere_investigations_data.zip" and "SWOT_troposphere_investigations_software.zip" contain data and python jupyter notebooks supporting the research presented in GRL publication "Small scale variability in the wet troposphere impacts the interpretation of SWOT satellite observations", Hay et al., 2024. The analysis covers Australian coastal regions during the SWOT fast sampling phase (FSP) from 2023-03-30 to 2023-07-10.  


NOTES
- Wet path delay (WPD) is also referred to as zenith wet delay (ZWD) throughout the datasets and notebooks. 
- Contact Andrea Hay, andrea.hay@utas.edu.au for further information.


ACKNOWLEDGEMENTS
- This study was supported by Australia’s Integrated Marine Observing System (IMOS) Satellite Altimetry Calibration and Validation sub-Facility - IMOS is enabled by the National Collaborative Research Infrastructure Strategy (NCRIS). It is operated by a consortium of institutions as an incorporated joint venture, with the University of Tasmania as Lead Agent. 
- This research used the ACCESS-NRI’s model ACCESS-C infrastructure, which is enabled by the Australian Government’s National Collaborative Research Infrastructure Strategy (NCRIS). 


ADDITIONAL DATASETS
- SWOT Level 2 KaRIn Low Rate Sea Surface Height data (SWOT project, 2023) is openly available and distributed by PODAAC (https://podaac.jpl.nasa.gov/dataset/SWOT_L2_LR_SSH_Expert_2.0). 
- Sentinel-3A OLCI Level 1B RGB data from the Copernicus missions of the European Union is openly available and distributed by EUMETSAT (https://navigator.eumetsat.int/product/EO:EUM:DAT:0177). 
- The GNSS buoy data are openly available through the Australian Ocean Data Network (https://portal.aodn.org.au/). 


==============
DATA
==============

- Grids of hourly ACCESS-C ZWD values from each of four regions: Bass Strait, Albany, Carpentaria, and Davies reef:
	- ACCESS_ZWD_bst_20230330_20230710.nc
	- ACCESS_ZWD_alb_20230330_20230710.nc
	- ACCESS_ZWD_crp_20230330_20230710.nc
	- ACCESS_ZWD_dvr_20230330_20230710.nc

- ACCESS-C ZWD values interpolated to the SWOT grids during the FSP:
	- ACCESS_ZWD_alb_21_at_SWOT.nc
	- ACCESS_ZWD_alb_8_at_SWOT.nc
	- ACCESS_ZWD_bst_19_at_SWOT.nc
	- ACCESS_ZWD_bst_6_at_SWOT.nc
	- ACCESS_ZWD_crp_at_SWOT.nc
	- ACCESS_ZWD_dvr_at_SWOT.nc

- Hourly ACCESS-C ZWD values interpolated to the buoy locations during FSP:
	- ACCESS_at_buoys_FSP.nc

- Hourly GNSS ZWD values from the nine buoys
	- GNSS_hourly.nc

- ECMWF operational analysis from the SWOT product interpolated to the buoy locations during FSP:
	- ECMWF_at_buoys_FSP.nc

- Locations of GNSS buoys during FSP (WGS84 latitude and longitude, and UTM55 eastings and northings): 
	- buoy_locations_FSP_latlon.csv
	- buoy_locations_FSP_UTM.csv

- WPD data from ACCESS-C, GNSS and ECMWF from the SWOT product, reformatted for semivariogram analysis:
	- ACCESS_hourly_WPD.csv
	- buoy_hourly_WPD.csv
	- ECMWF_FSP_WPD.csv


==============
NOTEBOOKS
==============

- To calculate WPD from vapour and cloud liquid water components from the ACCESS-C model:
	- WPDliquid_ACCESS.ipynb
	- WPDvapour_ACCESS.ipynb
	- ZWD_functions.py

- To interpolate ACCESS-C ZWD values to buoy locations during FSP:
	- ACCESS_at_buoy_locations.ipynb

- To interpolate ACCESS-C ZWD values to the SWOT grids during FSP:
	- ACCESS_over_SWOT_regions.ipynb

- To interpolate ECMWF from the SWOT product to buoy locations during FSP:
	- ECMWF_at_buoy_locations.ipynb

- To reindex GNSS data to hourly intervals for comparison with ACCESS-C:
	- GNSS_hourly.ipynb

- To reformat data for semivariogram analysis:
	- Format_data_for_semivariogram.ipynb

- To calculate the model assessment results presented in section 3 of the manuscript:
	- GNSS_ACCESS_ECMWF_semivariogram.ipynb
	- GNSS_ACCESS_PSD_coherence.ipynb

- To calculate the SWOT comparison results presented in section 4 of the manuscript:
	- ACCESS_vs_SWOT.ipynb

- To calculate the radiometer comparison results in the approach to coast:
	- SWOT_comparisons_approach_to_coast.ipynb

