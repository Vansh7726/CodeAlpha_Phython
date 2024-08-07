import requests
import folium

def get_geolocation(ip_address):
    # Replace with a valid API key or URL for an IP geolocation service
    api_url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        loc = data.get('loc', '').split(',')
        latitude = float(loc[0]) if len(loc) > 0 else None
        longitude = float(loc[1]) if len(loc) > 1 else None

        return latitude, longitude
    except Exception as e:
        print(f"Error fetching geolocation data: {e}")
        return None, None

def create_map(latitude, longitude):
    if latitude is not None and longitude is not None:
        # Create a map centered around the given latitude and longitude
        location_map = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], tooltip='Your location').add_to(location_map)
        
        # Save the map to an HTML file
        location_map.save('map.html')
        print("Map has been saved to 'map.html'. Open this file in a web browser to view the map.")
    else:
        print("Invalid geolocation data.")

if __name__ == "__main__":
    ip_address = '8.8.8.8'  # Replace with the desired IP address or use 'your_ip' for your own IP
    latitude, longitude = get_geolocation(ip_address)
    create_map(latitude, longitude)
