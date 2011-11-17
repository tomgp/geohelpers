# quick and dirty testing
import osgb
import math
import unittest

#test radians to degrees conversion
assert osgb.radToDeg(math.pi) == 180, 'deg to rad not working'
assert osgb.radToDeg(math.pi * 2) == 360, 'deg to rad not working'

#test osgb to lat long note these often fail because of floating point precision, 
#need to add unittest so can do approximately equal to otherwise this is pretty useless
a = osgb.toLatLong(123456, 123456) 
assert a['lat'] == 50.944042 , 'lat conversion not accurate' + a
assert a['lon'] == -5.93824 , 'long conversion not accurate' + a

#shetlands can be tricky
a = osgb.toLatLong(439668, 1175316) 
assert a['lat'] == 60.459657 , 'lat conversion not accurate'
assert a['lon'] == -1.280628 , 'long conversion not accurate'

a = osgb.toLatLong(240000, 790000) 
assert a['lat'] == 56.973433 , 'lat conversion not accurate'
assert a['lon'] == -4.633887 , 'long conversion not accurate'