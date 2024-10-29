# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:15:38 2024

@author: Dhruv Singh
"""

import math

# Inputs
building_width = 8  # in meters
building_length = 28  # in meters
roof_angle = 22  # in degrees
pv_width = 1690  # in mm
pv_height = 1046  # in mm
pv_power = 400  # in Wp (Watts peak)

# Convert panel dimensions from mm to meters
pv_width_m = pv_width / 1000  # 1.69 meters
pv_height_m = pv_height / 1000  # 1.046 meters

# Calculate sloped width
sloped_width = building_width / math.cos(math.radians(roof_angle))

# Calculate roof area available for panels
roof_area = sloped_width * building_length  # Adjusted for slope
panel_area = pv_width_m * pv_height_m  # 1.76974 square meters

# Calculate maximum number of panels and total power
num_panels = int(roof_area // panel_area)  # Floor division to get whole panels
total_power_kWp = (num_panels * pv_power) / 1000  # Convert W to kW

# Output results
print("Number of panels:", num_panels)
print("Total power capacity:", total_power_kWp, "kWp")
