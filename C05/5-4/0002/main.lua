local myMap = native.newMapView(0,0,320,480)
myMap:setCenter(35.681382, 139.766084)
for i=1, 10 do
	lat = 35.681382
	lon = math.random()* 5 + 135
	myMap:addMarker(lat, lon, {title="ABC", subtitle="DEF"})
end
