class rentals:
    def get_date_tuples(self,number,startdate,enddate):
        date_tuples = []
        for i in range(len(startdate.split())):
            date_tuples.append([startdate.split()[i],enddate.split()[i],int(enddate.split()[i])-int(startdate.split()[i])])
        return date_tuples
    def get_min_start(self, date_tuples):
        return min(date_tuples)
    def get_min_end(self, date_tuples):
        return min(date_tuples, key = lambda t: t[1])
    def get_min_time(self, date_tuples):
        return min(date_tuples, key = lambda t: t[2])
    def remove_old_appointments(self, date_tuples, current_time):
        to_delete = []
        for i in range(0,len(date_tuples)):
            if int(date_tuples[i][0]) <= int(current_time):
                to_delete.append(date_tuples[i])
        for j in to_delete:
            date_tuples.remove(j)
    def get_appointment(self, date_tuples):
        print self.get_min_start(date_tuples)
        return self.get_min_start(date_tuples)[1] 
    def get_number_cars(self,number,startdate,enddate):
        date_tuples = self.get_date_tuples(number,startdate,enddate)
        current_sales = 0
        current_time =0
        while len(date_tuples) > 0:
            current_time = self.get_appointment(date_tuples)
            current_sales += 1 
            self.remove_old_appointments(date_tuples,current_time)
        return current_sales
    

    #look at the smallest starting number and any other starting number that fits in to that range
    #then take the options that have the smallest end date. repeat 