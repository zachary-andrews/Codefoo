class light:
    def union(self, schedule: list) -> list:
        changes = True
        while changes:
            changes = False
            for hours in schedule:
                for hours2 in schedule:
                    if hours != hours2:
                        if hours[0] <= hours2[0] <= hours[1]:
                            if hours[0] <= hours2[1] <= hours[1]:
                                schedule.remove(hours2)
                                changes = True
                            else:
                                hours = ((hours[0],hours2[1]))
                                schedule.remove(hours2)
                                schedule.append((hours[0],hours2[1]))
                                changes = True
        return schedule

    def countem(self, schedule: list) -> int:
        count = 0
        for hours in schedule:
            count += abs(int(hours[1])-int(hours[0]))
        return count

    def get(self, schedule: list) -> int:
        schedule.sort(key=lambda tup: tup[0])
        new_schedule = self.union(schedule)
        
        return self.countem(new_schedule)