from array import array
import ROOT
from ROOT import gStyle
from ROOT import TGraphAsymmErrors, TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
#import CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
from ROOT import TCanvas, TGaxis, TLine,  TFile, TProfile, TNtuple, TH1F, TH2F, TColor
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import CMS_lumi

gStyle.SetOptStat(0)
gStyle.SetPalette(76)
#nb=256
TColor.InvertPalette()
ncontours = 256
#stops = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.08, 0.20, 0.40, 0.70, 0.9]
#red   = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]
#green = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]
#blue  = [1.00, 0.84, 0.61, 0.58, 0.48, 0.38, 0.28, 0.25, 0.18, 0.10, 0.05]


#stops = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.30, 0.50, 0.60]
#red   = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]
#green = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]
#blue  = [1.00, 0.84, 0.71, 0.68, 0.60, 0.55, 0.50, 0.47, 0.42, 0.38, 0.32, 0.25, 0.15]
#
#
#
#s = array('d', stops)
#r = array('d', red)
#g = array('d', green)
#b = array('d', blue)
#
#npoints = len(s)
#TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
gStyle.SetNumberContours(ncontours)


points = [250, 500, 750, 1000, 1250, 1500,1750, 2000, 2250, 2500]
kv = [0.1,0.25,0.50,0.75,1.0]
kvp = ['0p1','0p25','0p50','0p75','1p0']
kv1 = [-0.0,0.30,0.45,0.65,0.85]
xsec = [119.2, 5.365, 0.8273, 0.1994, 0.06114, 0.02174, 0.008568, 0.003596, 0.001609, 0.0007504]

mp =     [250.0, 705.8, 1102.4, 1373.7, 1559.5]  #exp gl=0
mp_minSig = [400,798.2, 1224.6, 1496.0, 1690.5]
mp_posSig = [200, 625.2, 983.1, 1245.5, 1443.4]

mp_obs = [200, 869.8, 1278.3, 1543.7, 1735.1]  #exp gl=0

c1 = TCanvas( 'c1', 'Dynamic Filling Example',75,53,1000,700 )
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
c1.SetRightMargin(0.16)
c1.SetBottomMargin(0.125)
c1.SetTopMargin(0.249)
c1.SetFrameBorderMode(0)
c1.SetFrameBorderMode(0)


def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    hpxpy  = TH2F( 'hpxpy', '',10 , 125., 2625.,5,0.,1.0  )
    N_kv = len(kv)
    gr = TGraph(N_kv)
    #gr = TGraphAsymmErrors(N_kv)
    gr_minSig = TGraph(N_kv)
    gr_posSig = TGraph(N_kv)
    gr_obs = TGraph(N_kv)
    gr_obsmin = TGraph(N_kv)
    gr_obspos = TGraph(N_kv)
    N = len(points)
    up2s = [ ]
    for j in range(N_kv):
	for i in range(N):
            file_name = "tau_gl1_20perdata_kv"+kvp[j]+"/higgsCombine.Test.AsymptoticLimits.mH"+str(points[i])+".root"
#            print("WWgl0_20perdata_kv"+kvp[j])
	    limit = getLimits(file_name)
#Aman

            gBenchmark.Start( 'hsimple' )
	    histos = ['hpxpy']
    	    for name in histos:
                exec('%sFill = %s.Fill' % (name,name))
    		binx = hpxpy.GetXaxis().FindBin(points[i])
    		biny = hpxpy.GetYaxis().FindBin(kv1[j])
    		x = hpxpy.GetXaxis().GetBinCenter(binx)
    		y = hpxpy.GetYaxis().GetBinCenter(biny)
		xx = hpxpy.GetXaxis().FindBin(x)
                yy = hpxpy.GetYaxis().FindBin(y)
		hpxpy.SetBinContent(xx,yy,limit[2])
    		#gr.SetPoint(yy,mp[j],kv[j]) # median
    		gr.SetPoint(yy,mp[j],kv[j])
    		gr_minSig.SetPoint(yy,mp_posSig[j], kv[j])
    		gr_posSig.SetPoint(yy,mp_minSig[j], kv[j])
    		gr_obs.SetPoint(yy,mp_obs[j],kv[j]) # median
    		gr_obsmin.SetPoint(yy,mp_obs[j]-0.002*mp_obs[j],kv[j]) # median
    		gr_obspos.SetPoint(yy,mp_obs[j]+0.002*mp_obs[j],kv[j]) # median

    hpxpy.GetZaxis().SetRangeUser(0.0005,1.)
    hpxpy.GetYaxis().SetRangeUser(0,1.)
    ROOT.gPad.SetLogz()
#    hpxpy.GetZaxis().SetNdivisions(5)
#    hpxpy.SetContour(nb)
    hpxpy.Draw("colz C")
#    hexp.Draw("SCAT same")
#    hexp.Draw("P* sames")
    gr.Draw("lep same")
    gr.SetLineStyle(2)
    gr.SetLineColor(2)
    gr.SetLineWidth(5)

    gr_minSig.Draw("C same")
    gr_minSig.SetLineStyle(2)
    gr_minSig.SetLineColor(2)
    gr_minSig.SetLineWidth(2)

    gr_posSig.Draw("C same")
    gr_posSig.SetLineStyle(2)
    gr_posSig.SetLineColor(2)
    gr_posSig.SetLineWidth(2)

    gr_obs.Draw("C same")
    gr_obs.SetLineStyle(1)
    gr_obs.SetLineColor(1)
    gr_obs.SetLineWidth(4)

    gr_obsmin.Draw("C same")
    gr_obsmin.SetLineStyle(2)
    gr_obsmin.SetLineColor(1)
    gr_obsmin.SetLineWidth(2)

    gr_obspos.Draw("C same")
    gr_obspos.SetLineStyle(2)
    gr_obspos.SetLineColor(1)
    gr_obspos.SetLineWidth(2)

    hpxpy.GetYaxis().SetTitle("#kappa_{V}")
    hpxpy.GetYaxis().SetTitleSize(0.06)
    hpxpy.GetYaxis().SetTitleOffset(0.7)
    hpxpy.GetYaxis().SetLabelSize(0.05)
    
    hpxpy.GetXaxis().SetTitle("m_{Z'} [GeV]")
    hpxpy.GetXaxis().SetTitleSize(0.055)
    hpxpy.GetXaxis().SetTitleOffset(1.0)
    hpxpy.GetXaxis().SetLabelSize(0.05)

    hpxpy.GetZaxis().SetTitle("95% CL upper limit on cross section [pb]")
    hpxpy.GetZaxis().SetTitleSize(0.05)
    hpxpy.GetZaxis().SetTitleOffset(1.0)
    hpxpy.GetZaxis().SetLabelSize(0.05)
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


    leg = TLegend(0.0996654,0.75,0.8450476,0.90)
    leg_obs = TLegend(0.62,0.75,0.8450476,0.90)

    legup = TLegend(0.0996654,0.70,0.8450476,0.84)
    legup_obs = TLegend(0.62,0.70,0.8450476,0.84)

    legdn = TLegend(0.0996654,0.73,0.8450476,0.88)
    legdn_obs = TLegend(0.62,0.73,0.8450476,0.88)
#    leg.SetNColumns(2)
    leg.SetBorderSize(1)
    legup.SetBorderSize(0)
    legdn.SetBorderSize(0)

    leg_obs.SetBorderSize(0)
    legup_obs.SetBorderSize(0)
    legdn_obs.SetBorderSize(0)

    leg.SetFillStyle(0)
    leg_obs.SetFillStyle(0)
    
    legup.SetFillStyle(0)
    legup_obs.SetFillStyle(0)
    
    legdn.SetFillStyle(0)
    legdn_obs.SetFillStyle(0)
    leg.SetFillStyle(1001)
    leg.SetTextFont(42)
    leg_obs.SetTextFont(42)
    leg.SetTextSize(0.045)
    leg_obs.SetTextSize(0.045)
    leg_obs.SetHeader(" ")
    leg.SetHeader("VBF Z' #rightarrow #tau#tau (g_{l} = 1, g_{h} = 1), #it{#Beta} = 20%")
#    leg.AddEntry(gr_minSig," ","l")
#    leg.AddEntry(gr_obsmin," ","L")
    leg.AddEntry(gr,"Expected, median & 68%","l")
    leg_obs.AddEntry(gr_obs,"Observed","L")
#    leg.AddEntry(gr_posSig," ","l")
#    leg.AddEntry(gr_minSig,"Expected","LP")
#    leg.AddEntry(gr_obspos," ","L")
    leg.Draw()
    leg_obs.Draw()

    legup.AddEntry(gr_posSig," ","l")
#    legup_obs.AddEntry(gr_obspos," ","l")
    legup.Draw()
    legup_obs.Draw()

    legdn.AddEntry(gr_minSig," ","L")
#    legdn_obs.AddEntry(gr_obsmin," ","l")
    legdn.Draw()
    legdn_obs.Draw()

    for name in histos:
        exec('del %sFill' % name)
    del histos
     
    gBenchmark.Show( 'hsimple' )
    
    c1.Modified()
    c1.Update()
    c1.SaveAs("2D_tau_gl1_UpperLimit.pdf")
    c1.SaveAs("2D_tau_gl1_UpperLimit.root")
    c1.Close()

def getLimits(file_name):
        file = TFile(file_name)
        tree = file.Get("limit")

        limits = [ ]
        for quantile in tree:
            limits.append(0.01*tree.limit)
#            print ">>>   %.2f" % limits[0]

        return limits[:6]

def main():
        plotUpperLimits(points)
if __name__ == '__main__':
    main()

