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


points = [250, 500, 750, 1000, 1250, 1700,1750, 2000, 2250, 2500]
kv = [0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.4,0.6,0.8,1.0]
kv1 = [-0.0,0.30,0.45,0.65,0.85]
xsec = [119.2, 5.365, 0.8273, 0.1994, 0.06114, 0.02174, 0.008568, 0.003596, 0.001609, 0.0007504]

mpkv0p1 = [100, 150, 170, 200, 210, 220, 279.1, 428.2, 493.8, 592.2, 654.9]
mpkv0p25 = [100, 150, 200, 247.8, 276.1, 520.7, 708.6, 896.5, 1003.8, 1102.3, 1164.9]
mpkv0p50 =  [250, 419.4, 514.9, 646.3, 711.9, 911.9, 1103.0, 1314.9, 1452.2, 1535.8, 1601.5] 
mpkv0p75 = [445.4, 693.5, 818.9, 902.5, 956.3, 1168.2, 1377.0, 1579.9, 1705.2, 1785.7, 1854.3 ]
mp = [650.4, 873.9, 984.2, 1079.6, 1148.1, 1356.8, 1559.5, 1777.0, 1899.2, 1991.6, 2051.3]  #mutau gl=0

#mp observed
mpkv0p1_obs = [100, 150, 170, 200, 210, 220, 250, 371.6, 461.0, 678.7, 807.0]
mpkv0p25_obs = [80, 100, 150, 200, 250, 508.8, 875.6, 1087.4, 1209.6, 1284.2, 1349.8]
mpkv0p50_obs = [200, 338.8, 446.3, 816.4, 894.0, 1088.1, 1279.1, 1488.1, 1610.4, 1688.1, 1756.7]
mpkv0p75_obs = [361.4, 884.9, 1007.3, 1084.9, 1153.5, 1347.5, 1535.4, 1738.2, 1866.5, 1947.0, 2021.6]
mp_obs = [844.1, 1061.6, 1183.9, 1276.3, 1326.9, 1532.6, 1735.3, 1940.9, 2060.2, 2149.6, 2224.1 ]


mp0p1_error1 = [150,150,150,150,150,150,365.6, 487.9, 616.1, 693.6, 741.4] #-1 sigma 
mp0p1_error2 = [150,150,150,150,150,150,200, 371.6, 443.2, 487.8, 553.5]    #+1 sigma

mp0p25_error1 = [156, 206, 256.9, 323.8, 416.3, 625.1, 801.0, 988.9, 1132.1, 1218.6, 1284.2 ] #-1 sigma 
mp0p25_error2 = [80, 100, 150, 200, 250.7, 431.2, 628.1, 789.1, 902.4, 980.0, 1036.6]    #+1 sigma

mp0p5_error1 = [326.8, 497.0, 670.1, 747.8, 819.4, 1004.5, 1222.4, 1449.3, 1574.6, 1652.2, 1714.9 ] #-1 sigma 
mp0p5_error2 = [200, 338.8, 446.3, 500.0, 607.4, 810.4, 983.5, 1183.6, 1309, 1407.5, 1473.1]    #+1 sigma

mp0p75_error1 = [550.2, 813.1, 926.6, 1001.2, 1075.8, 1287.7, 1493.6, 1702.4, 1830.6, 1914.1, 1988.7] #-1 sigma 
mp0p75_error2 = [364.4, 558.9, 705.3, 791.9, 860.6, 1048.6, 1242.6, 1451.4, 1573.7, 1657.3, 1722.9]    #+1 sigma

mp_error1 = [769.6, 981.2, 1112.4, 1207.7,1270.3, 1481.9, 1690.6, 1902.2, 2027.4, 2116.8, 2185.4  ] #-1 sigma
mp_error2 = [501.3, 763.6, 885.8, 963.3, 1019.9, 1231.6, 1434.2, 1648.9, 1768.1, 1854.5, 1923.1] #+1 sigma



c1 = TCanvas( 'c1', 'Dynamic Filling Example',347,180,1500,800)
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
c1.SetLeftMargin(0.09)
c1.SetRightMargin(0.30)
c1.SetBottomMargin(0.125)
c1.SetTopMargin(0.12)
c1.SetFrameBorderMode(0)
c1.SetFrameBorderMode(0)

c1.cd()
frame = c1.DrawFrame(2000.4,0.001, 2400.1, 10)
def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    hpxpy  = TH2F( 'hpxpy', '',10 , 250, 2750.,12,0.,1.2  )
    N_kv = len(kv)
    mg = TMultiGraph()
    gr_kv0p1 = TGraph(N_kv)
    gr_kv0p25 = TGraph(N_kv)
    gr_kv0p50 = TGraph(N_kv)
    gr_kv0p75 = TGraph(N_kv)
    gr_kv1p0 = TGraph(N_kv)

    grkv0p1_error = TGraph(2*N_kv)
    grkv0p25_error = TGraph(2*N_kv)
    grkv0p50_error = TGraph(2*N_kv)
    grkv0p75_error = TGraph(2*N_kv)
    grkv1p0_error = TGraph(2*N_kv)


    gr_kv0p1_obs = TGraph(N_kv) 
    gr_kv0p25_obs = TGraph(N_kv) 
    gr_kv0p50_obs = TGraph(N_kv) 
    gr_kv0p75_obs = TGraph(N_kv) 
    gr_kv1p0_obs = TGraph(N_kv) 
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
        gr_kv0p1.SetPoint(j,mpkv0p1[j],kv[j]) # median
        gr_kv0p25.SetPoint(j,mpkv0p25[j],kv[j]) # median
        gr_kv0p50.SetPoint(j,mpkv0p50[j],kv[j]) # median
        gr_kv0p75.SetPoint(j,mpkv0p75[j],kv[j]) # median
        gr_kv1p0.SetPoint(j,mp[j],kv[j]) # median
#	gr.SetPointError(j,mp[j]-mp_error2[j],0.05)
	

        gr_kv0p1_obs.SetPoint(j,mpkv0p1_obs[j],kv[j]) 
        gr_kv0p25_obs.SetPoint(j,mpkv0p25_obs[j],kv[j]) 
        gr_kv0p50_obs.SetPoint(j,mpkv0p50_obs[j],kv[j]) 
        gr_kv0p75_obs.SetPoint(j,mpkv0p75_obs[j],kv[j]) 
        gr_kv1p0_obs.SetPoint(j,mp_obs[j],kv[j]) 


#
#
	grkv0p1_error.SetPoint(2*N_kv-1-j,mp0p1_error1[j],kv[j])
	grkv0p1_error.SetPoint(j,mp0p1_error2[j],kv[j])

	grkv0p25_error.SetPoint(2*N_kv-1-j,mp0p25_error1[j],kv[j])
	grkv0p25_error.SetPoint(j,mp0p25_error2[j],kv[j])

	grkv0p50_error.SetPoint(2*N_kv-1-j,mp0p5_error1[j],kv[j])
	grkv0p50_error.SetPoint(j,mp0p5_error2[j],kv[j])

	grkv0p75_error.SetPoint(2*N_kv-1-j,mp0p75_error1[j],kv[j])
	grkv0p75_error.SetPoint(j,mp0p75_error2[j],kv[j])

	grkv1p0_error.SetPoint(2*N_kv-1-j,mp_error1[j],kv[j])
	grkv1p0_error.SetPoint(j,mp_error2[j],kv[j])
#
#
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

    gr_kv0p1.SetLineStyle(2)
    gr_kv0p1.SetLineColor(ROOT.kRed+3)
    gr_kv0p1.SetLineWidth(2)
    gr_kv0p1.SetTitle("")
    gr_kv0p1.SetFillColor(ROOT.kRed-6)
    gr_kv0p1.SetFillStyle(3001)

    gr_kv0p25.SetLineStyle(2)
    gr_kv0p25.SetLineColor(ROOT.kYellow+3)
    gr_kv0p25.SetLineWidth(2)
    gr_kv0p25.SetTitle("")
    gr_kv0p25.SetFillColor(ROOT.kYellow-6)
    gr_kv0p25.SetFillStyle(3001)

    gr_kv0p50.SetLineStyle(2)
    gr_kv0p50.SetLineColor(ROOT.kGreen+3)
    gr_kv0p50.SetLineWidth(2)
    gr_kv0p50.SetTitle("")
    gr_kv0p50.SetFillColor(ROOT.kGreen-6)
    gr_kv0p50.SetFillStyle(3001)

    gr_kv0p75.SetLineStyle(2)
    gr_kv0p75.SetLineColor(ROOT.kMagenta+3)
    gr_kv0p75.SetLineWidth(2)
    gr_kv0p75.SetTitle("")
    gr_kv0p75.SetFillColor(ROOT.kMagenta-6)
    gr_kv0p75.SetFillStyle(3001)

    gr_kv1p0.SetLineStyle(2)
    gr_kv1p0.SetLineColor(ROOT.kBlue+3)
    gr_kv1p0.SetLineWidth(2)
    gr_kv1p0.SetTitle("")
    gr_kv1p0.SetFillColor(ROOT.kBlue-6)
    gr_kv1p0.SetFillStyle(3001)
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



    gr_kv0p1_obs.SetLineStyle(1)
    gr_kv0p1_obs.SetLineColor(ROOT.kRed-4)
    gr_kv0p1_obs.SetLineWidth(3)
  
    gr_kv0p25_obs.SetLineStyle(1)
    gr_kv0p25_obs.SetLineColor(ROOT.kYellow-3)
    gr_kv0p25_obs.SetLineWidth(3)

    gr_kv0p50_obs.SetLineStyle(1)
    gr_kv0p50_obs.SetLineColor(ROOT.kGreen-4)
    gr_kv0p50_obs.SetLineWidth(3)

    gr_kv0p75_obs.SetLineStyle(1)
    gr_kv0p75_obs.SetLineColor(ROOT.kMagenta-4)
    gr_kv0p75_obs.SetLineWidth(3)

    gr_kv1p0_obs.SetLineStyle(1)
    gr_kv1p0_obs.SetLineColor(ROOT.kBlue-4)
    gr_kv1p0_obs.SetLineWidth(3)

 
    grkv0p1_error.SetLineColor(ROOT.kRed-6)
    grkv0p1_error.SetLineStyle(6)
    grkv0p1_error.SetLineWidth(2)
    grkv0p1_error.SetTitle("")
    grkv0p1_error.SetFillColor(ROOT.kRed-6)
    grkv0p1_error.SetFillStyle(3001)


    grkv0p25_error.SetLineColor(ROOT.kYellow-6)
    grkv0p25_error.SetLineStyle(6)
    grkv0p25_error.SetLineWidth(2)
    grkv0p25_error.SetTitle("")
    grkv0p25_error.SetFillColor(ROOT.kYellow-6)
    grkv0p25_error.SetFillStyle(3001)

    grkv0p50_error.SetLineColor(ROOT.kGreen-6)
    grkv0p50_error.SetLineStyle(6)
    grkv0p50_error.SetLineWidth(2)
    grkv0p50_error.SetTitle("")
    grkv0p50_error.SetFillColor(ROOT.kGreen-6)
    grkv0p50_error.SetFillStyle(3001)

    grkv0p75_error.SetLineColor(ROOT.kMagenta-6)
    grkv0p75_error.SetLineStyle(6)
    grkv0p75_error.SetLineWidth(2)
    grkv0p75_error.SetTitle("")
    grkv0p75_error.SetFillColor(ROOT.kMagenta-6)
    grkv0p75_error.SetFillStyle(3001)

    grkv1p0_error.SetLineColor(ROOT.kBlue-6)
    grkv1p0_error.SetLineStyle(6)
    grkv1p0_error.SetLineWidth(2)
    grkv1p0_error.SetTitle("")
    grkv1p0_error.SetFillColor(ROOT.kBlue-6)
    grkv1p0_error.SetFillStyle(3001)

    gr_kv0p1.Draw("AC")
    gr_kv0p25.Draw("C same")
    gr_kv0p50.Draw("C same")
    gr_kv0p75.Draw("C same")
    gr_kv1p0.Draw("C same")
    gr_kv0p1_obs.Draw("C same")
    gr_kv0p25_obs.Draw("C same")
    gr_kv0p50_obs.Draw("C same")
    gr_kv0p75_obs.Draw("C same")
    gr_kv1p0_obs.Draw("Csame")

    grkv0p1_error.Draw("Fsame")
    grkv0p25_error.Draw("Fsame")
    grkv0p50_error.Draw("Fsame")
    grkv0p75_error.Draw("Fsame")
    grkv1p0_error.Draw("Fsame")
    gr_kv0p1.GetXaxis().SetLimits(250.,2500.)
    #gr.GetYaxis().CenterTitle(1)
    gr_kv0p1.GetYaxis().SetLimits(0.,0.9)
    gr_kv0p1.GetYaxis().SetTitleSize(0.06)
    gr_kv0p1.GetYaxis().SetLabelSize(0.05)
    gr_kv0p1.GetYaxis().SetRangeUser(0.,0.9)
    gr_kv0p1.GetYaxis().SetTitle("#it{#Beta}(Z' #rightarrow #tau#tau)")
    gr_kv0p1.GetYaxis().SetTitleOffset(0.6)

    gr_kv0p1.GetXaxis().SetTitle("m_{Z'} [GeV]")
    gr_kv0p1.GetXaxis().SetTitleSize(0.055)
    gr_kv0p1.GetXaxis().SetTitleOffset(1.0)
    gr_kv0p1.GetXaxis().SetLabelSize(0.05)
    c1.Update()


    CMS_lumi.CMS_lumi(c1,4,11)
    ROOT.gPad.SetTicks(1,1)


    #leg = TLegend(0.13,0.80,0.92,0.90)
    #leg_obs = TLegend(0.68,0.75, 0.88,0.91)
    #leg_exp = TLegend(0.13,0.75, 0.92,0.91)
    
    leg = TLegend(0.13,0.80,0.92,0.90)
    leg_obs = TLegend(0.72,0.50, 0.99,0.85)
    leg_exp = TLegend(0.72,0.16, 0.99,0.49)
    
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(3001)
    leg.SetTextFont(42)
    leg.SetTextSize(0.045)

    leg_obs.SetBorderSize(0)
    leg_obs.SetFillColor(0)
    leg_obs.SetFillStyle(0)
    leg_obs.SetTextFont(42)
    leg_obs.SetTextSize(0.045)

    leg_exp.SetBorderSize(0)
    leg_exp.SetFillColor(0)
    leg_exp.SetFillStyle(0)
    leg_exp.SetTextFont(42)
    leg_exp.SetTextSize(0.045)

    leg.SetHeader("VBF Z' #rightarrow #tau#tau (g_{l} = 0, g_{h} = 1)")
    #leg.AddEntry("", "", "")
    #leg.Draw()

    leg_obs.SetHeader("#splitline{VBF Z' #rightarrow #tau#tau (g_{l} = 1, g_{h} = 1)}{Observed}")
    leg_obs.AddEntry(gr_kv0p1_obs, "#kappa_{V} : 0.1", "l")
    leg_obs.AddEntry(gr_kv0p25_obs, "#kappa_{V} : 0.25", "l")
    leg_obs.AddEntry(gr_kv0p50_obs, "#kappa_{V} : 0.50", "l")
    leg_obs.AddEntry(gr_kv0p75_obs, "#kappa_{V} : 0.75", "l")
    leg_obs.AddEntry(gr_kv1p0_obs, "#kappa_{V} : 1.0", "l")
    leg_obs.Draw()

#    leg_exp.SetNColumns(2)
    leg_exp.SetHeader("Expected, median & 68%")
    leg_exp.AddEntry(gr_kv0p1,"#kappa_{V} : 0.1","lf")
    leg_exp.AddEntry(gr_kv0p25,"#kappa_{V} : 0.25","lf")
    leg_exp.AddEntry(gr_kv0p50,"#kappa_{V} : 0.50","lf")
    leg_exp.AddEntry(gr_kv0p75,"#kappa_{V} : 0.75","lf")
    leg_exp.AddEntry(gr_kv1p0,"#kappa_{V} : 1.0","lf")
    leg_exp.Draw()

#    leg_obs.SetNColumns(2)

#    for name in histos:
#        exec('del %sFill' % name)
#    del histos
#     
#    gBenchmark.Show( 'hsimple' )
    
    c1.Modified()
    c1.Update()
    c1.SaveAs("br_2D_tautau_gl1_UpperLimit.pdf")
    c1.SaveAs("br_2D_tautau_gl1_UpperLimit.png")
    c1.SaveAs("br_2D_tautau_gl1_UpperLimit.root")
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

