import ROOT
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
import CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
import sys

bratio = 0.20
coupling = sys.argv[1]
value_xsec = 0.01 #default value of x-section for signal	
fac = float(bratio)*float(coupling)*float(coupling)

print(fac)
points = [250, 500, 750, 1000, 1250, 1500,1750, 2000, 2250, 2500, 2750, 3000]
xsec = [119.2, 5.365, 0.8273, 0.1994, 0.06114, 0.02174, 0.008568, 0.003596, 0.001609, 0.0007504, 0.0007504,0.0007504]
def executeCards(points):
    mass = len(points)
    for j in range(mass):
        #file_name = "VBF_M"+str(points[j])+".txt" 
        file_name = "VBF_2016_mutau_M"+str(points[j])+".txt" 
        combine_command = "combine -M AsymptoticLimits -m %s %s" % (points[j], file_name)
        print(">>> " + combine_command)
        p = subprocess.Popen(combine_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line.rstrip("\n")
            print(">>>   higgsCombine_M"+str(points[j])+"_AsymptoticLimits.root created")
            retval = p.wait()

#get limits from root file


def getLimits(file_name):
	file = TFile(file_name)
    	tree = file.Get("limit")
 
    	limits = [ ]
    	for quantile in tree:
            limits.append(value_xsec*tree.limit)
            print ">>>   %.2f" % limits[-1]
 
    	return limits[:6]

#plot limits

def plotUpperLimits(file_name):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
 
    N = len(points)
    yellow = TGraph(2*N)    # yellow band
    green = TGraph(2*N)     # green band
    median = TGraph(N)      # median line
    theo_line = TGraph(N)      # median line 
    theo_p1sig = TGraph(N)
    theo_m1sig = TGraph(N)

    up2s = [ ]
    for i in range(N):
        file_name = "higgsCombine.Test.AsymptoticLimits.mH"+str(points[i])+".root" 
        limit = getLimits(file_name)
        up2s.append(limit[4])
        yellow.SetPoint(    i,    points[i], limit[4] ) # + 2 sigma
        green.SetPoint(     i,    points[i], limit[3] ) # + 1 sigma
        median.SetPoint(    i,    points[i], limit[2] ) # median
        green.SetPoint(  2*N-1-i, points[i], limit[1] ) # - 1 sigma
        yellow.SetPoint( 2*N-1-i, points[i], limit[0] ) # - 2 sigma
	theo_line.SetPoint( i,    points[i], fac*xsec[i]) 
	theo_p1sig.SetPoint( i,    points[i],fac*xsec[i]+0.021*fac*xsec[i])
	theo_m1sig.SetPoint( i,    points[i],fac*xsec[i]-0.021*fac*xsec[i])
   	print(xsec[i])
	print(xsec[i]+0.021*xsec[i]) 
    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = TCanvas("c","c",100,100,W,H)
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetLogy()
#    c.SetGrid()
    c.cd()
    frame = c.DrawFrame(2000.4,0.001, 2400.1, 10)
    
#    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(0.9)
    frame.GetXaxis().SetNdivisions(508)
#    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitle("#sigma #times B [pb]")
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    frame.GetXaxis().SetTitle("m_{Z'} [GeV]")
    frame.SetMinimum(0.00001)
#    frame.SetMaximum(max(up2s)*1.05)
    frame.SetMaximum(max(up2s)*6.05)
#    frame.GetXaxis().SetLimits(min(points),max(points))
    frame.GetXaxis().SetLimits(min(points),2500.)
    yellow.SetFillColor(ROOT.kOrange)
    yellow.SetLineColor(ROOT.kOrange)
    yellow.SetFillStyle(1001)
    yellow.Draw('CF')
 
    green.SetFillColor(ROOT.kGreen+1)
    green.SetLineColor(ROOT.kGreen+1)
    green.SetFillStyle(1001)
    green.Draw('CFsame')
 
    median.SetLineColor(1)
    median.SetLineWidth(2)
    median.SetLineStyle(2)
    median.Draw('Csame')
 
    theo_line.SetLineColor(2)
    theo_line.SetLineWidth(2)
    theo_line.SetLineStyle(2)
    theo_line.Draw('Lsame')

    theo_p1sig.SetLineColor(2)
    theo_p1sig.SetLineWidth(2)
    theo_p1sig.SetLineStyle(2)
    theo_p1sig.Draw('Lsame')

    theo_m1sig.SetLineColor(2)
    theo_m1sig.SetLineWidth(2)
    theo_m1sig.SetLineStyle(2)
    theo_m1sig.Draw('Lsame')

    CMS_lumi.CMS_lumi(c,14,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')
 
    x1 = 0.52
#    x1 = 0.62
    x2 = x1 + 0.25
    y2 = 0.86
    y1 = 0.66
    legend = TLegend(x1,y1,x2,y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.041)
    legend.SetTextFont(42)
    legend.SetHeader("95% CL limits")
    legend.AddEntry(median, "Expected",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
    #legend.AddEntry(theo_line, "VBF Z' #rightarrow WW (BF=0.20)",'LEP')
    legend.AddEntry(theo_line, "VBF Z' #rightarrow #tau#tau (BF=0.20)",'LEP')
#    legend.AddEntry(theo_line, "VBF Z' #rightarrow #tau#tau #rightarrow e#mu (BF=0.20)",'LEP')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 2 std. deviation",'f')
    legend.Draw()
 
    print " "
    c.SaveAs("all_kv1p0_gl0_UpperLimit.png")
    c.SaveAs("all_kv1p0_gl0_UpperLimit.root")
    c.SaveAs("all_kv1p0_gl0_UpperLimit.pdf")
    c.Close()

def main():
#	executeCards(points)
	plotUpperLimits(points)

if __name__ == '__main__':
    main()
