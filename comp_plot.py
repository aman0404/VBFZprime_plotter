from array import array
import ROOT
from ROOT import gStyle
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
#import CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
from ROOT import TCanvas, TGaxis, TLine,  TFile, TProfile, TNtuple, TH1F, TH2F, TColor
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
import CMS_lumi
import math 

gStyle.SetOptStat(0)
#gStyle.SetPalette(52)
#nb=256
#TColor.InvertPalette()
ncontours = 512
#stops = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.08, 0.20, 0.40, 0.70, 0.9]
#red   = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]
#green = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]
#blue  = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]


stops = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.30, 0.50, 0.60]
red   = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]
green = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]
blue  = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]



s = array('d', stops)
r = array('d', red)
g = array('d', green)
b = array('d', blue)

npoints = len(s)
TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
gStyle.SetNumberContours(ncontours)


points = [250, 500, 750, 1000, 1250, 1500,1750, 2000, 2250, 2500]
kv = [0.1,0.25,0.50,0.75,1.0]
kv1 = [-0.0,0.30,0.45,0.65,0.85]
xsec = [119.2, 5.365, 0.8273, 0.1994, 0.06114, 0.02174, 0.008568, 0.003596, 0.001609, 0.0007504]
mp = [1300,1730,2030,2210,2355]  #mutau gl=0

c1 = TCanvas( 'c1', 'Dynamic Filling Example',340,71,779,500 )
c1.SetFillColor(0)
#c1.Range(-331.3253,-0.1263158,3012.048,1.123684)
#c1.SetFillColor(0)
#c1.SetBorderMode(0)
#c1.SetBorderSize(2)
#c1.SetRightMargin(0.1531532)
#c1.SetFrameBorderMode(0)
#c1.SetFrameBorderMode(0)

c1.Range(-463.5762,-0.6847545,2752.483,5.452196)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetBorderSize(2)
c1.SetTickx(1)
c1.SetTicky(1)
c1.SetLeftMargin(0.1441441)
c1.SetRightMargin(0.07850708)
c1.SetTopMargin(0.07368421)
c1.SetBottomMargin(0.1115789)
c1.SetFrameBorderMode(0)
c1.SetFrameBorderMode(0)

case4_ratio = [1.11111111111,1.09495548961,1.05964912281,1.06040268456,1.06315789474,1.05194805195,1.05797101449,1.046875,1.06557377049,1.06779661017]
case5_ratio = [1,0.988130563798,0.99298245614,1.02013422819,1.02105263158,1.02597402597,1.02898550725,1.03125,1.03278688525,1.03389830508]
case1_more_ratio = [0.98, 1, 1.05, 1.06040268456, 1.06315789474, 1.05194805195, 1.07246376812, 1.078125, 1.09836065574, 1.10169491525]

def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    hpxpy  = TH1F( 'hpxpy', '',10 , 0, 2500.)
    N_kv = len(kv)
    N = len(points)
    gr = TGraph(N)
    up2s = [ ]
    for i in range(N):
        file_name = "btest_nosys/higgsCombine.Test.AsymptoticLimits.mH"+str(points[i])+".root"
        file_name1 = "btest/case3/higgsCombine.Test.AsymptoticLimits.mH"+str(points[i])+".root"
	limit = getLimits(file_name)
	limit_vbf = getLimits_vbf(file_name1)
#	print(limit[4])
#Aman

        gBenchmark.Start( 'hsimple' )
	histos = ['hpxpy']
    	for name in histos:
            exec('%sFill = %s.Fill' % (name,name))
    	    binx = hpxpy.GetXaxis().FindBin(points[i])
    	    #biny = hpxpy.GetYaxis().FindBin(kv1[j])
    	    x = hpxpy.GetXaxis().GetBinCenter(binx-1)
    	    #y = hpxpy.GetYaxis().GetBinCenter(biny)
    	    #fac = kv[j]*kv[j] 
	    fac = math.fabs((0.01*limit_vbf[2]))/math.fabs((0.01*limit[2]))    
            print(fac)
        #    hpxpy.Fill(fac)
            gr.SetPoint(i,points[i],fac) # median

            hpxpy.Draw("lep")


    hpxpy.GetYaxis().SetTitle("#frac{with b sys}{no b sys}")
    hpxpy.GetYaxis().SetTitleSize(0.035)
    hpxpy.GetYaxis().SetTitleOffset(1.3)
    hpxpy.GetYaxis().SetLabelSize(0.045)
    hpxpy.GetYaxis().SetRangeUser(0.5,1.5)
    
    hpxpy.GetXaxis().SetTitle("m_{Z'} [GeV]")
    hpxpy.GetXaxis().SetTitleSize(0.05)
    hpxpy.GetXaxis().SetTitleOffset(0.9)
    hpxpy.GetXaxis().SetLabelSize(0.045)

    gr.Draw("same")
    gr.SetLineStyle(10)
    gr.SetLineColor(1)
    gr.SetLineWidth(3)

#    a = hpxpy.GetYaxis()
#    a.SetNdivisions(20)
#    a.SetNdivisions(6)
    val = ["0.1", "0.25", "0.50", "0.75", "1.0","."]
    
#    for i in range(6):
#        a.ChangeLabel((i+1), -1, -1, -1, -1, -1, val[i])
#    a.CenterLabels(1)

    #CMS_lumi.CMS_lumi(c1,4,11)
    ROOT.gPad.SetTicks(1,1)


    leg = TLegend(0.0996654,0.7597895,0.8450476,0.9)
    leg.SetNColumns(2)
    leg.SetBorderSize(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(1001)
    leg.SetTextFont(42)
    leg.SetTextSize(0.047)
#    leg.AddEntry(gr,"Exp #pm std. deviation","LP")
#    leg.AddEntry(gr,".","P")
#    leg.AddEntry(gr,"VBF Z' #rightarrow #tau#tau ; g_{l}=0, g_{h}=1","LP")
#    leg.Draw()



    for name in histos:
        exec('del %sFill' % name)
    del histos
     
    gBenchmark.Show( 'hsimple' )
    
    c1.Modified()
    c1.Update()
    c1.SaveAs("comparison_bsys_case5_Upperlimit_test.png")
    c1.SaveAs("comparison_bsys_case5_Upperlimit_test.pdf")
    c1.SaveAs("comparison_bsys_case5_Upperlimit_test.root")
    c1.Close()

def getLimits(file_name):
        file = TFile(file_name)
        tree = file.Get("limit")

        limits = [ ]
        for quantile in tree:
            limits.append(tree.limit)
#            print ">>>   %.2f" % limits[-1]

        return limits[:6]

def getLimits_vbf(file_name1):
        file = TFile(file_name1)
        tree = file.Get("limit")

        limits_vbf = [ ]
        for quantile in tree:
            limits_vbf.append(tree.limit)
#            print ">>>   %.2f" % limits[-1]

        return limits_vbf[:6]

def main():
        plotUpperLimits(points)
if __name__ == '__main__':
    main()

