import folium

world_map = folium.Map(location=[46.603354, 1.8883335], zoom_start=5)
folium.Marker([46.078637266899,  6.4111924884134]).add_to(world_map)
folium.Marker([48.636,  -1.5114]).add_to(world_map)
world_map.save("world.map.html")

