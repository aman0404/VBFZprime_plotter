from array import array
import ROOT
from ROOT import gStyle
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TGraphAsymmErrors, TLegend
#import CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
from ROOT import TAttFill, TCanvas, TGaxis, TLine,  TFile, TProfile, TNtuple, TH1F, TH2F, TColor
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import CMS_lumi

gStyle.SetOptStat(0)
gStyle.SetPalette(70)


points = [250, 500, 750, 1000, 1250, 1500,1750, 2000, 2250, 2500]
kv = [0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.4,0.6,0.8,1.0]
kv1 = [-0.0,0.30,0.45,0.65,0.85]
xsec = [119.2, 5.365, 0.8273, 0.1994, 0.06114, 0.02174, 0.008568, 0.003596, 0.001609, 0.0007504]
mp = [1285.6, 1483.7, 1614.3, 1701.3, 1771.4, 1970.2, 2201.2, 2436.5,2532.3, 2579.5, 2607.6]  #mutau gl=0
mpkv0p5 = [866.6, 1071.4, 1200.0, 1285.6, 1352.4, 1557.1, 1771.4, 1976.2, 2109.5, 2201.8, 2280.9] 
mpkv0p1 = [240,271.4, 338.1, 385.7,428.6,576.2,800.0, 1004.8, 1133.3, 1219.0, 1285.7]


mp_error1 = [1400.0, 1619.0, 1727.1, 1821.0, 1897.0,2110.1, 2333.3, 2529.1, 2592.9, 2624.5, 2643.4]
mp_error2 = [1161.9, 1376.2, 1490.5, 1580.9, 1652.4, 1852.4, 2076.2, 2295.2, 2438.1, 2503.6, 2547.4]

mp0p5_error1 = [971.4, 1200.0, 1323.8, 1414.3, 1466.6, 1680.9, 1885.7, 2109.5, 2242.8, 2333.3, 2400.0] 
mp0p5_error2 = [757.1, 942.8, 1071.4, 1157.1, 1228.6, 1438.1, 1647.6, 1857.1, 1980.9, 2076.2, 2147.6]

mp0p1_error1 = [240, 323.8, 390.5, 447.6, 480.9, 700.0, 919.0, 1133.3, 1261.9, 1357.1, 1419.0] 
mp0p1_error2 = [240, 240, 280.9, 328.6, 366.6, 480.9, 685.7, 885.7, 1004.8, 1090.5, 1161.9]

c1 = TCanvas( 'c1', 'Dynamic Filling Example',347,180,779,500)
c1.SetFillColor(0)
#c1.Range(-331.3253,-0.1263158,3012.048,1.123684)
#c1.SetFillColor(0)
#c1.SetBorderMode(0)
#c1.SetBorderSize(2)
#c1.SetRightMargin(0.1531532)
#c1.SetFrameBorderMode(0)
#c1.SetFrameBorderMode(0)

c1.Range(678.9465,-0.154752,2588.71,1.181743)
c1.SetFillColor(0)
c1.SetBorderMode(0)
c1.SetBorderSize(2)
c1.SetTickx(1)
c1.SetTicky(1)
c1.SetLeftMargin(0.08751608)
c1.SetRightMargin(0.08365508)
c1.SetBottomMargin(0.1157895)
c1.SetTopMargin(0.2547368)
c1.SetFrameBorderMode(0)
c1.SetFrameBorderMode(0)

c1.cd()
frame = c1.DrawFrame(2000.4,0.001, 2400.1, 10)
def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    hpxpy  = TH2F( 'hpxpy', '',10 , 250, 2750.,12,0.,1.2  )
    N_kv = len(kv)
    mg = TMultiGraph()
    gr = TGraph(N_kv)
    gr1 = TGraph(N_kv)
    gr2 = TGraph(N_kv)

    gr_error1 = TGraph(2*N_kv)

    gr1_error1 = TGraph(2*N_kv)

    gr2_error1 = TGraph(2*N_kv)

 #   gr2_error1 = TGraph(N_kv)
 #   gr2_error2 = TGraph(N_kv)

    N = len(points)
    up2s = [ ]
    for j in range(N_kv):
	#for i in range(N):
        #    file_name = "br"+str(kv[j])+"/higgsCombineTest.AsymptoticLimits.mH"+str(points[i])+".root"
        #    limit = getLimits(file_name)
#	#    print(limit[4])
	#    max_val = 1
	#    if(str(points[i])=="250"):
	#      max_val = limit[2]
#Aman

        #    gBenchmark.Start( 'hsimple' )
	histos = ['hpxpy']
    	#    for name in histos:
        #        exec('%sFill = %s.Fill' % (name,name))
    	#	binx = hpxpy.GetXaxis().FindBin(points[i])
    	#	biny = hpxpy.GetYaxis().FindBin(kv[j])
  	#	x = hpxpy.GetXaxis().GetBinCenter(binx)
    	#	y = hpxpy.GetYaxis().GetBinCenter(biny)
	#	fac = kv[j]*kv[j]
	#	if kv[j]==1.0: 
	#    	   hpxpy.SetBinContent(binx,biny,0.1*limit[2])
	#	else:
	#	   hpxpy.SetBinContent(binx,biny,0.01*limit[2])
	
	erry = [0.005,0.005,0.005,0.005,0.005,0.025,0.05,0.1,0.1,0.1,0.1]
        gr.SetPoint(j,mp[j],kv[j]) # median
#	gr.SetPointError(j,mp[j]-mp_error2[j],0.05)
	
        gr1.SetPoint(j,mpkv0p5[j],kv[j])
        gr2.SetPoint(j,mpkv0p1[j],kv[j])	
	gr_error1.SetPoint(2*N_kv-1-j,mp_error1[j],kv[j])
	gr_error1.SetPoint(j,mp_error2[j],kv[j])
#
#
	gr1_error1.SetPoint(2*N_kv-1-j,mp0p5_error1[j],kv[j])
	gr1_error1.SetPoint(j,mp0p5_error2[j],kv[j])
#
#
        gr2_error1.SetPoint(2*N_kv-1-j,mp0p1_error1[j],kv[j])
	gr2_error1.SetPoint(j,mp0p1_error2[j],kv[j])
#
#    hpxpy.GetZaxis().SetRangeUser(0.0001,0.02)
#    hpxpy.GetZaxis().SetNdivisions(5)
#    hpxpy.SetContour(nb)
#    hpxpy.Draw("CONT1Z")
#    hpxpy.Draw("COLZ Text")
#    hexp.Draw("SCAT same")
#    hexp.Draw("P* sames")
 #   gr.SetFillStyle(3001)
#    gr.SetFillColor(15)
#    gr.Draw("AC")

    gr1.SetLineStyle(1)
    gr1.SetLineColor(ROOT.kRed+3)
    gr1.SetLineWidth(2)
    gr1.SetTitle("")


    gr1.SetFillColor(ROOT.kRed-6)
    gr1.SetFillStyle(3001)
#    gr1_error1.SetLineColor(ROOT.kRed-6)
#    gr1_error1.SetLineStyle(6)
#    gr1_error1.SetLineWidth(2)
#    gr1_error1.SetTitle("")
#    gr1_error1.SetFillColor(ROOT.kRed-6)
#    gr1_error1.SetFillStyle(3001)
#
#    gr1_error2.SetLineColor(ROOT.kRed-6)
#    gr1_error2.SetLineStyle(6)
#    gr1_error2.SetLineWidth(2)
#    gr1_error2.SetTitle("")

    gr2.SetLineStyle(1)
    gr2.SetLineColor(9)
    gr2.SetLineWidth(2)
    gr2.SetTitle("")

    gr2.SetFillColor(ROOT.kBlue-6)
    gr2.SetFillStyle(3001)

    gr.SetLineStyle(1)
    gr.SetLineColor(ROOT.kGreen+3)
    gr.SetLineWidth(2)
    gr.SetTitle("")

    gr.SetFillColor(ROOT.kGreen+3)
    gr.SetFillStyle(3001)

    gr_error1.SetLineColor(ROOT.kGreen-2)
    gr_error1.SetLineStyle(6)
    gr_error1.SetLineWidth(2)
    gr_error1.SetTitle("")
    gr_error1.SetFillColor(ROOT.kGreen-2)
    gr_error1.SetFillStyle(3001)
#

    gr1_error1.SetLineColor(ROOT.kRed-2)
    gr1_error1.SetLineStyle(6)
    gr1_error1.SetLineWidth(2)
    gr1_error1.SetTitle("")
    gr1_error1.SetFillColor(ROOT.kRed-2)
    gr1_error1.SetFillStyle(3001)


    gr2_error1.SetLineColor(ROOT.kBlue-2)
    gr2_error1.SetLineStyle(6)
    gr2_error1.SetLineWidth(2)
    gr2_error1.SetTitle("")
    gr2_error1.SetFillColor(ROOT.kBlue-2)
    gr2_error1.SetFillStyle(3001)








    gr.Draw("AC")
    gr1.Draw("Csame")
    gr2.Draw("Csame")
    gr_error1.Draw("Fsame")
    gr1_error1.Draw("Fsame")
    gr2_error1.Draw("Fsame")
    gr.GetXaxis().SetLimits(250.,2500.)
    gr.GetYaxis().SetLimits(0.,0.9)
    gr.GetYaxis().SetRangeUser(0.,0.9)
    gr.GetYaxis().SetTitle("Branching fraction for Z' #rightarrow #tau#tau")
    gr.GetYaxis().SetTitleOffset(0.9)
    gr.GetXaxis().SetTitle("m_{Z'} [GeV]")
    gr.GetXaxis().SetTitleOffset(0.9)
    c1.Update()


    CMS_lumi.CMS_lumi(c1,4,11)
    ROOT.gPad.SetTicks(1,1)


    leg = TLegend(0.0875184,0.7420263,0.91635,0.885789)
    leg.SetNColumns(3)
    leg.SetBorderSize(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(1001)
    leg.SetTextFont(42)
    leg.SetTextSize(0.047)
    leg.SetHeader("VBF Z' Search")
    leg.AddEntry(gr2,"#kappa_{V} : 0.1","lf")
    leg.AddEntry(gr1,"#kappa_{V} : 0.5","lf")
    leg.AddEntry(gr,"#kappa_{V} : 1.0","lf")
    leg.Draw()



#    for name in histos:
#        exec('del %sFill' % name)
#    del histos
#     
#    gBenchmark.Show( 'hsimple' )
    
    c1.Modified()
    c1.Update()
    c1.SaveAs("br_all_tautau_gl0_UpperLimit.pdf")
    c1.SaveAs("br_all_tautau_gl0_UpperLimit.png")
    c1.SaveAs("br_all_tautau_gl0_UpperLimit.root")
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

