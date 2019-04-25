#!/usr/bin/python

import sys, string
import numpy as np
from math import sqrt, pi


def hist(a):
        start=-180.0-7.5
        binnumber=24
        binsize=360/binnumber
        bincount=np.zeros(binnumber)
        for n1 in a:
            nindex=int((n1-start)/binsize)
            if nindex >= binnumber:
                nindex=0
            bincount[nindex]+=1
        return bincount

def hist2(a):
        start=-180.0-7.5
        binnumber=24
        binsize=360/binnumber
        bincount=np.zeros(binnumber)
        for n1 in a:
            n1=np.abs(n1) # for asp, phe, tyr's chi2
            nindex=int((n1-start)/binsize)
            if nindex >= binnumber:
                nindex=0
            bincount[nindex]+=1
        return bincount

def hist2d(a,b):
# to do 2-dimensional binning, still returning 1-d probability distribution
        start=-180.0-7.5
        binnumber=24
        binsize=360/binnumber
        binstart=[]
        binstop=[]
        for i in range(binnumber):
            binstart.append(start+binsize*i)
            binstop.append(start+binsize+binsize*i)
        bincount=np.zeros(binnumber*binnumber)
        nlen=len(a)
        for n in range(nlen):
            index1=int((a[n]-start)/binsize)
            if index1 >= binnumber:
                index1=0
            index2=int((b[n]-start)/binsize)
            if index2 >= binnumber:
                index2=0
            bincount[index1*binnumber+index2]+=1
        #bincount=bincount/len(a)
        return bincount        

def hist2d2(a,b):
#   hist2d for asp and tyr
        start=-180.0-7.5
        binnumber=24
        binsize=360/binnumber
        binstart=[]
        binstop=[]
        for i in range(binnumber):
            binstart.append(start+binsize*i)
            binstop.append(start+binsize+binsize*i)
        bincount=np.zeros(binnumber*binnumber)
        nlen=len(a)
        for n in range(nlen):
            index1=int((a[n]-start)/binsize)
            if index1 >= binnumber:
                index1=0
            index2=int((np.abs(b[n])-start)/binsize)
            if index2 >= binnumber:
                index2=0
            bincount[index1*binnumber+index2]+=1
        return bincount

def oc(x,y):
        c1=0.0
        c2=0.0
        c3=0.0
        for i in range(len(x)):
            c1+=x[i]*y[i]
            c2+=x[i]*x[i]
            c3+=y[i]*y[i]
        c=c1/np.sqrt(c2*c3)
        return c


if __name__ == "__main__":
    compchi2=1
    mmfile=np.loadtxt(sys.argv[1]).T
    xrayfile=np.loadtxt(sys.argv[2]).T
    if compchi2:
        chi1mm=mmfile[0]
        chi2mm=mmfile[1]
        chi1pdb=xrayfile[0]
        chi2pdb=xrayfile[1]
        print 'chi1:',oc(hist(chi1mm),hist(chi1pdb))
        print 'chi2:',oc(hist(chi2mm),hist(chi2pdb))
        print '2D OC:',oc(hist2d(chi1mm,chi2mm),hist2d(chi1pdb,chi2pdb))
    else:
        #chi1mm=mmfile # for Val
        chi1mm=mmfile[0]
        chi1pdb=xrayfile
        print 'chi1:',oc(hist(chi1mm),hist(chi1pdb))
