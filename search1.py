from pygeocoder import Geocoder
 
if __name__ == '__main__':
    address = 'Tamil Nadu, India, 600127'
    print(Geocoder.geocode(address)[0].coordinates)