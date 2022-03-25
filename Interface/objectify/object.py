import numpy as np


scale = 108000/3600


class Object():
    def __init__(self,dted_array):
        self.dummy = None
        self.dted_data = dted_array
        self.interval = 5
        self.clipped_near_points= []



    def find_position(self, unity_data):
        self.x_pos = (int(unity_data.split(",")[0].split(".")[0])/(scale))
        self.y_pos = 3600-(int(unity_data.split(",")[3].split(".")[0])/(scale))
        self.height = int(unity_data.split(",")[2].split(".")[0])
        #self.z_pos = (int(unity_data.split(",")[1].split(".")[0])/scale)



        return self.x_pos, self.y_pos, self.height

    def find_nearly_heights(self,height):
        height = 3000-int(float(height))

        
        self.interval_x = height+self.interval
        self.interval_y = height-self.interval

        self.near_points=np.where(np.logical_and(self.interval_y<=self.dted_data,self.dted_data <=self.interval_x))


        #print(f"Yukseklik : {height}, Istenen araliktaki nokta sayisi : {len(self.near_points[0])}")
        


        return self.near_points

    def clip_nearly_heights(self):
        pass
    

        if abs(self.near_points[1]-self.y_pos)**2 + abs(self.near_points[0]-self.x_pos)**2 <=10000:
            return True


     




    