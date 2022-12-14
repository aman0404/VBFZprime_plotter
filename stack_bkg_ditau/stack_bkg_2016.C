{
TCanvas *c1= new TCanvas("c1","stacked hists",0,0,600,600);
 c1->Range(0,0,1,1);
 c1->SetLogy();

TH1 *h[5], *hsignal[4],*h1, *hstat;
//Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 1500};
Double_t bins[11] = {100,150,200,250,300,350,400,500,650,850, 1500};

TFile *f1 = TFile::Open("2016bkg/DY_ditau_2016.root");
f1->GetObject("h1",h[0]);

TFile *fstat = TFile::Open("2016bkg/DY_ditau_2016.root");
fstat->GetObject("h1",hstat);

TFile *f2 = TFile::Open("2016bkg/W_ditau_2016.root");
f2->GetObject("h1",h[1]);

TFile *f3 = TFile::Open("2016bkg/QCD_ditau_2016.root");
f3->GetObject("h1",h[2]);


TFile *f4 = TFile::Open("2016bkg/SingleTop_ditau_2016.root");
f4->GetObject("h1",h[3]);

TFile *f5 = TFile::Open("2016bkg/VV_ditau_2016.root");
f5->GetObject("h1",h[4]);


TFile *f41 = TFile::Open("VBF_Zprime_tau_tau_M_1000_gl_0_gh_1_kv_1p0.root");
f41->GetObject("NRecoBJet/DiTauReconstructableMass",hsignal[0]);

TFile *f51 = TFile::Open("VBF_Zprime_tau_tau_M_1500_gl_0_gh_1_kv_1p0.root");
f51->GetObject("NRecoBJet/DiTauReconstructableMass",hsignal[1]);

TFile *f61 = TFile::Open("VBF_Zprime_WW_M_750_gl_0_gh_1_kv_1p0.root");
f61->GetObject("NRecoBJet/DiTauReconstructableMass",hsignal[2]);

TFile *f71 = TFile::Open("VBF_Zprime_WW_M_1250_gl_0_gh_1_kv_1p0.root");
f71->GetObject("NRecoBJet/DiTauReconstructableMass",hsignal[3]);


for(int i=0; i<4; i++){
double xsec[4] = {0.1994, 0.02174, 0.8273, 0.06114};
double fac = (xsec[i]*35900)/(100000);
hsignal[i]->Scale(fac);
}

TH1F *hsig1 = (TH1F*)hsignal[0]->Rebin(10,"hsig1",bins);
TH1F *hsig2 = (TH1F*)hsignal[1]->Rebin(10,"hsig2",bins);
TH1F *hsig3 = (TH1F*)hsignal[2]->Rebin(10,"hsig3",bins);
TH1F *hsig4 = (TH1F*)hsignal[3]->Rebin(10,"hsig4",bins);

THStack *hs = new THStack("hs"," ");
h[0]->SetFillColor(kRed-7);
h[1]->SetFillColor(kGreen-8);
h[2]->SetFillColor(kBlue-8);
h[3]->SetFillColor(kOrange-8);
h[4]->SetFillColor(kYellow-8);


h[0]->SetLineColor(kRed-7);
h[1]->SetLineColor(kGreen-8);
h[2]->SetLineColor(kBlue-8);
h[3]->SetLineColor(kOrange-8);
h[4]->SetLineColor(kYellow-8);

hsig1->SetLineColor(kAzure-6);
hsig2->SetLineColor(kYellow-6);
hsig3->SetLineColor(kGreen-6);
hsig4->SetLineColor(kOrange-6);

std::cout<<"checked"<<std::endl;
hs->Add(h[4]);
hs->Add(h[3]);
hs->Add(h[2]);
hs->Add(h[1]);
hs->Add(h[0]);


hstat->Add(h[2]);
hstat->Add(h[1]);
hstat->Add(h[3]);
hstat->Add(h[4]);

std::cout<<hstat->Integral()<<'\t'<<h[0]->Integral()<<'\t'<<h[1]->Integral()<<'\t'<<h[2]->Integral()<<std::endl;
hs->Draw("hist");
hsig1->Draw("ep,same");
//hsig2->Draw("ep,same");
//hsig3->Draw("ep,same");
hsig4->Draw("ep,same");
hstat->Draw("E2,same");
hstat->SetLineWidth(1);
   hstat->SetFillColor(1);
   hstat->SetFillStyle(3002);
hs->GetYaxis()->SetTitle("Events");
hs->GetXaxis()->SetTitle("M_{#tau_{h}#tau_{h},MET} [GeV]");
hs->GetXaxis()->SetTitleOffset(1.1);
hs->GetYaxis()->SetRangeUser(0.05,20);
hs->SetMinimum(0.5);
hs->SetMaximum(40);
c1->Update();
c1->Modified();

        double y_legend = hs->GetMaximum() + 45;
        double x_legend = 170;
        TLatex *   tex = new TLatex(x_legend,y_legend,"CMS");
//      TLatex *   tex = new TLatex(105,400,"CMS");
     tex->SetTextAlign(20);
   tex->SetTextSize(0.0512915);
   tex->SetLineWidth(2);
        tex->Draw();
        TLatex *   tex1 = new TLatex(x_legend+220,y_legend,"#it{#bf{Preliminary}}");
   tex1->SetTextAlign(20);
   tex1->SetTextSize(0.03042526);

   tex1->SetLineWidth(2);
   tex1->Draw();

        double x_pos1 = x_legend+1050;
        TLatex * tex2 = new TLatex(x_pos1,y_legend,"2016, 35.9 fb^{-1} (13 TeV)");
        tex2->SetTextAlign(20);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.0332915);
        tex2->SetLineWidth(2);
        tex2->Draw();

TLegend *legend=new TLegend(0.52,0.60,0.89,0.88);
	//legend->SetHeader("NRecoJet1");
        legend->SetTextSize(0.03);
        legend->AddEntry(h[0],"DY+Jets","f");
        legend->AddEntry(h[1],"W+Jets","f");
	legend->AddEntry(h[2],"QCD","f");
	legend->AddEntry(h[3],"Single Top","f");
	legend->AddEntry(h[4],"VV","f");
	legend->AddEntry(hsig1,"VBF Z' #rightarrow #tau#tau (M1000)","lep");
  	legend->AddEntry(hsig4,"VBF Z' #rightarrow WW (M1250)","lep");
	legend->AddEntry(hstat,"Stat. Uncert.","fp");
	legend->Draw();

c1->SaveAs("bkg_ditau_2016.root");
c1->SaveAs("bkg_ditau_2016.pdf");
	}
