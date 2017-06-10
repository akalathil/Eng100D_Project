
import pandas as pd
import requests

##################################
#Load in the "cleaned" data #
##################################
df_communicable_diseases = pd.read_csv("../python/communicable_and infectious_diseases_(2011-14).csv")
df_injuries = pd.read_csv("../python/injury_data(2011-14).csv")
df_mental_health = pd.read_csv("../python/Mental_Health_Data(2011-14).csv")
df_nutrition = pd.read_csv("../python/Nutrition_Data(2011-14).csv")
df_oral_eye = pd.read_csv("../python/Oral_Eye_Health_Data(2011-14).csv")
df_tuberculosis = pd.read_csv("../python/Tuberculosis_Health_Data(2012-13).csv")
df_malaria = pd.read_csv("../python/Malaria_Health_Data(2013-14).csv")
df_water = pd.read_csv("../python/Water_Sanitation(2011).csv")
#test=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=Achham&key=AIzaSyAOTrmHFjUxiO8JUs8gqZReTxjFJ1W-9TY")
#print(test.json()['results'][0]['geometry']['location'])

# In[92]:

################################
# Drop unneeded attributes #
################################
del df_communicable_diseases["Zone"]
del df_communicable_diseases["Ecological Belt"]
del df_communicable_diseases["Development Region"]
del df_communicable_diseases["Year (BS)"]
del df_communicable_diseases["Indicator"]

del df_injuries["Zone"]
del df_injuries["Ecological Belt"]
del df_injuries["Development Region"]
del df_injuries["Year (BS)"]

del df_mental_health["Zone"]
del df_mental_health["Ecological Belt"]
del df_mental_health["Development Region"]
del df_mental_health["Year (BS)"]

del df_nutrition["Zone"]
del df_nutrition["Ecological Belt"]
del df_nutrition["Development Region"]
del df_nutrition["Year (BS)"]

del df_oral_eye["Zone"]
del df_oral_eye["Ecological Belt"]
del df_oral_eye["Development Region"]
del df_oral_eye["Year (BS)"]
del df_oral_eye["Indicator"]


del df_tuberculosis["Zone"]
del df_tuberculosis["Ecological Belt"]
del df_tuberculosis["Development Region"]
del df_tuberculosis["Year (BS)"]
del df_tuberculosis["Indicator"]
df_tuberculosis.columns = ["Name", "Year", "Sub-Indicator1", "Sub-Indicator2", "Sub-Indicator3", "Value"]
del df_tuberculosis["Sub-Indicator2"]
del df_tuberculosis["Sub-Indicator3"]

del df_malaria["Zone"]
del df_malaria["Ecological Belt"]
del df_malaria["Development Region"]
del df_malaria["Year (BS)"]
del df_malaria["Indicator"]

del df_water["Zone"]
del df_water["Geographical Region"]
del df_water["Development Region"]


df_communicable_diseases.columns = ["Name", "Year", "Indicator", "Value"]
df_injuries.columns = ["Name", "Year", "Indicator", "Value"]
df_mental_health.columns = ["Name", "Year", "Indicator", "Sub-Indicator", "Value"]
df_nutrition.columns = ["Name", "Year", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]
df_oral_eye.columns = ["Name", "Year", "Indicator", "Value"]
df_malaria.columns = ["Name", "Year", "Sub-Indicator1", "Sub-Indicator2", "Value"]
df_water.columns = ["Name", "Indicator", "Value"]
df_tuberculosis = df_tuberculosis.dropna()
df_mental_health.ix[df_mental_health["Sub-Indicator"] == "Dipression", "Sub-Indicator"] = "Depression"
df_water = df_water[df_water["Indicator"] == "Sanitation Coverage (%"]
df_water.ix[df_water["Indicator"] == "Sanitation Coverage (%", "Indicator"] = "Sanitation Coverage (%)"


# In[93]:

region_loc_dict ={}
disease_region_dict = {}
injury_region_dict = {}
oral_eye_disease_dict = {}
def region_lat_long_sort(row):
    loc_data={}
    if row["Name"] not in region_loc_dict.keys():
        req_loc=row["Name"].replace(" ","+")
        req=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+req_loc+"+,+Nepal"+"&key=AIzaSyDc8yRHl7AHRKdNK9_RJdg8Ndb56vQ5XnQ")        
        loc_data=req.json()['results'][0]['geometry']['location']
        region_loc_dict[row["Name"]] = loc_data

def region_sort(row, c_disease_region_dict, file_name):
    region_lat_long_sort(row)

df_communicable_diseases[["Name", "Year", "Indicator","Value"]].apply(lambda x: region_sort(x, disease_region_dict, "communicable_and infectious_diseases_(2011-14).csv"), axis=1)
df_injuries[["Name", "Year", "Indicator","Value"]].apply(lambda x: region_sort(x, injury_region_dict, "injury_data(2011-14).csv"), axis=1)
df_oral_eye[["Name","Year", "Indicator","Value"]].apply(lambda x: region_sort(x, oral_eye_disease_dict, "Oral_Eye_Health_Data(2011-14).csv"), axis=1)


# In[94]:

#Adding Mental Health Data
mental_health_region_dict = {}
def mental_region_sort(row, file_name):
    region_lat_long_sort(row)

df_mental_health[["Name", "Year", "Indicator", "Sub-Indicator", "Value"]].apply(lambda x: mental_region_sort(x, "Mental_Health_Data(2011-14).csv"), axis=1) 
df = df_mental_health.loc[df_mental_health["Indicator"] == "Mental Health related problems"]


# In[95]:

#Adding Nutrition Data
nutrition_region_dict = {}
def nutrition_region_sort(row, file_name): 
    region_lat_long_sort(row)

df_nutrition[["Name", "Year", "Indicator", "Sub-Indicator1", "Sub-Indicator2", "Value"]].apply(lambda x: nutrition_region_sort(x, "Nutrition_Data(2011-14).csv"), axis=1)
dfn = df_nutrition.loc[df_nutrition["Indicator"] == "Weighing Status according to age group (Repeated Visit)"]


# In[96]:

#Adding Water Sanitation Data
water_dict = {}


# In[97]:

def convert_list_to_dict(new_dict, old_list):
    for dic1 in old_list:
        value = dic1[list(dic1.keys())[0]]
        new_dict[list(dic1.keys())[0]] = value


# In[98]:

def demographic_indicators(dictionary):   
    key       = list(dictionary.keys())[0]
    frame     = dictionary[key]
    
    frame = frame.loc[frame["Year"] =="2013/14"]  
    frame.is_copy = False
    frame.reset_index(drop=True, inplace=True)
    
    districts  = frame["Name"]
    latitudes  = districts.apply(lambda d: region_loc_dict[d]["lat"])
    longitudes = districts.apply(lambda d: region_loc_dict[d]["lng"])
    
    frame["Latitude"]   = latitudes
    frame["Longtitude"] = longitudes
    
    del frame["Indicator"]
    headers       = frame.columns.values
    frame.columns = ["0", "1", "2", "Latitude", "Longitude"]
    
    return {key : {"Data": {"cols": list(headers) ,"rows":frame.to_json(orient="records")}} }


disease_frames          = df_communicable_diseases.groupby("Indicator")
disease_frames          = [{c : disease_frames.get_group(c)} for c in disease_frames.groups]
disease_region_list     = [demographic_indicators(d) for d in disease_frames]
disease_dict = {}
convert_list_to_dict(disease_dict, disease_region_list)

injury_frames           = df_injuries.groupby("Indicator")
injury_frames           = [{c : injury_frames.get_group(c)} for c in injury_frames.groups]
injury_list             = [demographic_indicators(d) for d in injury_frames]
injury_dict = {}
convert_list_to_dict(injury_dict, injury_list)

oral_eye_frames         = df_oral_eye.groupby("Indicator")
oral_eye_frames         = [{c : oral_eye_frames.get_group(c)} for c in oral_eye_frames.groups]
oral_eye_list           = [demographic_indicators(d) for d in oral_eye_frames]
oral_eye_dict = {}
convert_list_to_dict(oral_eye_dict, oral_eye_list)
oral_eye_dict


# In[99]:

def mental_indicators(dictionary):   
    key       = list(dictionary.keys())[0]
    frame     = dictionary[key]
    
    frame = frame.loc[frame["Year"] =="2013/14"]  
    frame.is_copy = False
    frame.reset_index(drop=True, inplace=True)
    
    districts  = frame["Name"]
    latitudes  = districts.apply(lambda d: region_loc_dict[d]["lat"])
    longitudes = districts.apply(lambda d: region_loc_dict[d]["lng"])
    
    frame["Latitude"]   = latitudes
    frame["Longtitude"] = longitudes
    
    del frame["Indicator"]
    del frame["Sub-Indicator"]
    headers       = frame.columns.values
    frame.columns = ["0", "1", "2", "Latitude", "Longitude"]
    
    return {key : {"Data": {"cols": list(headers) ,"rows":frame.to_json(orient="records")}}}

mental_frames           = df_mental_health.groupby("Sub-Indicator")
mental_frames           = [{c : mental_frames.get_group(c)} for c in mental_frames.groups]
mental_list             = [mental_indicators(d) for d in mental_frames]
mental_dict = {}
convert_list_to_dict(mental_dict, mental_list)
mental_dict


# In[100]:

def nutrition_indicators(d1, d2):   
    outer_key  = list(d1.keys())[0]
    inner_key  = list(d2.keys())[0]
    key        = outer_key + inner_key
    
    frame = d1[outer_key]
    frame = frame.loc[frame["Year"] =="2013/14"]  
    frame.is_copy = False
    frame.reset_index(drop=True, inplace=True)
    
    districts  = frame["Name"]
    latitudes  = districts.apply(lambda d: region_loc_dict[d]["lat"])
    longitudes = districts.apply(lambda d: region_loc_dict[d]["lng"])
    
    frame["Latitude"]   = latitudes
    frame["Longtitude"] = longitudes
    
    weight_frame = frame[frame["Sub-Indicator2"] == inner_key]
    weight_frame.is_copy = False
    weight_frame.reset_index(drop=True, inplace=True)
    
    del weight_frame["Indicator"]
    del weight_frame["Sub-Indicator1"]
    del weight_frame["Sub-Indicator2"]
    
    headers              = weight_frame.columns.values
    weight_frame.columns = ["0", "1", "2", "Latitude", "Longitude"]
    
    weight_map = { key : {"cols": list(headers), "rows": weight_frame.to_json(orient="records")} }
    
    return weight_map

nutrition_frames1           = dfn.groupby("Sub-Indicator1")
nutrition_frames2           = dfn.groupby("Sub-Indicator2")
nutrition_frames1           = [{c : nutrition_frames1.get_group(c)} for c in nutrition_frames1.groups]
nutrition_frames2           = [{c : nutrition_frames2.get_group(c)} for c in nutrition_frames2.groups]
nutrition_frames            = zip(nutrition_frames1, nutrition_frames2)
nutrition_list              = [nutrition_indicators(d,y) for d in nutrition_frames1 for y in nutrition_frames2]
nutrition_dict = {}
convert_list_to_dict(nutrition_dict, nutrition_list)
nutrition_dict


# In[101]:

def water_indicators(dictionary):   
    key       = list(dictionary.keys())[0]
    frame     = dictionary[key]

    frame.is_copy = False
    frame.reset_index(drop=True, inplace=True)
    loc_dict = {k.strip(' '): v for k, v in region_loc_dict.items()}

    districts  = frame["Name"]
    latitudes  = districts.apply(lambda d: loc_dict[d]["lat"])
    longitudes = districts.apply(lambda d: loc_dict[d]["lng"])
    
    frame["Latitude"]   = latitudes
    frame["Longtitude"] = longitudes
    
    del frame["Indicator"]
    headers       = frame.columns.values
    frame.columns = ["0", "1", "Latitude", "Longitude"]
    
    return {key : {"cols": list(headers) ,"rows":frame.to_json(orient="records")} }

df_water[["Name", "Indicator"]].apply(lambda x: region_lat_long_sort(x), axis=1)
water_frames           = df_water.groupby("Indicator")
water_frames           = [{c : water_frames.get_group(c)} for c in water_frames.groups]
water_list             = [water_indicators(d) for d in water_frames]
water_dict = {}
convert_list_to_dict(water_dict, water_list)
water_dict


# In[102]:

disease_region_dict


# In[103]:

injury_region_dict


# In[104]:

mental_health_region_dict


# In[105]:

nutrition_region_dict


# In[106]:

len(region_loc_dict)


# In[107]:

oral_eye_disease_dict


# In[108]:

water_dict


# In[109]:

import json
web_dict  = {
  "disease"         : disease_region_dict,
  "injury"          : injury_region_dict,
  "mental_health"   : mental_dict,
  "nutrition"       : nutrition_dict, 
  "oral_eye_health" : oral_eye_dict, 
  "water"           : water_dict  
}
with open ('data.json', 'w') as fp:
    json.dump(web_dict,fp)


# In[ ]:



