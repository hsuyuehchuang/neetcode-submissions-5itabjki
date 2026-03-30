class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=[]
        cars=[]
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        print(cars)
        for position, speed in cars:
            distance = target - position
            time = distance / speed
            if not res:
                res.append(time)
                continue
                
            elif res and time <= res[-1]:
                continue    
            else:
                res.append(time)
                
        return len(res)