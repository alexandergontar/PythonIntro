def snail(height, speed_down=1,speed_up=2):
    if speed_down==speed_up:
        print('Улитка никогда не заползет на столб')
        return None
    first_height = height
    day=0
    while(True):
        day+=1
        height-=speed_up
        if height<=0: return day
        height+=speed_down   
        if height>first_height:
            print('Улитка никогда не заползет на столб')
            return None

print(snail(12,1,1))
