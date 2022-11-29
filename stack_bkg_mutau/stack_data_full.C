{
TCanvas *c1= new TCanvas("c1","stacked hists",0,0,900,900);
   c1->SetHighLightColor(2);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(3);
   c1->SetLeftMargin(0.08);
   c1->SetRightMargin(0.05);
   c1->SetTopMargin(0.05);
   c1->SetFrameBorderMode(0);


TH1 *h0[3], *hsignal[2], *h0stat, *hdata;
//TH1 *h[3], *hsignal[4], *hstat, *hdata;
//Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550, 650, 1000,1500};
Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 4000}; //final

//Double_t bins[15] = {100,150,200,250,300,350,400,450,500,550,650,850, 1000, 1200, 4000};

TFile *f1 = TFile::Open("faketau_mutau_all.root");
f1->GetObject("h1",h0[0]);

TFile *fstat = TFile::Open("faketau_mutau_all.root");
fstat->GetObject("h1",h0stat);

TFile *f2 = TFile::Open("ttbar_mutau_all.root");
f2->GetObject("h1",h0[1]);

TFile *f3 = TFile::Open("prompt_mutau_all.root");
f3->GetObject("h1",h0[2]);

//TFile *fdata = TFile::Open("allData.root");
TFile *fdata = TFile::Open("20percent_data/allData.root");
fdata->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hdata);

TFile *f4 = TFile::Open("VBF_Zprime_tau_tau_M_1500_gl_0_gh_1_kv_1p0.root");
f4->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[0]);

TFile *f5 = TFile::Open("VBF_Zprime_WW_M_1500_gl_0_gh_1_kv_1p0.root");
f5->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[1]);
//
//TFile *f6 = TFile::Open("VBF_Zprime_WW_M_750_gl_0_gh_1_kv_1p0.root");
//f6->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[2]);
//
//TFile *f7 = TFile::Open("VBF_Zprime_WW_M_1250_gl_0_gh_1_kv_1p0.root");
//f7->GetObject("NDiJetCombinations/Muon1Tau1ReconstructableMass",hsignal[3]);
//
//
double lumi = 27.42;
for(int i=0; i<2; i++){
double xsec[2] = {0.02174, 0.021740000};
double fac = (1500*xsec[i]*lumi)/(100000);
hsignal[i]->Scale(fac);
}

TH1F *hsig1 = (TH1F*)hsignal[0]->Rebin(12,"hsig1",bins);
TH1F *hsig2 = (TH1F*)hsignal[1]->Rebin(12,"hsig2",bins);
//TH1F *hsig3 = (TH1F*)hsignal[2]->Rebin(12,"hsig3",bins);
//TH1F *hsig4 = (TH1F*)hsignal[3]->Rebin(12,"hsig4",bins);

TH1 *h[3];
for(int i=0; i<3; i++){
h[i] = (TH1F*)h0[i]->Rebin(12,"hdata",bins);
}
TH1F *hstat = (TH1F*)h0stat->Rebin(12,"hdata",bins);

TH1F *hdata_rebin = (TH1F*)hdata->Rebin(12,"hdata",bins);
//
//for(int i = 1; i<14; i++){
//if(hdata_rebin->GetBinContent(i)==0.){
//hdata_rebin->SetBinContent(i,0.01);
//hdata_rebin->SetBinError(i,0.01);
//}
//}
//h[0]->Sumw2();
//h[1]->Sumw2();
//h[2]->Sumw2();

h[0]->Scale(0.20);
h[1]->Scale(0.20);
h[2]->Scale(0.20);
hstat->Scale(0.20);

double error1;
double error2;
double error3;
std::cout<<"data "<<hdata_rebin->Integral()<<std::endl;
std::cout<<"fake "<<h[0]->IntegralAndError(1,13,error1)<< " error "<<error1<<std::endl;
std::cout<<"ttba "<<h[1]->IntegralAndError(1,13,error2)<< " error "<<error2<<std::endl;
std::cout<<"prom "<<h[2]->IntegralAndError(1,13,error3)<< " error "<<error3<<std::endl;

//std::cout<<h0[0]->GetBinError(2)<<std::endl;

THStack *hs = new THStack("hs"," ");
h[0]->SetFillColor(kRed-7);
h[1]->SetFillColor(kGreen-8);
h[2]->SetFillColor(kBlue-8);

h[0]->SetLineColor(kRed-7);
h[1]->SetLineColor(kGreen-8);
h[2]->SetLineColor(kBlue-8);

hsig1->SetLineColor(kAzure-6);
hsig2->SetLineColor(kMagenta);
//hsig3->SetLineColor(kGreen-6);
//hsig4->SetLineColor(kOrange-6);
hsig1->SetLineStyle(2);
hsig2->SetLineStyle(2);
hsig1->SetLineWidth(2);
hsig2->SetLineWidth(2);

hdata_rebin->SetLineWidth(2);
hdata_rebin->SetLineColor(kBlack);
hdata_rebin->SetMarkerColor(kBlack);
hdata_rebin->SetMarkerStyle(20);
hdata_rebin->SetMarkerSize(1.4);


//std::cout<<"checked"<<std::endl;
hs->Add(h[2]);
hs->Add(h[1]);
hs->Add(h[0]);


hstat->Add(h[2]);
hstat->Add(h[1]);

lumi = 0.025;
Trig210 = 0.03;
PU18 = 0.05;
TES = 0.02;
ELID18 = 0.02;
TAUID18 = 0.04;
JER = 0.05;
double JEC[13] = {0.05, 0.05,0.05451, 0.09507, 0.03421, 0.04966, 0.05554, 0.05614, 0.05089, 0.03457, 0.0522, 0.05195, 0.07742};
double wfake[13] = {0.02868, 0.02868, 0.02932, 0.04441, 0.05668, 0.07095, 0.08822, 0.08433, 0.07264 ,0.04332, 0.00655, 0.11886, 0.28847};

double e_sys = pow(TES,2) + pow(lumi,2) + pow(Trig210,2) + pow(PU18,2) + pow(ELID18,2) + pow(TAUID18,2)  + pow(JER,2);
double sys = sqrt(e_sys);


TPad *pad1 = new TPad("pad1", "pad1",0.0,0.0,1,0.33);

  pad1->SetTickx();
  pad1->SetTicky();
  pad1->Draw();
  pad1->cd();
//  pad1->Range(61.49425,-1.281439,167.8161,2.98999);
  pad1->SetFillColor(0);
  pad1->SetBorderMode(-1);
  pad1->SetBorderSize(5);
  pad1->SetLeftMargin(0.12);
  pad1->SetRightMargin(0.04);
  pad1->SetTopMargin(0.02);
  pad1->SetBottomMargin(0.4);
  pad1->SetFrameBorderMode(0);
  pad1->SetFrameBorderMode(0);




  // pad1->Draw();
  // pad1->cd();
  // pad1->Range(-49.46043,-0.4895868,524.2806,1.328879);
  // pad1->SetFillColor(0);
  // pad1->SetBorderMode(0);
  // pad1->SetBorderSize(2);
  // pad1->SetGridx();
  // pad1->SetLeftMargin(0.0862069);
  // pad1->SetRightMargin(0.04231974);
  // pad1->SetTopMargin(0.00961554);
  // pad1->SetBottomMargin(0.2692307);
  // pad1->SetFrameBorderMode(0);
  // pad1->SetFrameBorderMode(0);

        TH1F *htotal_bkg = (TH1F*)h[0]->Clone("htotal_bkg");
        htotal_bkg->Add(h[1]);
        htotal_bkg->Add(h[2]);

        TH1F *htotal_data = (TH1F*)hdata_rebin->Clone("htotal_data");

        htotal_data->Divide(htotal_bkg);

//      TH1F *hdiv1_error = (TH1F*)htotal_bkg->Clone("hdiv1_error");
        //TH1F *hdiv1_error = (TH1F*)htotal_data->Clone("hdiv1_error");
                TH1* hdiv1_error = new TH1F("hdiv1_error", " ",12,bins);
                TH1* hdiv2_error = new TH1F("hdiv2_error", " ",12,bins);
                for(int i=1; i<13; i++)
                {
                hdiv1_error->SetBinContent(i,1);
                double deno_err = h[0]->GetBinContent(i) + h[1]->GetBinContent(i)  + h[2]->GetBinContent(i) ;
                double value = sqrt((pow(h[0]->GetBinError(i),2))+ (pow(h[1]->GetBinError(i),2)) + (pow(h[2]->GetBinError(i),2)));
		double total_err = sqrt(pow(sys,2) + pow(value/deno_err,2) + pow(JEC[i], 2) + pow(wfake[i],2));
//                std::cout<<i<<'\t'<<total_err<<'\t'<<value/deno_err<<std::endl;
                hdiv1_error->SetBinError(i,total_err);
                }
        htotal_data->Draw("EP");
        hdiv1_error->SetStats(kFALSE);
ci = TColor::GetColor("#cc00cc");
hdiv1_error->SetFillColor(ci);
hdiv1_error->SetFillStyle(3004);
hdiv1_error->Draw("E2,same");

htotal_data->SetStats(kFALSE);
htotal_data->SetTitle("");
htotal_data->SetMarkerStyle(20);
htotal_data->SetMarkerSize(1.4);
htotal_data->GetYaxis()->SetNdivisions(20505);
htotal_data->GetYaxis()->SetLabelFont(42);
htotal_data->GetYaxis()->SetLabelSize(0.12);
htotal_data->GetYaxis()->SetTitleSize(0.12);
htotal_data->GetYaxis()->SetTitleOffset(0.45);
htotal_data->GetYaxis()->SetTitleFont(42);
htotal_data->SetLineColor(kBlack);
htotal_data->SetLineWidth(2);
htotal_data->GetYaxis()->SetRangeUser(0.,2.0);
//htotal_data->GetXaxis()->SetRangeUser(100.,1500.0);
htotal_data->GetXaxis()->SetTitle(" ");
htotal_data->GetYaxis()->SetTitle("#frac{Data}{Prediction}");
htotal_data->GetXaxis()->SetLabelFont(42);

htotal_data->GetXaxis()->SetLabelOffset(0.03);
htotal_data->GetXaxis()->SetTitleSize(0.14);
htotal_data->GetXaxis()->SetTitleOffset(1.1);
htotal_data->GetXaxis()->SetLabelSize(0.12);
htotal_data->GetXaxis()->SetTitle("m(#mu,#tau_{h},E_{T}^{miss}) [GeV]");
htotal_data->GetYaxis()->CenterTitle(true);

   TLine *line = new TLine(100, 1,4000, 1);
   line->SetLineColor(kRed);
   line->Draw();


        // ------------>Primitives in pad: pad2
   c1->cd();
   pad2 = new TPad("pad2", "pad2",0.0,0.33,1,0.99);
   pad2->SetTickx();
   pad2->SetTicky();
   pad2->Draw();
   pad2->cd();
   pad2->Range(61.49425,-1.836137,167.8161,16.52523);
   pad2->SetFillColor(0);
   pad2->SetBorderMode(-1);
   pad2->SetBorderSize(5);
   pad2->SetLeftMargin(0.12);
   pad2->SetRightMargin(0.04);
   pad2->SetTopMargin(0.08);
   pad2->SetBottomMargin(0.0001);
   pad2->SetFrameBorderMode(0);
   pad2->SetFrameBorderMode(0);

   pad2->SetLogy();

   //pad2 = new TPad("pad2", "pad2",0.01,0.33,0.99,0.99);
   //pad2->Draw();
   //pad2->cd();
   //pad2->Range(-44.421,-161.3852,528.7119,36963.49);
   //pad2->SetFillColor(0);
   //pad2->SetBorderMode(0);
   //pad2->SetBorderSize(2);
   //pad2->SetLogy();

   //pad2->SetGridx();
   //pad2->SetLeftMargin(0.0775056);
   //pad2->SetRightMargin(0.05009633);
   //pad2->SetBottomMargin(0.004347092);
   //pad2->SetFrameBorderMode(0);
   //pad2->SetFrameBorderMode(0);

hs->Draw("hist");
hsig1->Draw("ep,same");
hdata_rebin->Draw("ep,same");
hsig2->Draw("ep,same");
//hsig3->Draw("ep,same");
//hsig4->Draw("ep,same");
    for(int i=1; i<13; i++)
	{
	hdiv1_error->SetBinContent(i,1);
	double deno_err = h[0]->GetBinContent(i) + h[1]->GetBinContent(i)  + h[2]->GetBinContent(i) ;
	double value = sqrt((pow(h[0]->GetBinError(i),2))+ (pow(h[1]->GetBinError(i),2)) + (pow(h[2]->GetBinError(i),2)));
	double total_err = sqrt(pow(sys,2) + pow(JEC[i], 2) + pow(wfake[i],2)) + value;
//std::cout<<i<<'\t'<<total_err<<'\t'<<value/deno_err<<std::endl;
	hstat->SetBinError(i,total_err);
	}

hstat->Draw("E2,same");
//hstat->SetLineWidth(1);
   hstat->SetFillColor(ci);
   hstat->SetFillStyle(3004);
hs->SetMinimum(0.50);
hs->SetMaximum(2000);
   hs->GetXaxis()->SetRange(1,12);
   hs->GetXaxis()->SetLabelFont(42);
   hs->GetXaxis()->SetLabelOffset(0.007);
   hs->GetXaxis()->SetLabelSize(0.035);
   hs->GetXaxis()->SetTitleSize(0.12);
   hs->GetXaxis()->SetTitleOffset(0.9);
   hs->GetXaxis()->SetTitleFont(42);
   hs->GetYaxis()->SetTitle("Events");

   hs->GetYaxis()->SetLabelFont(42);
   hs->GetYaxis()->SetLabelOffset(0.007);
   hs->GetYaxis()->SetTitleOffset(0.8);
   hs->GetYaxis()->SetLabelSize(0.06);
   hs->GetYaxis()->SetTitleSize(0.065);
   hs->GetYaxis()->SetTitleFont(42);

c1->Update();
c1->Modified();

        double y_legend = 3800;
        double x_legend = 300;
        TLatex *   tex = new TLatex(x_legend,y_legend,"CMS");
//      TLatex *   tex = new TLatex(105,400,"CMS");
     	tex->SetTextAlign(20);
   	tex->SetTextSize(0.09);
  	 tex->SetLineWidth(2);
        tex->Draw();
        TLatex *   tex1 = new TLatex(x_legend+520,y_legend,"#it{#bf{Internal}}");
   	tex1->SetTextAlign(20);
   	tex1->SetTextSize(0.06);

   	tex1->SetLineWidth(2);
   	tex1->Draw();

        double x_pos1 = x_legend + 3200;
        TLatex * tex2 = new TLatex(x_pos1,y_legend,"27.4 fb^{-1} (13 TeV)");
        tex2->SetTextAlign(20);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.06);
        tex2->SetLineWidth(2);
        tex2->Draw();

TLegend *legend=new TLegend(0.33,0.55,0.95,0.88);
	//legend->SetHeader("NRecoJet1");
	legend->SetNColumns(2);
        legend->SetTextSize(0.05);
	legend->AddEntry(hdata_rebin,"Data","lep");
	legend->AddEntry(hsig1,"VBF Z' #rightarrow #tau#tau (1.5 TeV)","l");

        legend->AddEntry(h[0],"Fake #tau_{h}","f");
	legend->AddEntry(hsig2,"VBF Z' #rightarrow WW (1.5 TeV)","l");

        legend->AddEntry(h[1],"t#bar{t}","f");

	legend->AddEntry(hstat,"Uncertainty","fp");
	legend->AddEntry(h[2],"Other prompt","f");
//	legend->AddEntry(hsig1,"VBF Z' #rightarrow #tau#tau (M1000)","lep");
//  	legend->AddEntry(hsig4,"VBF Z' #rightarrow WW (M1250)","lep");
	
	legend->Draw();

//c1->SaveAs("bkg_mutau_2018.root");
//c1->SaveAs("bkg_mutau_2018.pdf");
	}
