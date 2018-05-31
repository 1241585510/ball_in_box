import math
import random
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    circles = []
    for circle_index in range(m):
        x1=[0.5,0.5,0.5]
        y1=[0.5,-0.5,0.3]
        i=0
        j=0
        k=0
        s=0.0
        x2 =[0.0,0.0,0.0,0.0]
        y2 =[0.0,0.0,0.0,0.0]
        x3 =[0.0 for x in range(0,5)]
        y3 =[0.0 for x in range(0,5)]
        x4 =[0.0 for x in range(0,5)]
        y4 =[0.0 for x in range(0,5)]
        n=[0 for x in range(0,5)]
        r=[0.0 for x in range(0,5)]
        d=[0.0 for x in range(0,16)]
        x3[0]=-1.0
        x3[4]=1.0
        y3[0]=-1.0
        y3[4]=1.0
        d1=[0.0 for x in range(0,16)]
        d2=[0.0 for x in range(0,16)]

        for i in range(0,3):    
	        for j in range(i+1,3):
		        x1[i]=min(x1[i],x1[j])
        for i in range(0,3):
	        for j in range(i+1,3):
		        y1[i]=min(y1[i],y1[j])


        for i in range(1,4):
	        x3[i]=x1[i-1]
        for i in range(1,4):
	        y3[i]=y1[i-1]

        for i in range(0,4):
	        x2[i]=x3[i+1]-x3[i]
        for i in range(0,4):
	        y2[i]=y3[i+1]-x3[i]

        for i in range(0,4):
	        for j in range(0,4):
		        d[4*i+j]=min(x2[i],y2[j])

        for i in range(0,16):
	        d1[i]=d[i]

        for i in range(0,16):
	        for j in range(i+1,16):
		        d[i]=max(d[i],d[j])

        for i in range(0,16):
	        if d[0]==d1[i]:
		        n[0]=i
		
        for i in range(0,16):
            if d[1]==d1[i]and i!=n[0]:
                n[1]=i

        for i in range(0,16):
            if d[2]==d1[i]and i!=n[0]and i!=n[1]:
                n[2]=i

        for i in range(0,16):
            if d[3]==d1[i]and i!=n[0]and i!=n[1]and i!=n[2]:
                n[3]=i
                                                                       
        for i in range(0,16):
            if d[4]==d1[i]and i!=n[0]and i!=n[1]and i!=n[2]and i!=n[3]:
                n[4]=i

        for i in range(0,5):
            x4[i]=(x3[n[i]//4+1]+x3[n[i]//4])/2
            y4[i]=(y3[n[i]%4+1]+y3[n[i]%4])/2
            r[i]=d[i]/2

 
     
        circles[circle_index] = (x4[circle_index], y4[circle_index], r[circle_index])
        circle_index += 1
    return circles
