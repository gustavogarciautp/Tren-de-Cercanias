from vpython import *
from tren2 import calculate

scene.width = 1300
scene.height = 600
scene.background = vec(1,1,1)
scene.range = 4.0
scene.center=vec(100,0,-2730-100)

#_______________________________________________TREN___________________________________________________________

height_cab=2
length_cab=0.03
      
cab1_der=extrusion(path=[vec(0,0,0),vec(0,0,-0.03)],color=color.green,
    shape=[shapes.rectangle(width=1, height=height_cab),shapes.rectangle(pos=[0,0.7],width=0.8,height=0.5)])

cab1_front=extrusion(path=[vec(-0.53,0,-1),vec(-0.5,0,-1)],color=color.green,
    shape=[shapes.rectangle(width=2, height=height_cab),shapes.rectangle(pos=[-0.3,0.7],width=0.7,height=0.5),shapes.rectangle(pos=[0.5,0.7],width=0.7,height=0.5)])

cab1_izq=cab1_der.clone (pos = vector (0,0,-2))

del_1 = cylinder(pos=vector(-0.53,-0.3,-1),axis=vector(-0.7,0,0), radius=0.7,color=color.yellow)
del_2 = del_1.clone(pos=vec(-1.23,-0.3,-1),color=color.blue,radius=0.7,axis=vec(-1,0,0))

luz_1 = cylinder(pos=vector(-2,0.45,-0.5),axis=vector(-0.22,0,0), radius=0.2,color=vec(0,0,0))
luz_2 = luz_1.clone(pos=vec(-2,0.45,-1.5))

luz_11 = cylinder(pos=vector(-2.22,0.45,-0.5),axis=vector(-0.01,0,0), radius=0.2,color=vec(1,1,1))
luz_21 = luz_11.clone(pos=vec(-2.22,0.45,-1.5))

rect = shapes.rectangle(width=0.05, height=0.07)
circpath = paths.circle(pos=vec(-2.25,0.45,-0.5),radius=0.2)
luz_111=extrusion(path=circpath,axis=vec(0,5,0), shape=rect, color=color.yellow)
luz_222=luz_111.clone(pos=vec(-2.25,0.45,-1.5))

front=box(pos=vec(-2.28,-1.2,-1),axis=vec(1,0,0),length=0.15, height=0.5, width=2.3,color=color.red)
tq_1 = cylinder(pos=vector(-2.3,-1.1,-0.5),axis=vector(-0.22,0,0), radius=0.09,color=vec(0,0,0))
tq_2 = tq_1.clone(pos=vec(-2.3,-1.1,-1.5))

tq_11 = cylinder(pos=vector(-2.5,-1.1,-0.5),axis=vector(-0.10,0,0), radius=0.13)
tq_22 = tq_11.clone(pos=vec(-2.5,-1.1,-1.5))

tq_3=cylinder(pos=vec(0.68,-1.1,-0.3),axis=vector(-0.08,0,0), radius=0.09,color=color.red)
tq_4=tq_3.clone(pos=vec(0.68,-1.1,-1.7))

group_tq_1=compound([tq_3,tq_4])
group_tq_2=group_tq_1.clone(pos=vec(1.47,-1.1,-1))
group_tq_3=group_tq_1.clone(pos=vec(5.54,-1.1,-1))
group_tq_4=group_tq_1.clone(pos=vec(5.97,-1.1,-1))
group_tq_5=group_tq_1.clone(pos=vec(10.04,-1.1,-1))
group_tq_6=group_tq_1.clone(pos=vec(10.47,-1.1,-1))
group_tq_7=group_tq_1.clone(pos=vec(14.54,-1.1,-1))
group_tq_8=group_tq_1.clone(pos=vec(14.97,-1.1,-1))
group_tq_9=group_tq_1.clone(pos=vec(19.04,-1.1,-1))

join_11=cylinder(pos=vec(1.6,-1.1,-0.3),axis=vector(-1.2,0,0), radius=0.06)
join_12=cylinder(pos=vec(1.6,-1.1,-1.7),axis=vector(-1.2,0,0), radius=0.06)
group_join_1=compound([join_11,join_12])

join_21=cylinder(pos=vec(6.5,-1.1,-0.3),axis=vector(-1.2,0,0), radius=0.06)
join_22=cylinder(pos=vec(6.5,-1.1,-1.7),axis=vector(-1.2,0,0), radius=0.06)
group_join_2=compound([join_21,join_22])
group_join_3=group_join_2.clone(pos=vec(10.4,-1.1,-1))
group_join_4=group_join_2.clone(pos=vec(14.8,-1.1,-1))

suelo_1=box(pos=vector(-0.8,-1.1,-1),axis=vec(0,0,-1),length=2, height=0.2, width=2.8)
star=extrusion(path=[vec(-2.2,-0.3,-1),vec(-2.3,-0.3,-1)],shape=shapes.star (n = 5,radius=0.5))
chim=cone(pos=vector(-1.6,1,-1),     axis=vector(0,-2,0),     radius=0.4,color=color.red)

rect_1 = shapes.rectangle(width=0.4, height=0.5)
circpath = paths.circle(pos=vec(-1.6,1.2,-1),radius=0.4)
tec_chim=extrusion(path=circpath, shape=rect_1, color=color.yellow)

rect_2 = shapes.rectangle(width=1, height=1.2)
arcpath = paths.arc(pos=vec(0,1.43,-0.52),angle1=0, angle2=pi,radius=0.5)
techo_cab_1=extrusion(path=arcpath,axis=vec(0,0,5),color=color.red,shape=rect_2)
techo_cab_1.rotate(angle=pi/2)

r1=cylinder (pos = vec (-1.5,-1.3,0), axis = vec (0,0,0.3), radius = 0.6)
r2=cylinder (pos = vec (-1.5,-1.3,0.3), axis = vec (0,0,0.05), radius = 0.57,color=vec(0.2,0.2,0.2))
r3=cylinder (pos = vec (-1.5,-1.3,0.35), axis = vec (0,0,0.1), radius = 0.2,color=color.red)
r4=cylinder (pos = vec (-1.5,-1.3,0.45), axis = vec (0,0,0.08), radius = 0.08,color=vec(0.3,0.3,0.3))

rueda_1 = compound([r1,r2,r3,r4])
rueda_2 =rueda_1.clone(pos=vec(0,-1.3,0.26))
rueda_3 =rueda_1.clone(pos=vec(-1.5,-1.3,-2.26),axis=vec(-5,0,0))
rueda_4 =rueda_3.clone(pos=vec(0,-1.3,-2.26))

group_rueda_0=compound([suelo_1,rueda_1,rueda_2,rueda_3,rueda_4])

locomotora=compound([cab1_front,cab1_der,cab1_izq,del_1,del_2,star,chim,tec_chim,
    techo_cab_1,group_rueda_0,luz_1,luz_2,luz_11,luz_21,luz_111,luz_222,
    front,tq_1,tq_2,group_tq_1,tq_11,tq_22,group_join_1])

suelo_2=suelo_1.clone(pos=vec(3.5,-1.1,-1),width=4)
rueda_5=rueda_1.clone(pos=vec(2.5,-1.3,0.26))
rueda_6=rueda_1.clone(pos=vec(4.5,-1.3,0.26))
rueda_7=rueda_3.clone(pos=vec(2.5,-1.3,-2.26))
rueda_8=rueda_3.clone(pos=vec(4.5,-1.3,-2.26))

group_rueda_1=compound([suelo_2,rueda_5,rueda_6,rueda_7,rueda_8])
group_rueda_2=group_rueda_1.clone(pos=vec(8,-1.3,-1))

cab2_der_1=box(pos=vec(2.9,0,0),axis=vec(0,0,1),length=length_cab, height=height_cab, width=suelo_2.width*0.7,color=color.yellow)
cab2_izq_1=box(pos=vec(2.9,0,-2),axis=vec(0,0,1),length=length_cab, height=height_cab, width=suelo_2.width*0.7,color=color.yellow)
cab2_front=box(pos=vec(1.51,0,-1),axis=vec(1,0,0),length=length_cab, height=height_cab, width=2,color=color.yellow)
cab2_der_2=box(pos=vec(4.9,-0.26,0),axis=vec(0,0,1),length=length_cab, height=1.5, width=suelo_2.width*0.3,color=color.yellow)
cab2_izq_2=box(pos=vec(4.9,-0.26,-2),axis=vec(0,0,1),length=length_cab, height=1.5, width=suelo_2.width*0.3,color=color.yellow)
cab2_diag_der=box(pos=vec(4.4,0.55,0),axis=vec(0,0,1),length=length_cab, height=0.8, width=0.5,color=color.yellow)
cab2_diag_der.rotate(angle=45*pi/180)
cab2_diag_izq=box(pos=vec(4.4,0.55,-2),axis=vec(0,0,1),length=length_cab, height=0.8, width=0.5,color=color.yellow)
cab2_diag_izq.rotate(angle=45*pi/180)

rect_3 = shapes.rectangle(width=1, height=2.8)
arcpath = paths.arc(pos=vec(2.9,1.43,-0.52),angle1=0, angle2=pi,radius=0.5)
techo_cab_2=extrusion(path=arcpath,axis=vec(0,0,5),color=color.red,shape=rect_3)
techo_cab_2.rotate(angle=pi/2)

cab2_trasero=box(pos=vec(5.49,-0.26,-1),axis=vec(1,0,0),length=length_cab, height=1.5, width=2,color=color.yellow)

cabina2=compound([cab2_der_1,cab2_der_2,cab2_izq_1,cab2_izq_2,cab2_front,cab2_diag_der,cab2_diag_izq,techo_cab_2,group_rueda_1,
    group_tq_2,group_tq_3,group_join_2,cab2_trasero])

cab3_der=extrusion(path=[vec(8,0,0),vec(8,0,-0.03)],color=color.green,
    shape=[shapes.rectangle(width=4, height=height_cab,),shapes.rectangle(pos=[-1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[-0.9,0.1],width=0.6,height=0.76),shapes.rectangle(pos=[0,-0.2],width=0.7,height=1.5),
        shapes.rectangle(pos=[1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[0.9,0.1],width=0.6,height=0.76)])
        
cab3_izq=cab3_der.clone(pos=vec(8,0,-2))
cab3_front=cab2_front.clone(pos=vec(6,0,-1),color=color.green)
cab3_trasero=cab3_front.clone(pos=vec(10,0,-1))

rect_4 = shapes.rectangle(width=1, height=4)
arcpath = paths.arc(pos=vec(8,1.43,-0.52),angle1=0, angle2=pi,radius=0.5)
techo_cab_3=extrusion(path=arcpath,axis=vec(0,0,5),color=color.red,shape=rect_4)
techo_cab_3.rotate(angle=pi/2)

cabina3=compound([cab3_front,cab3_der,cab3_izq,techo_cab_3,group_rueda_2,cab3_trasero,group_tq_4,group_tq_5,group_join_3])

cab4_der=extrusion(path=[vec(8,0,0),vec(8,0,-0.03)],color=color.blue,
    shape=[shapes.rectangle(width=4, height=height_cab,),shapes.rectangle(pos=[-1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[-0.9,0.1],width=0.6,height=0.76),shapes.rectangle(pos=[0,-0.2],width=0.7,height=1.5),
        shapes.rectangle(pos=[1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[0.9,0.1],width=0.6,height=0.76)])
        
cab4_izq=cab4_der.clone(pos=vec(8,0,-2))
cab4_front=cab3_front.clone(color=color.blue)
cab4_trasero=cab3_trasero.clone(color=color.blue)

cabina4_aux=compound([cab4_front,cab4_der,cab4_izq,techo_cab_3,group_rueda_2,cab4_trasero])
cabina4_aux.pos=vec(12.5,0,-1)

cabina4=compound([cabina4_aux,group_tq_6,group_tq_7,group_join_4])

cab5_der=extrusion(path=[vec(8,0,0),vec(8,0,-0.03)],color=color.magenta,
    shape=[shapes.rectangle(width=4, height=height_cab,),shapes.rectangle(pos=[-1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[-0.9,0.1],width=0.6,height=0.76),shapes.rectangle(pos=[0,-0.2],width=0.7,height=1.5),
        shapes.rectangle(pos=[1.6,0.1],width=0.6,height=0.76),
        shapes.rectangle(pos=[0.9,0.1],width=0.6,height=0.76)])
        
cab5_izq=cab5_der.clone(pos=vec(8,0,-2))
cab5_front=cab3_front.clone(color=color.magenta)
cab5_trasero=cab3_trasero.clone(color=color.magenta)
cabina5_aux=compound([cab5_front,cab5_der,cab5_izq,techo_cab_3,group_rueda_2,cab5_trasero])
cabina5_aux.pos=vec(17,0,-1)

cabina5=compound([cabina5_aux,group_tq_8,group_tq_9])

#______________________________________________________CARRETETA_______________________________________________
alt=-1.95
rad=100
d1=2730 
d2=2730
d3=2730

tren=[locomotora,cabina2,cabina3,cabina4,cabina5]
for e in tren:
    e.rotate(angle=pi,axis=vec(0,1,0),origin=vector(-5,0,0))
    e.pos.x-=(d1-30)
    e.pos.z=0
    e.pos.y+=0.17

rect =shapes.rectangle(width=5,height=0.1)

tramo1 = extrusion(path=[vec(-d1,alt,0), vec(0.5,alt,0)],shape=rect)

arcpath1 = paths.arc(angle1=3*pi/2, angle2=2*pi,radius=rad,np=128)
giro1=extrusion(path=arcpath1, shape=rect)
giro1.pos.y=alt
giro1.pos.z=giro1.pos.z-rad

tramo2 = extrusion(path=[vec(rad,alt,-rad+0.5), vec(rad,alt,-rad-d2-0.5)],shape=rect)

arcpath2 = paths.arc(angle1=pi/2, angle2=pi,radius=rad,np=128)
giro2=extrusion(path=arcpath2, shape=rect)
giro2.pos=vec(giro2.pos.x+2*rad,alt,giro2.pos.z-d2-rad)

tramo3 = extrusion(path=[vec(2*rad-0.5,alt,-rad*2-d2), vec(2*rad+d3+0.5,alt,-rad*2-d2)],shape=rect)

arcpath3 = paths.arc(angle1=0, angle2=pi/2,radius=rad,np=128)
giro3=extrusion(path=arcpath3, shape=rect)
giro3.pos=vec(giro3.pos.x+2*rad+d3,alt,giro2.pos.z)

tramo4 = tramo2.clone(pos=vec(3*rad+d3,alt,tramo2.pos.z))

arcpath4 = paths.arc(angle1=pi, angle2=3*pi/2,radius=rad,np=128)
giro4=extrusion(path=arcpath4, shape=rect)
giro4.pos=vec(giro4.pos.x+4*rad+d3,alt,giro1.pos.z)

tramo5 = extrusion(path=[vec(4*rad+d3-0.5,alt,0), vec(4*rad+d3+d1-0.5,alt,0)],shape=rect)

carretera=compound([tramo1,giro1,tramo2,giro2,tramo3,giro3,tramo4,giro4,tramo5])

#-------------------------------------------Rieles-----------------------------------------
riel_group_1=[]
riel_group_2=[]
riel_group_3=[]
riel_group_4=[]
riel_group_5=[]
riel_group_6=[]

i=0
while(i<d1):
    b=box(pos=vector(-i,alt+0.135,0), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    riel_group_2.append(b)
    i+=1

rect_r =shapes.rectangle(width=0.17,height=0.2)

riel_1 = extrusion(path=[vec(-d1,alt+0.3,-1.4), vec(0,alt+0.3,-1.4)],shape=rect_r,color=vec(141/255, 73/255, 37/255))
riel_12 = riel_1.clone()
riel_12.pos.z=1.4

riel_group_1.append(riel_1)
riel_group_1.append(riel_12)

arcpath_r= paths.arc(angle1=3*pi/2, angle2=2*pi,radius=rad-1.4,np=128)
giro_r1=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r1.pos.y=alt+0.3
giro_r1.pos.z=giro1.pos.z-1.87

arcpath_r= paths.arc(angle1=3*pi/2, angle2=2*pi,radius=rad+1.4,np=128)
giro_r12=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r12.pos.y=alt+0.3
giro_r12.pos.z=giro1.pos.z-0.47

riel_group_1.append(giro_r1)
riel_group_1.append(giro_r12)

riel_2 = extrusion(path=[vec(rad-1.4,alt+0.3,-rad), vec(rad-1.4,alt+0.3,-rad-d2)],shape=rect_r,color=vec(141/255, 73/255, 37/255))
riel_21 = riel_2.clone()
riel_21.pos.x=rad+1.4

riel_group_1.append(riel_2)
riel_group_1.append(riel_21)

arcpath_r= paths.arc(angle1=pi, angle2=pi/2,radius=rad+1.4,np=128)
giro_r2=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r2.pos=vec(giro_r2.pos.x+2*rad,alt+0.3,giro_r2.pos.z-rad-d2)

arcpath_r= paths.arc(angle1=pi, angle2=pi/2,radius=rad-1.4,np=128)
giro_r21=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r21.pos=vec(giro_r21.pos.x+2*rad,alt+0.3,giro_r21.pos.z-rad-d2)

riel_group_1.append(giro_r2)
riel_group_1.append(giro_r21)

riel_3 = extrusion(path=[vec(2*rad,alt+0.3,-2*rad-d2-1.4), vec(2*rad+d3,alt+0.3,-2*rad-d2-1.4)],shape=rect_r,color=vec(141/255, 73/255, 37/255))
riel_32 = riel_3.clone()
riel_32.pos.z=-2*rad-d2+1.4

riel_group_1.append(riel_3)
riel_group_1.append(riel_32)

arcpath_r= paths.arc(angle1=pi/2, angle2=0,radius=rad+1.4,np=128)
giro_r3=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r3.pos=vec(giro_r3.pos.x+2*rad+d3,alt+0.3,giro_r2.pos.z)

arcpath_r= paths.arc(angle1=pi/2, angle2=0,radius=rad-1.4,np=128)
giro_r31=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r31.pos=vec(giro_r31.pos.x+2*rad+d3,alt+0.3,giro_r21.pos.z)

riel_group_1.append(giro_r3)
riel_group_1.append(giro_r31)

riel_4 = extrusion(path=[vec(3*rad+d3-1.4,alt+0.3,-rad-d2), vec(3*rad+d3-1.4,alt+0.3,-rad)],shape=rect_r,color=vec(141/255, 73/255, 37/255))
riel_42 = riel_4.clone()
riel_42.pos.x=3*rad+d3+1.4

riel_group_1.append(riel_4)
riel_group_1.append(riel_42)

arcpath_r= paths.arc(angle1=pi, angle2=3*pi/2,radius=rad+1.4,np=128)
giro_r4=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r4.pos=vec(giro_r4.pos.x+4*rad+d3,alt+0.3,giro_r12.pos.z)

arcpath_r= paths.arc(angle1=pi, angle2=3*pi/2,radius=rad-1.4,np=128)
giro_r41=extrusion(path=arcpath_r, shape=rect_r,color=vec(141/255, 73/255, 37/255))
giro_r41.pos=vec(giro_r41.pos.x+4*rad+d3,alt+0.3,giro_r1.pos.z)

riel_group_1.append(giro_r4)
riel_group_1.append(giro_r41)

riel_5 = extrusion(path=[vec(4*rad+d3,alt+0.3,-1.4), vec(4*rad+d3+d1,alt+0.3,riel_1.pos.z)],shape=rect_r,color=vec(141/255, 73/255, 37/255))
riel_52 = riel_5.clone()
riel_52.pos.z=riel_12.pos.z

riel_group_1.append(riel_5)
riel_group_1.append(riel_52)

s=rad*pi/2
ds=0.95
theta1=0
theta3=0
x=0
z=0
while(ds<=s):
    a=box(pos=vec(x,alt+0.135,z), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    theta1=asin(x/rad)
    a.rotate(angle=theta1,axis=vec(0,1,0))
    theta3=ds/rad
    x=rad*sin(theta3)
    z=rad*cos(theta3)-rad
    ds+=0.95
    riel_group_1.append(a)
    
i=0
while(-rad-i>-d2-rad):
    a=box(pos=vector(0,alt+0.135,0), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    a.rotate(angle=pi/2,axis=vec(0,1,0))
    a.pos.x=rad
    a.pos.z=-rad-i
    i+=1
    riel_group_3.append(a)
   
theta1=0
theta3=0
ds=0
x=rad
z=-rad-d2
while(ds<=s):
    a=box(pos=vec(x,alt+0.135,z), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    theta1=asin((z+rad+d2)/rad)
    a.rotate(angle=theta1+pi/2,axis=vec(0,1,0))
    theta3=ds/rad
    x=(-rad*cos(theta3)+rad)+rad
    z=-(rad*sin(theta3))-rad-d2
    ds+=0.95
    riel_group_1.append(a)
    
i=0
while(rad*2+i<d3+2*rad):
    a=box(pos=vector(0,alt+0.135,0), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    a.pos.x=rad*2+i
    a.pos.z=-rad*2-d2
    i+=1
    riel_group_4.append(a)
    
theta1=0
theta2=0
theta3=0
ds=0
x=2*rad+d3
z=-rad*2-d2
while(ds<=s):   
    a=box(pos=vec(x,alt+0.135,z), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    theta1=-asin((x-2*rad-d3)/rad)
    a.rotate(angle=theta1,axis=vec(0,1,0))
    theta3=ds/rad
    x=(rad*sin(theta3))+d3+2*rad
    z=(-rad*cos(theta3)+rad)-2*rad-d2
    ds+=0.95
    riel_group_1.append(a)
    
i=0
while(-rad-d2+i<-rad):
    a=box(pos=vector(0,alt+0.135,0), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    a.rotate(angle=-pi/2,axis=vec(0,1,0))
    a.pos.z=-rad-d2+i
    a.pos.x=rad*3+d3
    i+=1
    riel_group_5.append(a)

theta1=0
theta3=0
ds=0
x=3*rad+d3
z=-rad
while(ds<=s):   
    a=box(pos=vec(x,alt+0.135,z), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    theta1=asin((z+rad)/rad)
    a.rotate(angle=theta1-pi/2,axis=vec(0,1,0))
    theta3=ds/rad
    x=-(rad*cos(theta3)-rad)+d3+3*rad
    z=(rad*sin(theta3))-rad
    ds+=0.95
    riel_group_1.append(a)
    
i=0
while(rad*4+d3+i<rad*4+d3+d1):
    box(pos=vector(rad*4+d3+i,alt+0.135,0), axis=vec(0,0,-1),length=5, height=0.17, width=0.2,color=vec(141/255, 73/255, 37/255))
    i+=1
    riel_group_6.append(a)

riel_compound_1=compound(riel_group_1)
riel_compound_2=compound(riel_group_2)
riel_compound_3=compound(riel_group_3)
riel_compound_4=compound(riel_group_4)
riel_compound_5=compound(riel_group_5)
riel_compound_6=compound(riel_group_6)
#__________________________________________Estaciones de tren_____________________________-
st_der= box(pos=vec(-110+7,4,-4-7), axis=vec(0,0,-1),length=14, height=10, width=0.2,color=color.green)
st_izq= box(pos=vec(-110-7,4,-4-7), axis=vec(0,0,-1),length=14, height=10, width=0.2,color=color.green)
st_del=extrusion(path=[vec(-110,4,-4),vec(-110,4,-4.2)],color=color.green,
    shape=[shapes.rectangle(width=14, height=10),shapes.rectangle(pos=[-4,2.5],width=2,height=1.5),
    shapes.rectangle(pos=[0,2.5],width=2,height=1.5),shapes.rectangle(pos=[4,2.5],width=2,height=1.5),
    shapes.rectangle(pos=[0,-3.49],width=2,height=3)])
st_tras= box(pos=vec(-110,4,-4-14+0.1), axis=vec(1,0,0),length=14, height=10, width=0.2,color=color.green)
st_piso=box(pos=vec(-110,-1+0.1,-4-7), axis=vec(0,1,0),length=0.2, height=14, width=14,color=color.green)


rect_st =shapes.trapezoid(pos=[0,0], width=18, height=3)
tec_st=extrusion(path=[vec(0,0,0),vec(0,0,14)], shape=rect_st, color=color.yellow)
tec_st.pos=vec(-110,9+1.5,-4-7)

rect_st_2 =shapes.trapezoid(pos=[0,0], width=26, height=1,top=24)
tec_st_2=extrusion(path=[vec(0,0,0),vec(0,0,4)], shape=rect_st_2, color=color.yellow)
tec_st_2.pos=vec(-110,4,-2)

viga_1=cylinder(pos=vector(-120,-1,-2),axis=vector(0,4.5,0), radius=0.5,color=color.red)
viga_2=viga_1.clone(pos=vec(viga_1.pos.x+5,-1,-2))
viga_3=viga_2.clone(pos=vec(viga_2.pos.x+5,-1,-2))
viga_4=viga_3.clone(pos=vec(viga_3.pos.x+5,-1,-2))
viga_5=viga_4.clone(pos=vec(viga_4.pos.x+5,-1,-2))

station_1=compound([st_der,st_izq,st_del,st_tras,st_tras,st_piso,tec_st,tec_st_2,viga_1,viga_2,viga_3,viga_4,viga_5])
station_1.pos=vec(rad+2.5+station_1.width/2,-2+station_1.height/2,-rad-d2/2)
station_1.rotate(angle=-pi/2,axis=vec(0,1,0))

station_2=station_1.clone()
station_2.rotate(angle=pi/2,axis=vec(0,1,0))
station_2.pos.x=2*rad+d3/2
station_2.pos.z=-2*rad-d2-2.5-station_2.width/2

station_3=station_1.clone()
station_3.rotate(angle=pi,axis=vec(0,1,0))
station_3.pos.x=3*rad+d3-2.5-station_2.width/2

plataforma=box(pos=vec(1400,-9,-1500), axis=vec(0,-1,0),length=14, height=9000, width=4000,texture={'file':textures.stucco, 
               'bumpmap':bumpmaps.stucco})

scene.camera.follow(cabina2)

a=0
curva=0
estacion=0
theta2=0
s=rad*pi/2

class vagon():
    def __init__(self,obj):
        self.obj=obj
        self.vel=0
        self.theta1=0
        self.theta3=0
        self.ds=0
        self.id=1

    def movimiento(self):
        global a
        global curva
        global estacion
        if self.obj.pos.x<0:
            if self.id==0:
                curva=(d1+self.obj.pos.x)/d1
                estacion=0
            if a==0:
                self.obj.pos.x+=self.vel
            else:
                self.obj.pos.x+=rad*sin(self.vel/rad)
        if (self.obj.pos.x>=0 and self.obj.pos.x<rad):
            if (self.ds==0 and self.obj.pos.x!=0):
                t=asin(self.obj.pos.x/rad)
                self.ds=rad*t
            if self.ds<=s:
                if self.id==0 and a==0:
                    a=1
                self.theta3=self.ds/rad
                self.obj.pos.x=rad*sin(self.theta3)
                self.obj.pos.z=rad*cos(self.theta3)-rad
                theta2=self.theta1
                self.theta1=asin(self.obj.pos.x/rad)
                self.obj.rotate(angle=self.theta1-theta2,axis=vec(0,1,0))
                if a==1:
                    self.ds+=self.vel
                else:
                    self.ds=rad*acos((self.obj.pos.z+rad-self.vel)/rad)
            else:
                self.obj.pos.x=rad
                self.obj.pos.z=rad*cos(self.ds/rad)-rad
                self.obj.rotate(angle=(pi/2)-self.theta1,axis=vec(0,1,0))
                self.ds=0
                self.theta1=0
        else:
            if(self.obj.pos.x==rad and self.obj.pos.z>-rad-d2):
                if self.id==0:
                    curva=(self.obj.pos.z+rad)/(-d2)
                    if self.obj.pos.z<(-rad-(d2/2)-11): 
                        if estacion!=0:
                            estacion=0
                    else:
                        estacion=(self.obj.pos.z+rad)/(-(d2/2)-11)
                if a==1 and self.id==0:
                    a=2
                if a==2:
                    self.obj.pos.z-=self.vel
                else:
                    self.obj.pos.z-=(rad*sin(self.vel/rad))            
            if (self.obj.pos.x>=rad and self.obj.pos.x<2*rad and self.obj.pos.z<=-rad-d2):
                if (self.ds==0 and self.obj.pos.z!=-rad-d2):
                    t=-asin((self.obj.pos.z+rad+d2)/rad)
                    self.ds=rad*t
                if self.ds<=s:
                    if self.id==0 and a==2:
                        a=3
                    self.theta3=self.ds/rad
                    self.obj.pos.x=(-rad*cos(self.theta3)+rad)+rad
                    self.obj.pos.z=-(rad*sin(self.theta3))-rad-d2
                    theta2=self.theta1
                    self.theta1=asin((self.obj.pos.z+rad+d2)/rad)
                    self.obj.rotate(angle=self.theta1-theta2,axis=vec(0,1,0))
                    if a==3:
                        self.ds+=self.vel
                    else:
                        self.ds=rad*acos((-(self.obj.pos.x+self.vel)+2*rad)/rad)
                else:
                    self.obj.pos.x=(-rad*cos(self.ds/rad)+rad)+rad
                    self.obj.pos.z=-2*rad-d2
                    self.obj.rotate(angle=-(pi/2)-self.theta1,axis=vec(0,1,0))
                    self.ds=0
                    self.theta1=0
            else:
                if (self.obj.pos.x>=2*rad and self.obj.pos.x<2*rad+d3):
                    if self.id==0:
                        curva=(self.obj.pos.x-2*rad)/d3
                        if self.obj.pos.x>(2*rad+(d3/2)+11): 
                            if estacion!=0:
                                estacion=0
                        else:
                            estacion=(self.obj.pos.x-2*rad)/((d3/2)+11)

                    if self.id==0 and a==3:
                        a=4
                    if a==4:
                        self.obj.pos.x+=self.vel
                    else:
                        self.obj.pos.x+=(rad*sin(self.vel/rad))
                if (self.obj.pos.x>=2*rad+d3 and self.obj.pos.x<3*rad+d3):
                    if (self.ds==0 and self.obj.pos.x!=2*rad+d3):
                        t=asin((self.obj.pos.x-2*rad-d3)/rad)
                        self.ds=rad*t                   
                    if self.ds<=s:
                        if self.id==0 and a==4:
                            a=5
                        self.theta3=self.ds/rad
                        self.obj.pos.x=(rad*sin(self.theta3))+d3+2*rad
                        self.obj.pos.z=(-rad*cos(self.theta3)+rad)-2*rad-d2
                        theta2=self.theta1
                        self.theta1=-asin((self.obj.pos.x-2*rad-d3)/rad)
                        self.obj.rotate(angle=self.theta1-theta2,axis=vec(0,1,0))
                        if a==5:
                            self.ds+=self.vel
                        else:
                            self.ds=rad*acos(-(self.obj.pos.z+self.vel+d2+rad)/rad)
                    else:
                        self.obj.pos.x=3*rad+d3
                        self.obj.pos.z=(-rad*cos(self.ds/rad)+rad)-2*rad-d2
                        self.obj.rotate(angle=-(pi/2)-self.theta1,axis=vec(0,1,0))
                        self.ds=0
                        self.theta1=0
                else:
                    if (self.obj.pos.x==3*rad+d3 and self.obj.pos.z<-rad):
                        if self.id==0:
                            curva=(self.obj.pos.z+rad+d2)/d2
                            if self.obj.pos.z>(-rad-(d2/2)+11): 
                                if estacion!=0:
                                    estacion=0
                            else:
                                estacion=(self.obj.pos.z+rad+d2)/((d2/2)+11)
                        if self.id==0 and a==5:
                            a=6
                        if a==6:
                            self.obj.pos.z+=self.vel
                        else:
                            self.obj.pos.z+=(rad*sin(self.vel/rad))
                    if (self.obj.pos.x>=3*rad+d3 and self.obj.pos.x<4*rad+d3 and self.obj.pos.z>=-rad):
                        if (self.ds==0 and self.obj.pos.z!=-rad):
                            t=asin((self.obj.pos.z+rad)/rad)
                            self.ds=rad*t
                        if self.ds<=s:
                            if self.id==0 and a==6:
                                a=7
                            self.theta3=self.ds/rad
                            self.obj.pos.x=-(rad*cos(self.theta3)-rad)+d3+3*rad
                            self.obj.pos.z=(rad*sin(self.theta3))-rad
                            theta2=self.theta1
                            self.theta1=asin((self.obj.pos.z+rad)/rad)
                            self.obj.rotate(angle=self.theta1-theta2,axis=vec(0,1,0))
                            if a==7:
                                self.ds+=self.vel
                            else:
                                self.ds=rad*acos(-(self.obj.pos.x+self.vel-4*rad-d3)/rad)
                        else:
                            self.obj.pos.x=-(rad*cos(self.ds/rad)-rad)+d3+3*rad
                            self.obj.pos.z=0
                            self.obj.rotate(angle=(pi/2)-self.theta1,axis=vec(0,1,0))
                            self.ds=0
                            self.theta1=0
                    else:
                        if (self.obj.pos.x>=4*rad+d3 and self.obj.pos.x<4*rad+d3+d1):
                            if self.id==0 and a==7:
                                a=8
                                curva=0
                            if a==8:
                                self.obj.pos.x+=self.vel
                        elif(self.obj.pos.x>=4*rad+d3+d1 and self.id==0):
                            a=9
vagones=[]
for v in tren:
    vagones.append(vagon(v))

vagones[0].id=0
etq_vel=label(pos=cabina3.pos+vec(0,1,0), text='0')

tiempo=60
i=0
vel=0.2
dif=0
cont=0
while(True):
    rate(tiempo)
    i+=1
    if i==tiempo:
        ac,dc=calculate(curva,estacion,vel)
        #print("estacion: "+str(estacion)+" velocidad: "+str(vel)+" ac: "+str(ac)+" dc: "+str(dc)+" curva: "+str(curva))
        i=0
        dif=ac-dc
        if vel+dif>0:
            if cont!=0:
                if cont==40:
                    cont=0
                else:
                    cont+=1
                    vel=0
                    dif=0
        else:
            dif=0
            cont+=1
        vel+=dif
    etq_vel.pos=cabina3.pos+vec(0,1,0)
    etq_vel.text=str(((vel-dif)+dif*(i/tiempo))*3.6)+" km/h"
    for e in vagones:
        e.vel=vel*(1/tiempo)
        e.movimiento()

