from connectify.connect import UnityConnection
from plotify.plot import Plotify
from geofy.geo import Geo
import time






if __name__ == "__main__":
    uc = UnityConnection()
    plotify = Plotify()
    geo = Geo()


    uc.establish_connection()
    dted_array = geo.readAsArray()
    #plotify.plot_contour_map(dted_array)

    while True:
        unity_data = uc.receive_data()
        plotify.find_x_y_position(unity_data,dted_array)

        time.sleep(0.5)