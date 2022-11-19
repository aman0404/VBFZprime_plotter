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

mpkv0p1 = [100, 150, 170, 200, 210, 220, 250, 386.5, 467.0, 559.5, 660.9]
mpkv0p25 = [0.1, 10, 20, 40, 80, 120, 160, 200, 250, 291.1, 381.3 ]
mpkv0p50 =  [100, 130, 160, 180, 210,230, 252.3, 413.3, 490.8, 657.9,747.4] 
mpkv0p75 = [110, 150, 180, 220, 260, 294.0, 428.2, 631.0, 801.0, 935.3, 1012.8]
mp = [100, 150, 200, 230, 264.2, 398.4, 532.6, 798.1, 962.1, 1063.5, 1138.1]  #mutau gl=0

#mp observed
mpkv0p1_obs = [100, 150, 170, 200, 210, 220, 250, 391.6, 481.3, 783.8, 923.9]
mpkv0p25_obs = [0.1, 10, 20, 40, 80, 150, 200, 250, 300, 350, 439.9]
mpkv0p50_obs = [110, 130, 150, 170, 190, 220, 252.3, 359.6, 833.8, 938.2, 1009.8]
mpkv0p75_obs = [100, 130, 160, 200, 250, 279.1, 365.6, 902.4, 1057.5, 1138.1, 1191.7]
mp_obs = [100, 150, 170, 190, 240, 311.9, 416.3, 1006.8, 1173.8, 1272.3, 1346.8 ]


mp0p1_error1 = [150,150,150,150,150,150,150,452.1, 604.2, 699.6, 774.20] #-1 sigma 
mp0p1_error2 = [150,150,150,150,150,150,150, 297.0, 407.4, 464.0, 499.8]    #+1 sigma

mp0p25_error1 = [10, 20, 40, 80, 120, 160, 200, 250, 300, 419.1, 475.6] #-1 sigma 
mp0p25_error2 = [0.1, 0.5, 10, 20, 40, 80, 120, 160, 190, 220, 260]    #+1 sigma

mp0p5_error1 = [130, 160, 170, 210, 250, 279, 344.7, 478.9, 702.6, 839.8, 941.2] #-1 sigma 
mp0p5_error2 = [80, 100, 130, 160, 170, 210, 280, 359.6, 428.2, 484.9, 586.3]    #+1 sigma

mp0p75_error1 = [150, 180, 220, 260, 308, 362.6, 484.9, 762.3, 979.9, 1081.4, 1144.0] #-1 sigma 
mp0p75_error2 = [80, 110, 150, 180, 220, 260, 365.6, 487.9, 654.9, 747.4, 863.7]    #+1 sigma

mp_error1 = [150, 200, 240, 282.1, 332.8, 452.1, 681.7, 956.1, 1105.3, 1197.7, 1281.2] #-1 sigma
mp_error2 = [ 80, 100, 160, 200, 220, 338.8, 458.1, 672.8, 821.9, 929.3, 1000.8] #+1 sigma



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

    #gr_kv0p1.Draw("AC")
    gr_kv0p25.Draw("AC")
    gr_kv0p50.Draw("C same")
    gr_kv0p75.Draw("C same")
    gr_kv1p0.Draw("C same")
    #gr_kv0p1_obs.Draw("C same")
    #gr_kv0p25_obs.Draw("C same")
    gr_kv0p50_obs.Draw("C same")
    gr_kv0p75_obs.Draw("C same")
    gr_kv1p0_obs.Draw("Csame")

#    grkv0p1_error.Draw("Fsame")
    grkv0p25_error.Draw("Fsame")
    grkv0p50_error.Draw("Fsame")
    grkv0p75_error.Draw("Fsame")
    grkv1p0_error.Draw("Fsame")
    gr_kv0p25.GetXaxis().SetLimits(250.,2500.)
    #gr.GetYaxis().CenterTitle(1)
    gr_kv0p25.GetYaxis().SetLimits(0.,0.9)
    gr_kv0p25.GetYaxis().SetTitleSize(0.06)
    gr_kv0p25.GetYaxis().SetLabelSize(0.05)
    gr_kv0p25.GetYaxis().SetRangeUser(0.,0.9)
    gr_kv0p25.GetYaxis().SetTitle("#it{#Beta}(Z' #rightarrow WW)")
    gr_kv0p25.GetYaxis().SetTitleOffset(0.6)

    gr_kv0p25.GetXaxis().SetTitle("m_{Z'} [GeV]")
    gr_kv0p25.GetXaxis().SetTitleSize(0.055)
    gr_kv0p25.GetXaxis().SetTitleOffset(1.0)
    gr_kv0p25.GetXaxis().SetLabelSize(0.05)
    c1.Update()


    CMS_lumi.CMS_lumi(c1,4,11)
    ROOT.gPad.SetTicks(1,1)


    #leg = TLegend(0.13,0.80,0.92,0.90)
    #leg_obs = TLegend(0.68,0.75, 0.88,0.91)
    #leg_exp = TLegend(0.13,0.75, 0.92,0.91)
    
    leg = TLegend(0.13,0.80,0.92,0.90)
    leg_obs = TLegend(0.70,0.50, 0.99,0.85)
    leg_exp = TLegend(0.70,0.16, 0.99,0.49)
    
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

    leg.SetHeader("VBF Z' #rightarrow WW (g_{l} = 0, g_{h} = 1)")
    #leg.AddEntry("", "", "")
    #leg.Draw()

    leg_obs.SetHeader("#splitline{VBF Z' #rightarrow WW (g_{l} = 1, g_{h} = 1)}{Observed}")
#    leg_obs.AddEntry(gr_kv0p1_obs, "#kappa_{V} : 0.1", "l")
#    leg_obs.AddEntry(gr_kv0p25_obs, "#kappa_{V} : 0.25", "l")
    leg_obs.AddEntry(gr_kv0p50_obs, "#kappa_{V} : 0.50", "l")
    leg_obs.AddEntry(gr_kv0p75_obs, "#kappa_{V} : 0.75", "l")
    leg_obs.AddEntry(gr_kv1p0_obs, "#kappa_{V} : 1.0", "l")
    leg_obs.Draw()

#    leg_exp.SetNColumns(2)
    leg_exp.SetHeader("Expected, median & 68%")
#    leg_exp.AddEntry(gr_kv0p1,"#kappa_{V} : 0.1","lf")
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
    c1.SaveAs("br_2D_WW_gl1_UpperLimit.pdf")
    c1.SaveAs("br_2D_WW_gl1_UpperLimit.png")
    c1.SaveAs("br_2D_WW_gl1_UpperLimit.root")
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

