{
TCanvas *c1= new TCanvas("c1","stacked hists",0,0,600,600);
 c1->Range(0,0,1,1);
 c1->SetLogy();

TH1 *h[3], *hsignal[4], *hstat;
Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 1500};

TFile *f1 = TFile::Open("fakebkg_etau_2018.root");
f1->GetObject("h1",h[0]);

TFile *fstat = TFile::Open("fakebkg_etau_2018.root");
fstat->GetObject("h1",hstat);

TFile *f2 = TFile::Open("ttbar_etau_2018.root");
f2->GetObject("h1",h[1]);

TFile *f3 = TFile::Open("prompt_etau_2018.root");
f3->GetObject("h1",h[2]);

TFile *f4 = TFile::Open("VBF_Zprime_tau_tau_M_1000_gl_0_gh_1_kv_1p0.root");
f4->GetObject("NDiJetCombinations/Electron1Tau1ReconstructableMass",hsignal[0]);

TFile *f5 = TFile::Open("VBF_Zprime_tau_tau_M_1500_gl_0_gh_1_kv_1p0.root");
f5->GetObject("NDiJetCombinations/Electron1Tau1ReconstructableMass",hsignal[1]);

TFile *f6 = TFile::Open("VBF_Zprime_WW_M_750_gl_0_gh_1_kv_1p0.root");
f6->GetObject("NDiJetCombinations/Electron1Tau1ReconstructableMass",hsignal[2]);

TFile *f7 = TFile::Open("VBF_Zprime_WW_M_1250_gl_0_gh_1_kv_1p0.root");
f7->GetObject("NDiJetCombinations/Electron1Tau1ReconstructableMass",hsignal[3]);

h[0]->Scale(0.84/0.90);
hstat->Scale(0.84/0.90);

double lumi = 59700.;
for(int i=0; i<4; i++){
double xsec[4] = {0.1994, 0.02174, 0.8273, 0.06114};
double fac = (xsec[i]*lumi)/(100000);
hsignal[i]->Scale(fac);
}

TH1F *hsig1 = (TH1F*)hsignal[0]->Rebin(12,"hsig1",bins);
TH1F *hsig2 = (TH1F*)hsignal[1]->Rebin(12,"hsig2",bins);
TH1F *hsig3 = (TH1F*)hsignal[2]->Rebin(12,"hsig3",bins);
TH1F *hsig4 = (TH1F*)hsignal[3]->Rebin(12,"hsig4",bins);

THStack *hs = new THStack("hs"," ");
h[0]->SetFillColor(kRed-7);
h[1]->SetFillColor(kGreen-8);
h[2]->SetFillColor(kBlue-8);

h[0]->SetLineColor(kRed-7);
h[1]->SetLineColor(kGreen-8);
h[2]->SetLineColor(kBlue-8);

hsig1->SetLineColor(kAzure-6);
hsig2->SetLineColor(kYellow-6);
hsig3->SetLineColor(kGreen-6);
hsig4->SetLineColor(kOrange-6);

std::cout<<"checked"<<std::endl;
hs->Add(h[2]);
hs->Add(h[1]);
hs->Add(h[0]);


hstat->Add(h[2]);
hstat->Add(h[1]);

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
hs->GetXaxis()->SetTitle("M_{e#tau_{h},MET} [GeV]");
hs->GetXaxis()->SetTitleOffset(1.1);
c1->Update();
c1->Modified();

        double y_legend = hs->GetMaximum() + 320;
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
        TLatex * tex2 = new TLatex(x_pos1,y_legend,"2018, 59.7 fb^{-1} (13 TeV)");
        tex2->SetTextAlign(20);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.0332915);
        tex2->SetLineWidth(2);
        tex2->Draw();

TLegend *legend=new TLegend(0.52,0.65,0.89,0.88);
	//legend->SetHeader("NRecoJet1");
        legend->SetTextSize(0.03);
        legend->AddEntry(h[0],"Fake #tau_{h}","f");
        legend->AddEntry(h[1],"t#bar{t}","f");
	legend->AddEntry(h[2],"Other prompt","f");
	legend->AddEntry(hsig1,"VBF Z' #rightarrow #tau#tau (M1000)","lep");
  	legend->AddEntry(hsig4,"VBF Z' #rightarrow WW (M1250)","lep");
	legend->AddEntry(hstat,"Stat. Uncert.","fp");
	legend->Draw();

c1->SaveAs("bkg_etau_2018.root");
c1->SaveAs("bkg_etau_2018.pdf");
	}
