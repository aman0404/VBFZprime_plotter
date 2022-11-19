{

TCanvas *c1 = new TCanvas("c1", "stacked hists",61,24,1305,744);
   c1->Range(0,0,1,1);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetLogy();
   c1->SetGridx();
TH1 *hRegion1, *hRegion2, *hRegion3, *hRegion4, *hRegion5, *hRegion6, *hRegion7, *hRegion8, *hRegion0, *hRegion9, *hRegion10;



	TFile *f2 = TFile::Open("W+Jets.root");
	f2->GetObject("NRecoBJet/DiTauReconstructableMass",hRegion2);


//	Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 1500};
//	Double_t bins[12] = {100,150,200,250,300,350,400,450,500,650,850, 1500};
	Double_t bins[11] = {100,150,200,250,300,350,400,500,650,850, 1500};  
     TH1F *h1 = (TH1F*)hRegion2->Rebin(10,"h1",bins);

	h1->Draw("lep");

   h1->SetTitle("");


       h1->SetStats(kFALSE);
//        hs->SetFillColor(30);
  //      hs->SetLineColor(30);
	h1->GetXaxis()->SetLabelFont(42);
   h1->GetYaxis()->SetLabelSize(0.035);
   h1->GetXaxis()->SetTitleSize(0.035);
   h1->GetXaxis()->SetTitleFont(42);
   h1->GetYaxis()->SetLabelFont(42);
   h1->GetYaxis()->SetTitleSize(0.04);
   h1->GetYaxis()->SetTitleFont(42);
   h1->GetYaxis()->SetTitle("Events");

   h1->GetYaxis()->SetTitleOffset(0.9);
//   h1->GetXaxis()->SetRangeUser(100,1000); 

h1->GetXaxis()->SetTitle("M_{#mu#tau_{h},MET} [GeV]");
  h1->SetMarkerColor(kMagenta+2);
  h1->SetLineColor(kMagenta+2);	
  h1->SetMarkerSize(0.5); 



TFile *file1 = new TFile("W_ditau_2016.root","RECREATE");
file1->cd();
//h1->SetName("faketau_mutau");
//h1->Write("faketau_mutau",TObject::kWriteDelete);
//check->Write();
h1->Write();
file1->Close();


//c1->SaveAs("stack_plots_hadW/Muon1Tau1ReconstructableMass.C");
//c1->SaveAs("stack_plots_hadW/Muon1Tau1ReconstructableMass.pdf");
//c1->SaveAs("Muon1Tau1ReconstructableMass.pdf");
//c1->SaveAs("stack_plots/Muon1Tau1ReconstructableMass.eps");
//c1->SaveAs("stack_plots/Muon1Tau1ReconstructableMass.root");

  double y_legend = h1->GetMaximum() + 1500;
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
	
	



