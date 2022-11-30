{

TCanvas *c1 = new TCanvas("c1", "stacked hists",61,24,1305,744);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetLogy();
   c1->SetGridx();


//Double_t bins[16] = {100,120,135,150,180,210,240,270,300,350,400,450,500,550,600,1500};

//Double_t bins[17] = {100,120,135,150,180,210,240,270,300,350,400,450,500,550,600,850,1500};

//Double_t bins[18] = {100,120,135,150,180,210,240,270,300,350,400,450,500,550,600,700,850,1500};

Double_t bins[19] = {100,120,135,150,180,210,240,270,300,350,400,450,500,550,600,700,850,1000,1500};
TH1 *h1[10], *h2[10], *hnew ;

std::vector<std::string>sample;
std::string str;
std::ifstream in("bkg_list.txt");
while (std::getline(in, str))
{
if(str.size() > 0)
        sample.push_back(str);
}

TFile *file[10];
for(int i=0; i < 10; i++){
char nl[256];
sprintf(nl,"%s",sample.at(i).c_str());
std::string fstr = sample.at(i).c_str();
file[i] = new TFile(nl);

file[i]->GetObject("h1",h2[i]);
//file[i]->GetObject("NRecoBJet/Muon1Electron1ReconstructableMass",h2[i]);


TH1F *hnew = (TH1F*)h2[i]->Rebin(18,"hnew",bins);




	hnew->Draw("lep");

   hnew->SetTitle("");


       hnew->SetStats(kFALSE);
//        hs->SetFillColor(30);
  //      hs->SetLineColor(30);
	hnew->GetXaxis()->SetLabelFont(42);
   hnew->GetYaxis()->SetLabelSize(0.035);
   hnew->GetXaxis()->SetTitleSize(0.035);
   hnew->GetXaxis()->SetTitleFont(42);
   hnew->GetYaxis()->SetLabelFont(42);
   hnew->GetYaxis()->SetTitleSize(0.04);
   hnew->GetYaxis()->SetTitleFont(42);
   hnew->GetYaxis()->SetTitle("Events");

   hnew->GetYaxis()->SetTitleOffset(0.9);
//   h1->GetXaxis()->SetRangeUser(100,1000); 

hnew->GetXaxis()->SetTitle("M_{#mu#tau_{h},MET} [GeV]");
  hnew->SetMarkerColor(kMagenta+2);
  hnew->SetLineColor(kMagenta+2);	
  hnew->SetMarkerSize(0.5); 


std::string delimiter = "." ;
std::string token = fstr.substr(0, fstr.find(delimiter));
TFile *filefinal = new TFile(TString(token) + "_emu_2016.root","RECREATE");
filefinal->cd();
hnew->SetName("h1");
hnew->Write("h1",TObject::kWriteDelete);
//check->Write();
filefinal->Close();

//c1->SaveAs("stack_plots_hadW/Muon1Tau1ReconstructableMass.C");
//c1->SaveAs("stack_plots_hadW/Muon1Tau1ReconstructableMass.pdf");
//c1->SaveAs("Muon1Tau1ReconstructableMass.pdf");
//c1->SaveAs("stack_plots/Muon1Tau1ReconstructableMass.eps");
//c1->SaveAs("stack_plots/Muon1Tau1ReconstructableMass.root");

  double y_legend = hnew->GetMaximum() + 1500;
        double x_legend = 150;
        TLatex *   tex = new TLatex(x_legend,y_legend,"CMS");
     tex->SetTextAlign(20);
   tex->SetTextSize(0.0552915);
   tex->SetLineWidth(2);
        tex->Draw();
        TLatex *   tex1 = new TLatex(x_legend+140,y_legend,"#it{#bf{Preliminary}}");
   tex1->SetTextAlign(20);
   tex1->SetTextSize(0.03642526);

   tex1->SetLineWidth(2);
   tex1->Draw();
        double x_pos1 = 1320;
        TLatex * tex2 = new TLatex(x_pos1,y_legend,"2016, 35.9 fb^{-1} (13 TeV)");
        tex2->SetTextAlign(20);
        tex2->SetTextFont(42);
        tex2->SetTextSize(0.0372915);
        tex2->SetLineWidth(2);
        tex2->Draw();
}

	}
	
	



