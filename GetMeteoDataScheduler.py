from bs4 import BeautifulSoup
from datetime import date, timedelta
from retry_requests import retry

import openmeteo_requests
import pandas as pd
import requests_cache
import re
import requests

today = date.today()

yesterday = today - timedelta(days = 1)
print("Requete des données météo pour le : ", yesterday)

DataFilePath = 'DATA/METEO/Donnees_meteo_Puylaurens.csv'
DataFilePathExpoSol = 'DATA/METEO/Tmp_ExpoSol.csv'
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 43.5722,
	"longitude": 2.0111,
	"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation", "pressure_msl", "cloud_cover", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
	"timezone": "auto",
	"start_date": yesterday,
	"end_date": yesterday
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(3).ValuesAsNumpy()
hourly_pressure_msl = hourly.Variables(4).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(5).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(6).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(7).ValuesAsNumpy()
hourly_wind_gusts_10m = hourly.Variables(8).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["dew_point_2m"] = hourly_dew_point_2m
hourly_data["precipitation"] = hourly_precipitation
hourly_data["pressure_msl"] = hourly_pressure_msl
hourly_data["cloud_cover"] = hourly_cloud_cover
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)

print('Load yesterday solar exposure')
ExpoSolYest=pd.read_csv(DataFilePathExpoSol)

print('Reformat of dataframe')
ReformatedDf= pd.DataFrame(columns=['year',
                                    'month',
                                    'day',
                                    'hours',
                                    'minute',
                                    'Températuce [°C]',
                                    'Point de Rosée [°C]',
                                    'Humidité [%]',
                                    'Vitesse vent [km/h]',
                                    'Direction vents [Pt Cardinaux]',
                                    'Direction vents [°]',
                                    'Vitesse Rafale [km/h]',
                                    'Pression [hPa]',
                                    'Exposition solaire [W/m²]',
                                    'Précipitation [mm]'])

for i in range(len(hourly_data["temperature_2m"] )):
	#Date
	year  = str(hourly_data["date"][i].year)
	month = str(hourly_data["date"][i].month)
	day   = str(hourly_data["date"][i].day)
	hour  = str(hourly_data["date"][i].hour)
	minute= str(0)

	#Température
	Température = str(round(float(hourly_data["temperature_2m"][i])*100)/100)
	PtRosee = str(round(float(hourly_data["dew_point_2m"][i])*100)/100)
	Humid = str(hourly_data["relative_humidity_2m"][i])

	#Vents
	V_vents = str(hourly_data["wind_speed_10m"][i])
	Card_vents = ''
	Dir_vents = str(hourly_data["wind_direction_10m"][i])
	Raf_vents = str(hourly_data["wind_gusts_10m"][i])
	
	#Pression
	Pression = str(hourly_data["pressure_msl"][i])
	
	#Expo solaire
	ExpoSol = str(0)
	for j in range(len(ExpoSolYest.Heure)):
		if int(hour) == int(ExpoSolYest.Heure[j]):
			ExpoSol = str(ExpoSolYest.SolarPower[j])
			break
	
	#Précipitation
	Precip = str(hourly_data["precipitation"][i])
	
	NewLigne = year + ';' + month + ';' + day + ';' + hour + ';' + minute + ';' + Température + ';' + PtRosee + ';' + Humid + ';' + V_vents + ';' + Card_vents + ';' + Dir_vents + ';' + Raf_vents + ';' + Pression + ';' + ExpoSol + ';' + Precip;
	
	with open(DataFilePath, 'a') as f:
		f.write(NewLigne)
		f.write('\n')
    
print('Get Solar exposure - today')

url_weather = "https://fr.tutiempo.net/radiation-solaire/puylaurens.html"
response = requests.get(url_weather)
HTML_content = BeautifulSoup(response.content, 'html.parser')
Content = HTML_content.text

start_point=Content.find("Aujourd'hui")
Content = Content[start_point:len(Content)]
end_point = [i.start() for i in re.finditer("Totale", Content)]
Content= Content[0:end_point[1]]

start_point = [i.start() for i in re.finditer(r"\d\d:\d\d", Content)]
end_point = [i.start() for i in re.finditer(" w/m2", Content)]

TableSolarPower = pd.DataFrame(columns=['Heure', 'SolarPower'])

for i in range(len(start_point)):
	Hour = int(Content[start_point[i]:start_point[i]+2])
	SolPow = int(Content[start_point[i]+5:end_point[i]])
	NvelleLigne = {"Heure": Hour,"SolarPower":SolPow}
	TableSolarPower = pd.concat([TableSolarPower, pd.DataFrame([NvelleLigne])], ignore_index=True)

TableSolarPower.to_csv(DataFilePathExpoSol,index=False)

print('execution success')
