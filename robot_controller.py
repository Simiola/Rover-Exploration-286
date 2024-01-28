from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
from controller import Camera


myRobot=Robot()
keyboard=Keyboard()
timestep=64


wheel1_left=myRobot.getDevice("wheel1_left")
wheel1_left.setPosition(float('inf'))
wheel1_left.setVelocity(0.0)

wheel1_right=myRobot.getDevice("wheel1_right")
wheel1_right.setPosition(float('inf'))
wheel1_right.setVelocity(0.0)


wheel2_left=myRobot.getDevice("wheel2_left")
wheel2_left.setPosition(float('inf'))
wheel2_left.setVelocity(0.0)

wheel2_right=myRobot.getDevice("wheel2_right")
wheel2_right.setPosition(float('inf'))
wheel2_right.setVelocity(0.0)


ds2=myRobot.getDevice("ds2")
ds2.enable(timestep)
ds1=myRobot.getDevice("ds1")
ds1.enable(timestep)

cam_slider=myRobot.getDevice("cam_slider")
cam=myRobot.getDevice("camera")
cam.enable(timestep)



speed=4
keyboard.enable(timestep)
autoMode=False
position=0
cam_slider_position=0
number_of_turns=0
img_num=1
prev_key=0
key_pressed=-1

while (myRobot.step(timestep) != -1):
    prev_key=key_pressed
    key_pressed=keyboard.getKey()
    ## print(key_pressed)
    print(autoMode)
    
    
    
    # 79is o key
    if(prev_key == -1 and key_pressed == 79):
        autoMode=not autoMode
        
     # 79is a key
    if (key_pressed == 315):
        cam_slider_position=cam_slider_position+0.01
        cam_slider_position.setPosition(cam_slider_position)
        
      #317 down_arrow key
    if (key_pressed == 317):
        cam_slider_position=cam_slider_position+0.01
        cam_slider_position.setPosition(cam_slider_position)
        
        
    if (prev_key == -1 and key_pressed == 80):
        cam.getImage()
        imag_name="img"+str(img_num)+".png"
        cam.saveImage(imag_name,200)
        img_num=img_num+1
        print("image captured:")
        
        
        
    if(autoMode):
        ds1_value=ds1.getValue()
        ds2_value=ds2.getValue()
        if(ds1_value<1000 or ds2_value<1000):
            number_of_turns=5
        
        if(number_of_turns>0):
            number_of_turns=number_of_turns-1
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
        else:
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
        

    if(not autoMode):   
    #83 means "s"
        if(key_pressed == 83):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            
        #87 means "W"
        if(key_pressed == 87):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(-speed)
            
        #65 means "a"
        if(key_pressed == 65):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
            
        #68 means "d"
        if(key_pressed == 68):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(-speed)
            
            
        if(key_pressed == -1):
            wheel1_left.setVelocity(0)
            wheel1_right.setVelocity(0)
            wheel2_left.setVelocity(0)
            wheel2_right.setVelocity(0)
        
        
# w means 87, a means 65, -1 means when u release the key, d means 68, s means 83