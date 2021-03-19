class two_city:
    def get_person_per_city(self, city_list:list) -> int:
        return int(len(city_list)/2)

    def get_cost(self, city_list:list) -> int:
        people_per_city = self.get_person_per_city(city_list)
        savings = []
        total = 0

        for n in city_list:
            savings.append(n[0]-n[1])
        
        bigsavings = (sorted(range(len(savings)), key=lambda i: savings[i])[-people_per_city:])
        
        for i,city in enumerate(city_list):
            if i in bigsavings:
                total += city[1]
            else:
                total += city[0]
                
        return total        
 