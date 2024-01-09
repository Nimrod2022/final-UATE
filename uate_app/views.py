from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
import json

def home(request):
    year_param = request.GET.get('year') 
    print(year_param)
    if year_param:
        baseurl = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23:Asylum%20decisions%20for%20Ukrainian%20applicants%20in%20Europe&maxFeatures=1000&outputFormat=application/json&CQL_FILTER=year=' + year_param
        baseurl2 = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23%3AAsylum%20applications%20for%20Ukrainians%20in%20Europe&maxFeatures=50&outputFormat=application%2Fjson&CQL_FILTER=year=' + year_param
        baseurl3 = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23%3AUkrainian%20asylum%20applications%20demographic%20breakdown%20in%20Europe&maxFeatures=1000&outputFormat=application%2Fjson&CQL_FILTER=year=' + year_param
    else:
        baseurl = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23:Asylum%20decisions%20for%20Ukrainian%20applicants%20in%20Europe&maxFeatures=1000&outputFormat=application/json&CQL_FILTER=year=2020'
        baseurl2 = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23%3AAsylum%20applications%20for%20Ukrainians%20in%20Europe&maxFeatures=50&outputFormat=application%2Fjson&CQL_FILTER=year=2020'
        baseurl3 = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23%3AUkrainian%20asylum%20applications%20demographic%20breakdown%20in%20Europe&maxFeatures=1000&outputFormat=application%2Fjson&CQL_FILTER=year=2020'

    # Disable SSL verification (not recommended in production)
    response = requests.get(baseurl, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
        # If the content is JSON, you can use response.json() to parse it
        # json_data = response.json()
    else:
        print(f"Error: {response.status_code}")
        
    response2 = requests.get(baseurl2, verify=False)
    if response2.status_code == 200:
        print('------------------response2------------------')
        print(response2.text)
    else:
        print(f"Error: {response2.status_code}")
        
    response3 = requests.get(baseurl3, verify=False)
    if response3.status_code == 200:
        print('------------------response3------------------')
        print(response3.text)
    else:
        print(f"Error: {response3.status_code}")
        
    
        
    
   
    
        
    def transform_json_to_array(json_data):
    # Extract the features from the JSON data
        features = json_data.get('features', [])

        # Create an array to store the transformed objects
        transformed_array = []

        # Loop through each feature and extract relevant information
        for feature in features:
            properties = feature.get('properties', {})
            geometry = feature.get('geometry', {}).get('coordinates', [])

            transformed_object = {
                'year': properties.get('year'),
                'coo_name': properties.get('coo_name'),
                'coa_name': properties.get('coa_name'),
                'procedure_type': properties.get('procedure_type'),
                'dec_level': properties.get('dec_level'),
                'dec_recognized': properties.get('dec_recognized'),
                'dec_other': properties.get('dec_other'),
                'dec_rejected': properties.get('dec_rejected'),
                'dec_closed': properties.get('dec_closed'),
                'dec_total': properties.get('dec_total'),
                'coordinates': geometry,
                'dec_level': properties.get('dec_level'),  # New property
                
            }

            # Add the transformed object to the array
            transformed_array.append(transformed_object)

        return transformed_array
    
    def transform_json2_to_array(json_data):
    # Extract the features from the JSON data
        features = json_data.get('features', [])

        # Create an array to store the transformed objects
        transformed_array = []

        # Loop through each feature and extract relevant information
        for feature in features:
            properties = feature.get('properties', {})
            geometry = feature.get('geometry', {}).get('coordinates', [])

            transformed_object = {
                'year': properties.get('year'),
                'coo_name': properties.get('coo_name'),
                'coa_name': properties.get('coa_name'),
                'app_type': properties.get('app_type'),  # New property
                'applied': properties.get('applied'),
                'coordinates': geometry,
            }

            # Add the transformed object to the array
            transformed_array.append(transformed_object)

        return transformed_array
    
    def transform_json3_to_array(json_data):
    # Extract the features from the JSON data
        features = json_data.get('features', [])

        # Create an array to store the transformed objects
        transformed_array = []

        # Loop through each feature and extract relevant information
        for feature in features:
            properties = feature.get('properties', {})
            geometry = feature.get('geometry', {}).get('coordinates', [])

            transformed_object = {
                'year': properties.get('year'),
                'coo_name': properties.get('coo_name'),
                'coa_name': properties.get('coa_name'),
                'm_total': properties.get('m_total'),
                'coordinates': geometry,
                'f_total': properties.get('f_total'),
                'm_0_11': properties.get('m_0_11'),
                'f_0_11': properties.get('f_0_11'),
                'm_12_17': properties.get('m_12_17'),
                'f_12_17': properties.get('f_12_17'),
                'm_above_18': properties.get('m_above_18'),
                'f_above_18': properties.get('f_above_18'),
           
            }

            # Add the transformed object to the array
            transformed_array.append(transformed_object)

        return transformed_array
    
    
    
    # print("-------------------------")
    # print(transform_json_to_array(response.json()))
    data = transform_json_to_array(response.json())
    data2 = transform_json2_to_array(response2.json())
    print('------------------data2------------------')
    print(data2)
    data3 = transform_json3_to_array(response3.json())
    print('------------------data3------------------')
    print(data3)
    
    applications_url = 'https://geoserver22s.zgis.at/geoserver/IPSDI_WT23/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IPSDI_WT23:Ukrainian%20asylum%20applications%20demographic%20breakdown%20in%20Europe&maxFeatures=10&outputFormat=application/json'
    applications_response = requests.get(applications_url, verify=False)
    if applications_response.status_code == 200:
        print(applications_response.text)
    else:
        print(f"Error: {applications_response.status_code}")
        
    # print("-------------applications------------")
    # print(transform_json_to_array(applications_response.json()))
    
    
    

    # Initialize empty lists to store formatted data
    
    
    def create_lookup(data_list):
        lookup = {}
        for item in data_list:
            key = (item['year'], item['coa_name'])
            lookup[key] = item
        return lookup
    
    data2_lookup = create_lookup(data2)
    data3_lookup = create_lookup(data3)
    formatted_coordinates_list = []
    coo_countries = set()
    coa_countries = set()

    # Loop through the data
    for entry in data:
        # Format coordinates
        key = (entry['year'], entry['coa_name'])
        entry_data2 = data2_lookup.get(key)
        entry_data3 = data3_lookup.get(key)
        
        formatted_coordinates = {
            'coords': {'lat': entry['coordinates'][1], 'lng': entry['coordinates'][0]},
            'content': entry['coa_name'],
            'card_data': {
                'year': entry['year'],
                'coo_name': entry['coo_name'],
                'coa_name': entry['coa_name'],
                'dec_other': entry['dec_other'],
                'dec_rejected': entry['dec_rejected'],
                'dec_closed': entry['dec_closed'],
                'dec_recognized': entry['dec_recognized'],
                'dec_total': entry['dec_total'],
                'dec_level': entry['dec_level'],
                'procedure_type': entry['procedure_type'],
                'applied': entry_data2.get('applied') if entry_data2 else None,
                'm_total': entry_data3.get('m_total') if entry_data3 else None,
                'f_total': entry_data3.get('f_total') if entry_data3 else None,
            }
        }
        formatted_coordinates_list.append(formatted_coordinates)

        # Add countries to sets
        coo_countries.add(entry['coo_name'])
        coa_countries.add(entry['coa_name'])

    # # Convert sets to lists
    # coo_countries_list = list(coo_countries)
    # coa_countries_list = list(coa_countries)

    # # Print or use the lists as needed
    # print("Formatted Coordinates List:", formatted_coordinates_list)
    # print("COO Countries List:", coo_countries_list)
    # print("COA Countries List:", coa_countries_list)

    
    
    context = {
        
        "all_data": data,
        "all_data2": data2,
        "all_data3": data3,
        "coordinates_list": formatted_coordinates_list,
        "coa_countries": coa_countries,
        "coo": coo_countries,
    }
    context['coordinates_list_json'] = json.dumps(formatted_coordinates_list)
    return render(request, 'home.html', context)
