# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:09:18 2010

@author: Ludovic Autin
"""
import math
import sys,os
from random import random

#pyubic have to be in the pythonpath, if not add it
pathtoupy = "/Users/ludo/DEV/upy/trunk/"
sys.path.insert(0,pathtoupy)

import upy
from upy import colors as col

#get the helperClass for modeling
helperClass = upy.getHelperClass()
helper = helperClass()

sc = helper.getCurrentScene()

#camera and light
center=[0.,-12.,40.]
cam = helper.addCameraToScene("cam1","persp",30.,center,sc)

light = helper.addLampToScene("light1","Sun",[1.,1.,1.],20.,1.0,1.0,True,center,sc)

t,extruder= helper.Text("text",string="upy",size=5.,pos=[0.,4.,0.],extrude=True)
#helper.rotateObj(t,(0.,0.,math.pi/2.))

Y=0.
simple = helper.Text("basicobjectLabel",string="BasicObject",size=2.,
                              pos=[-18.,0.,0.],extrude=extruder)
#helper.rotateObj(simple,(0.,math.pi/2.,0.))

basic = helper.newEmpty("BasicObject",location=[0.,Y,0.])

s,ms = helper.Sphere("sphere",radius=2.0,res=12,pos = [4.,Y,0.],parent=basic)
helper.changeColor(s,col.red)
helper.rotateObj(s,(math.pi/2.,0.,0.))

c,mc = helper.Cube("cube",center = [8.,0.,0.],size=[2.,2.,2.],parent=basic)
helper.changeColor(c,col.blue)
helper.rotateObj(c,(math.pi/2.,0.,0.))
#
cy,mcy= helper.Cylinder("cylinder",radius=2.,length=4.,res=12, pos = [-4.,Y,0.],parent=basic)
helper.changeColor(cy,col.green)
helper.rotateObj(cy,(math.pi/2.,0.,0.))
#
cone,mcone = helper.Cone("cone",radius=1.5,length=3.,res=9, pos = [0.,Y,0.],parent=basic)
helper.changeColor(cone,col.yellow)
helper.rotateObj(cone,(math.pi/2.,0.,0.))

p,mpl = helper.plane("plane",center = [-9.,Y,0.],size=[5.,5.],parent=basic)
filename = upy.__path__[0]+os.sep+"examples"+os.sep+"marble.jpg"
mat = helper.createTexturedMaterial("planeMat",filename)
helper.assignMaterial(p,mat,texture=True)
#
Y = -6.
complex = helper.Text("lineobjectLabel",string="LineObject",size=2.,
                      pos=[-18.,Y ,0.],extrude = extruder)
##helper.rotateObj(complex,(0.,math.pi/2.,0.))


#helper.rotateObj(instance,(0.,math.pi/2.,0.))

#curve pts
listPts = ( 
        ( 5.598 , 5.767 , 11.082),
        ( 8.496 , 4.609 , 8.837),
        ( 6.500 , 1.584 , 7.565),
        ( 3.545 , 3.935 , 6.751),
        ( 5.929 , 6.358 , 5.055),
        ( 7.331 , 3.607 , 2.791),
        ( 3.782 , 2.599 , 1.742),
        ( 2.890 , 6.285 , 1.126),
#        ( 5.895 , 6.489 , -1.213),
#        ( 4.933 , 3.431 , -3.326),
#        ( 2.792 , 5.376 , -5.797),
        )
line = helper.newEmpty("LineObject",location=[0.,0.,0.])
#spline
Y= -7.
spline,mspline = helper.spline("spline", listPts,close=0,type=1,parent=line)
helper.rotateObj(spline,(0.,math.pi/2.,0.))
helper.setTranslation(spline,[ -8.377, Y,2.556])
helper.scaleObj(spline,[ 0.5, 0.5,0.5])

#loft spline extrusion
extruder_spline,shape,spline_clone = helper.extrudeSpline(spline,shape="circle",clone = True)
#or instance
helper.rotateObj(extruder_spline,(0.,math.pi/2.,0.))
helper.setTranslation(extruder_spline,[ -1.7, Y,2.556])
helper.scaleObj(extruder_spline,[ 0.5, 0.5,0.5])
helper.reParent(extruder_spline,line)

#armature
armature,bones = helper.armature("armature",listPts,scn=sc,root=line)
helper.rotateObj(armature,(0.,math.pi/2.,0.))
helper.setTranslation(armature,[ 4.0, Y,2.556])
helper.scaleObj(armature,[ 0.5, 0.5,0.5])

Y = -12.
#points object : poin cloud, metaballs, particle
pointsLabel = helper.Text("pointsobjectLabel",string="PointsObject",size=2.,
                       pos=[-18.,Y,0.],extrude = extruder)
points = helper.newEmpty("PointsObject",location=[0.,0.,0.])
#pointClouds
pointscloud, mesh_pts = helper.PointCloudObject("pts_cloud",
                                        vertices=listPts,
                                        parent=points)
helper.rotateObj(pointscloud,(0.,math.pi/2.,0.))
helper.setTranslation(pointscloud,[ -8.377, Y,2.556])
helper.scaleObj(pointscloud,[ 0.5, 0.5,0.5])

#particle
f,modifiedVertex,n = helper.DecomposeMesh(pointscloud,edit=True,copy=True,
                                          tri=True,transform=True)
p = helper.particle("particle",modifiedVertex)

helper.setTranslation(pointscloud,[ -2.38, Y,2.556])
#surface
#metaball
metab,cloud = helper.metaballs("metaballs",listPts,None,scn=sc,root=points)
helper.rotateObj(metab,(0.,math.pi/2.,0.))
helper.setTranslation(metab,[ 4.0, Y,2.556])
helper.scaleObj(metab,[ 0.5, 0.5,0.5])

#Mesh
#platonic
Y = -18.
#points object : poin cloud, metaballs, particle
platonicLabel = helper.Text("platonicLabel",string="PlatonicObject",size=2.,
                       pos=[-18.,Y,0.],extrude = extruder)
platonic = helper.newEmpty("PlatonicObject",location=[0.,0.,0.])
#pointClouds
tetra,mtetra = helper.Platonic("Tetra","tetra",2.0,parent=platonic)
helper.setTranslation(tetra,[ -8.0, Y,0.])
hexa,mhexa = helper.Platonic("Hexa","hexa",2.0,parent=platonic)
helper.setTranslation(hexa,[ -4.5, Y,0.])
octa,mocta = helper.Platonic("Octa","octa",2.0,parent=platonic)
helper.setTranslation(octa,[ -0.8, Y,0.])
dodeca,mdodeca = helper.Platonic("Dodeca","dodeca",2.0,parent=platonic)
helper.setTranslation(dodeca,[ 3.15, Y,0.])
icosa,micosa = helper.Platonic("Icosa","icosa",2.0,parent=platonic)
helper.setTranslation(icosa,[ 7.81, Y,0.])

#instance
##compute instance
##one instance
##matrice instance
##object vertice instance
Y = -24.0
instancelabel = helper.Text("instanceLabel",string="InstanceObject",size=2.,
                       pos=[-18.,Y,0.],extrude = extruder)
instance = helper.newEmpty("InstanceObject",location=[0.,0.,0.])
#one instance
inst = helper.newInstance("instanceOfIco",icosa,location=[ -8.0, Y,0.],
                          parent = instance)
#list instance from an object vertices
isph = helper.newEmpty("InstanceOfSpheres",location=[0.,0.,0.],parent = instance)
f,verts,n = helper.DecomposeMesh(inst,edit=True,copy=True,tri=True,transform=True)
for i,v in enumerate(verts):
    instsph = helper.newInstance("instanceOfSph"+str(i),s,location=v,
                          parent = isph)
    helper.scaleObj(instsph,[ 0.1, 0.1,0.1])
#list instance from list of matrices
itetra = helper.newEmpty("InstanceOfTetra",location=[0.0, Y,0.],parent = instance)
listM = []
for i,p in enumerate(modifiedVertex):
    m = helper.rotation_matrix(random()*math.pi, [random(),random(),random()])
    m[:3, 3] = p
    listM.append(m.transpose())
ipoly = helper.instancePolygon("instOfTetra", matrices=listM, mesh=tetra,
                    parent = itetra)
helper.setTranslation(itetra,[ 6.0, -38,0.])#?

#some volume ?
#some physics ?
#set an object as rigid-body
#set an object as soft-body
#change some paramter

#helper.fit_view3D()

##execfile("/Users/ludo/DEV/upy/examples/BasicGeom.py")
#Blender Text Run Python Script
#maya open and run in the console OR execfile("pathto/pyubic/examples/Cube_Sphere.py")
#dejavu mgtloos/bin/pythonsh -i Cube_Sphere.py