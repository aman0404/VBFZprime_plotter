{
TCanvas *c1= new TCanvas("c1","stacked hists",0,0,700,700);
 c1->Range(0,0,1,1);
 c1->SetLogy();
 c1->SetRightMargin(0.05);
gPad->SetTickx();
        gPad->SetTicky();

TH1 *h[5], *hsignal[4], *hstat;
Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 1500};

TFile *f1 = TFile::Open("fakebkg_mutau_allyear.root");
f1->GetObject("h1",h[0]);

TFile *fstat = TFile::Open("fakebkg_mutau_allyear.root");
fstat->GetObject("h1",hstat);

TFile *f2 = TFile::Open("ttbar_mutau_allyear.root");
f2->GetObject("h1",h[1]);

TFile *f3 = TFile::Open("prompt_mutau_2016.root");
f3->GetObject("h1",h[2]);

TFile *f31 = TFile::Open("prompt_mutau_2017.root");
f31->GetObject("hist",h[3]);

TFile *f32 = TFile::Open("prompt_mutau_2018.root");
f32->GetObject("hist",h[4]);

TFile *f4 = TFile::Open("VBF_Zprime_tau_tau_M_1000_gl_0_gh_1_kv_1p0.root");
f4->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[0]);

TFile *f5 = TFile::Open("VBF_Zprime_tau_tau_M_1500_gl_0_gh_1_kv_1p0.root");
f5->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[1]);

TFile *f6 = TFile::Open("VBF_Zprime_WW_M_750_gl_0_gh_1_kv_1p0.root");
f6->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[2]);

TFile *f7 = TFile::Open("VBF_Zprime_WW_M_1250_gl_0_gh_1_kv_1p0.root");
f7->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[3]);

h[2]->Add(h[3]);
h[2]->Add(h[4]);


double lumi = 13700.;
for(int i=0; i<4; i++){
double xsec[4] = {0.1994, 0.02174, 0.8273, 0.06114};
double fac = (2*xsec[i]*lumi)/(100000);
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
hsig4->SetLineColor(kMagenta);

hsig1->SetLineStyle(2);
hsig4->SetLineStyle(2);

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
hstat->SetLineWidth(2);
hsig1->SetLineWidth(2);
hsig4->SetLineWidth(2);
   hstat->SetFillColor(1);
   hstat->SetFillStyle(3002);
//hs->GetYaxis()->SetTitle("Events");
hs->SetTitle("; m_{rec}(#mu, #tau, #Delta p_{T}) [GeV]  ; Events");
hs->GetXaxis()->SetTitleOffset(1.1);
hs->GetXaxis()->SetTitleSize(0.042);

hs->GetYaxis()->SetTitleOffset(1.1);
hs->GetYaxis()->SetTitleSize(0.042);

//hs->GetXaxis()->SetLabelOffset(1.1);
hs->GetXaxis()->SetLabelSize(0.042);

//hs->GetYaxis()->SetLabelOffset(1.1);
hs->GetYaxis()->SetLabelSize(0.042);
hs->SetMaximum(1e4);
hs->SetMinimum(0.25);

c1->Update();
c1->Modified();

        double y_legend = 20000;
        TLatex *   tex = new TLatex(200,y_legend,"CMS");
//      TLatex *   tex = new TLatex(105,400,"CMS");
     tex->SetTextAlign(20);
   tex->SetTextSize(0.06);
   tex->SetLineWidth(2);
        tex->Draw();
        TLatex *   tex1 = new TLatex(465,y_legend,"#it{#bf{Preliminary}}");
   tex1->SetTextAlign(20);
   tex1->SetTextSize(0.04);

   tex1->SetLineWidth(2);
   tex1->Draw();

        TLatex * tex2 = new TLatex(1220,y_legend,"137.1 fb^{-1} (13 TeV)");
        tex2->SetTextAlign(20);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.04);
        tex2->SetLineWidth(2);
        tex2->Draw();

TLegend *legend=new TLegend(0.42,0.63,0.92,0.88);
	//legend->SetHeader("NRecoJet1");
        legend->SetTextSize(0.04);
        legend->AddEntry(h[0],"Fake #tau_{h}","f");
        legend->AddEntry(h[1],"t#bar{t}","f");
	legend->AddEntry(h[2],"Other prompt","f");
	legend->AddEntry(hsig1,"VBF Z' #rightarrow #tau#tau (M1000)","lep");
  	legend->AddEntry(hsig4,"VBF Z' #rightarrow WW (M1250)","lep");
	legend->AddEntry(hstat,"Stat. Uncert.","fp");
	legend->Draw();

//c1->SaveAs("bkg_mutau_2016.root");
//c1->SaveAs("bkg_mutau_2016.pdf");
	}
