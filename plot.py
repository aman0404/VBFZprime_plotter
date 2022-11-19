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

c1 = TCanvas( 'c1', 'Dynamic Filling Example',75,53,779,500 )
c1.SetFillColor(0)
#c1.Range(-331.3253,-0.1263158,3012.048,1.123684)
#c1.SetFillColor(0)
#c1.SetBorderMode(0)
#c1.SetBorderSize(2)
#c1.SetRightMargin(0.1531532)
#c1.SetFrameBorderMode(0)
#c1.SetFrameBorderMode(0)

c1.Range(-331.3253,-0.1769437,3012.048,1.351206)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetBorderSize(2)
c1.SetTickx(1)
c1.SetTicky(1)
c1.SetRightMargin(0.1531532)
c1.SetBottomMargin(0.1157895)
c1.SetFrameBorderMode(0)
c1.SetFrameBorderMode(0)


def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    hpxpy  = TH2F( 'hpxpy', '',10 , 0, 2500.,6,0.,1.2  )
    N_kv = len(kv)
    gr = TGraph(N_kv)
    N = len(points)
    up2s = [ ]
    for j in range(N_kv):
	for i in range(N):
            file_name = "WWgl0_20perdata_kv1p0/higgsCombine.Test.AsymptoticLimits.mH"+str(points[i])+".root"
            limit = getLimits(file_name)
#	    print(limit[4])
	    max_val = 1
	    if(str(points[i])=="250"):
	      max_val = limit[2]
#Aman

            gBenchmark.Start( 'hsimple' )
	    histos = ['hpxpy']
    	    for name in histos:
                exec('%sFill = %s.Fill' % (name,name))
    		binx = hpxpy.GetXaxis().FindBin(points[i])
    		biny = hpxpy.GetYaxis().FindBin(kv1[j])
    		x = hpxpy.GetXaxis().GetBinCenter(binx-1)
    		y = hpxpy.GetYaxis().GetBinCenter(biny)
    		fac = kv[j]*kv[j] 
		if kv[j]==0.25 or kv[j]==0.50:   
               	   hpxpy.SetBinContent(i+1,j+1,0.01*limit[2])
		else:
		   hpxpy.SetBinContent(i+1,j+1,0.1*limit[2])
    		gr.SetPoint(j,mp[j],kv[j]) # median

    hpxpy.GetZaxis().SetRangeUser(0.0001,0.02)
    hpxpy.GetZaxis().SetNdivisions(5)
#    hpxpy.SetContour(nb)
    hpxpy.Draw("colz")
#    hexp.Draw("SCAT same")
#    hexp.Draw("P* sames")
    gr.Draw("same")
    gr.SetLineStyle(10)
    gr.SetLineColor(1)
    gr.SetLineWidth(3)


    hpxpy.GetYaxis().SetTitle("#kappa_{V}")
    hpxpy.GetYaxis().SetTitleSize(0.05)
    hpxpy.GetYaxis().SetTitleOffset(0.7)
    hpxpy.GetYaxis().SetLabelSize(0.045)
    
    hpxpy.GetXaxis().SetTitle("M_{Z'} [GeV]")
    hpxpy.GetXaxis().SetTitleSize(0.05)
    hpxpy.GetXaxis().SetTitleOffset(0.9)
    hpxpy.GetXaxis().SetLabelSize(0.045)

    hpxpy.GetZaxis().SetTitle("Cross section UL at 95% CL [pb]")
    hpxpy.GetZaxis().SetTitleSize(0.05)
    hpxpy.GetZaxis().SetTitleOffset(1.0)
    hpxpy.GetZaxis().SetLabelSize(0.04)
    hpxpy.GetZaxis().CenterTitle(1)

#    a = hpxpy.GetYaxis()
#    a.SetNdivisions(20)
#    a.SetNdivisions(6)
    val = ["0.1", "0.25", "0.50", "0.75", "1.0","."]
    
#    for i in range(6):
#        a.ChangeLabel((i+1), -1, -1, -1, -1, -1, val[i])
#    a.CenterLabels(1)

    CMS_lumi.CMS_lumi(c1,4,11)
    ROOT.gPad.SetTicks(1,1)


    leg = TLegend(0.0996654,0.7597895,0.8450476,0.9)
    leg.SetNColumns(2)
    leg.SetBorderSize(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(1001)
    leg.SetTextFont(42)
    leg.SetTextSize(0.047)
    leg.AddEntry(gr,"Exp #pm std. deviation","LP")
    leg.AddEntry(gr,".","P")
    leg.AddEntry(gr,"VBF Z' #rightarrow #tau#tau ; g_{l}=0, g_{h}=1","LP")
    leg.Draw()



    for name in histos:
        exec('del %sFill' % name)
    del histos
     
    gBenchmark.Show( 'hsimple' )
    
    c1.Modified()
    c1.Update()
    c1.SaveAs("2D_WW_gl0_UpperLimit.pdf")
    c1.SaveAs("2D_WW_gl0_UpperLimit.root")
    c1.Close()

def getLimits(file_name):
        file = TFile(file_name)
        tree = file.Get("limit")

        limits = [ ]
        for quantile in tree:
            limits.append(tree.limit)
#            print ">>>   %.2f" % limits[-1]

        return limits[:6]

def main():
        plotUpperLimits(points)
if __name__ == '__main__':
    main()

