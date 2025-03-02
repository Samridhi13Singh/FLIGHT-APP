import streamlit  as st
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as feature


cities ={
    'New York': [40.7128, -74.0059],
    'London': [51.5074, -0.1278],
    'Tokyo': [35.6895,139.6917],
    'Sydney': [-33.8688,151.2093],
    'Cape Town': [-33.9249,18.4241],
    'Rio de Janeiro': [-22.9068,-43.1729],
    'Paris' : [48.8566,2.3522 ],
    'Moscow' : [55.7558,37.6173],
    'Mumbai' : [ 19.0760,72.8777],
    'Queenstown':[-45.0312,168.6626]
}

st.title('Flight Path Between Ci✈️ies')

city_names=cities.keys()
city_names= list(city_names)

city1=st.selectbox('Select The Departure City: ',city_names)
city2=st.selectbox('Select The Arrival City: ',city_names)
if st.button("GENERATE"):
    if city1==city2:
        st.warning("Both The Destination Cannot Be Same... Please choose Another Destination")
    else:

        lat1,lon1 = cities[city1]
        lat2,lon2 =cities[city2]
        fig =plt.figure(figsize=(17,10))
        ax=fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())

        ax.set_extent([-180,180,-90,90],crs=ccrs.PlateCarree())

        ax.add_feature(feature.OCEAN,facecolor='lightblue',alpha=0.6)
        ax.add_feature(feature.LAND, facecolor='#95f3ac',alpha=0.7)
        ax.add_feature(feature.LAKES, facecolor='#a6e9f1',alpha=0.9)
        ax.add_feature(feature.RIVERS)
        ax.add_feature(feature.COASTLINE)
        ax.coastlines()
        for city,(lat,lon) in cities.items():
            ax.plot(lon,lat,color='red',marker='o',ms=5,transform=ccrs.PlateCarree())
            ax.text(lon+4,lat-4,city,color='brown',transform=ccrs.PlateCarree())

        ax.plot([lon1,lon2],[lat1,lat2],color='red',marker='o',transform=ccrs.Geodetic())
        plt.title(f'Flight Path Between {city1} and {city2}')

        st.pyplot(fig)
