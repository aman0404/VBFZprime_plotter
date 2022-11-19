#include "TH1.h"
#include "TH1F.h"
#include<iostream>
#include<TFile.h>
#include<TH1F.h>
#include<TH2F.h>
#include<TCanvas.h>
#include<TStyle.h>
#include<TF1.h>
#include<TF2.h>
#include<TGaxis.h>
#include<TTree.h>
#include<TMath.h>
#include<fstream>
#include<TChain.h>
{



//Double_t bins[13] = {100,150,200,250,300,350,400,450,500,550,650,850, 1500};
Double_t bins[11] = {100,150,200,250,300,350,400,500,650,850, 1500};

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

file[i]->GetObject("NRecoBJet/DiTauReconstructableMass",h2[i]);


TH1F *hnew = (TH1F*)h2[i]->Rebin(10,"hnew",bins);
for(int j = 1; j < 13 ;j++){ 
double yield = hnew->GetBinContent(j);

char name1[256];
std::string n[5] = {"wj", "dy","tt","st","vv"};
//std::cout<<n[i]<<std::endl;
sprintf(name1,"%s",n[i].c_str());
std::string delimiter = "." ;
std::string token = fstr.substr(0, fstr.find(delimiter));
//std::cout<<token<<std::endl;
std::ofstream log1(token+"_binyield.txt",std::ios_base::app|std::ios_base::out);
log1<<j<<" "<<yield<<std::endl;
log1.close();
}
}

}






