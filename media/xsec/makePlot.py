#!/usr/bin/env python

###################
# Import packages #
###################
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plotting
from math import sqrt
from operator import mul, add, sub

plotting.rc('text', usetex=True)
plotting.rc('font', family='serif')

listMasses             = []
listXsec8TeV           = []
listXsec8TeVRelUncert  = []
listXsec13TeV          = []
listXsec13TeVRelUncert = []

with open("xsec.dat", "r") as file :

    for line in file :
        [mass, xsec8TeV, xsec8TeVUncert, xsec13TeV, xsec13TeVUncert] = line.split(" ")
        listMasses.append(int(mass))
        listXsec8TeV.append(float(xsec8TeV)) 
        listXsec8TeVRelUncert.append(float(xsec8TeVUncert)/100)
        listXsec13TeV.append(float(xsec13TeV))
        listXsec13TeVRelUncert.append(float(xsec13TeVUncert)/100)

listXsec8TeVPlus1Sigma   = [xsec * (1+reluncert) for (xsec, reluncert) in zip(listXsec8TeV,  listXsec8TeVRelUncert)]
listXsec8TeVMinus1Sigma  = [xsec * (1-reluncert) for (xsec, reluncert) in zip(listXsec8TeV,  listXsec8TeVRelUncert)]
listXsec13TeVPlus1Sigma  = [xsec * (1+reluncert) for (xsec, reluncert) in zip(listXsec13TeV, listXsec13TeVRelUncert)]
listXsec13TeVMinus1Sigma = [xsec * (1-reluncert) for (xsec, reluncert) in zip(listXsec13TeV, listXsec13TeVRelUncert)]
   
plotting.figure()
plotting.xlabel(r"$\tilde{t}_1$ mass [GeV]", fontsize = 16)
plotting.ylabel(r"Direct $\tilde{t}_1$ pair production cross-section [pb]", fontsize = 16)
plotting.grid()

plotting.semilogy(listMasses,listXsec8TeV, 'r-', linewidth=1.5, color="#0077ff", label="pp, 8 TeV NLO")
plotting.fill_between(listMasses,listXsec8TeVPlus1Sigma, listXsec8TeVMinus1Sigma, alpha=0.1, facecolor="#0077ff")

plotting.semilogy(listMasses,listXsec13TeV, 'r-', linewidth=1.5, color="#ff7700", label="pp, 13 TeV NLO")
plotting.fill_between(listMasses,listXsec13TeVPlus1Sigma, listXsec13TeVMinus1Sigma, alpha=0.1, facecolor="#ff7700")

plotting.legend(loc="upper right")

plotting.savefig("plot.pdf")
