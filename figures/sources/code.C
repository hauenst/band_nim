void PrettyTGraphErrors( TGraphErrors * gP , int color , TString xTit , TString yTit , TString Tit );
// ===========================================================================================================================================
void code(){
	double temp;
	int sec, lay, com;
	ifstream f;
	// ----------------------------------------------------------------------------------------
	// Attenuation lengths
	int AL_ctr = 0;
	double attenuation[3][600] = {{0}};
	f.open("input/attenuation_lengths.txt");
	while(!f.eof()){
		f >> sec;
		f >> lay;
		f >> com;
		f >> attenuation[1][AL_ctr];
		f >> attenuation[2][AL_ctr];
		attenuation[0][AL_ctr] = (double)(100*sec + 10*lay + com);
		AL_ctr++;
	}
	AL_ctr--;
	f.close();
	
	TGraphErrors * g_attenuation = new TGraphErrors(AL_ctr,attenuation[0],attenuation[1],0,attenuation[2]);
	PrettyTGraphErrors( g_attenuation , 62 , "bar ID" , "Attenuation length [m]" , "" );

	TCanvas * c1 = new TCanvas("c1","c1",800,400);
	gPad -> SetTopMargin(0.03);
	gPad -> SetRightMargin(0.02);
	gPad -> SetLeftMargin(0.10);
	gPad -> SetBottomMargin(0.15);
	g_attenuation -> Draw("AP");

	TLatex * tex_AL = new TLatex(120,4,"PRELIMINARY");
	tex_AL -> SetTextColorAlpha(1,0.3);;
	tex_AL -> SetTextSize(0.24);
	tex_AL -> SetTextAngle(15);
	tex_AL -> Draw("same");

	c1 -> Print("attenuation.pdf");
	// ----------------------------------------------------------------------------------------
	// Effective velocity
	int EV_ctr = 0;
	double eff_velocity[3][600] = {{0}};
	f.open("input/effective_velocity.txt");
	while(!f.eof()){
                f >> sec;
                f >> lay;
                f >> com;
                f >> eff_velocity[1][EV_ctr];
                f >> temp;
		f >> eff_velocity[2][EV_ctr];
                f >> temp;
		eff_velocity[0][EV_ctr] = (double)(100*sec + 10*lay + com);
                EV_ctr++;
        }
        EV_ctr--;
        f.close();

	TGraphErrors * g_eff_velocity = new TGraphErrors(EV_ctr,eff_velocity[0],eff_velocity[1],0,eff_velocity[2]);
	PrettyTGraphErrors( g_eff_velocity , 62 , "bar ID" , "Effective velocity [cm/ns]" , "" );

	TCanvas * c2 = new TCanvas("c2","c2",800,400);
        gPad -> SetTopMargin(0.03);
        gPad -> SetRightMargin(0.02);
        gPad -> SetLeftMargin(0.10);
        gPad -> SetBottomMargin(0.15);
	g_eff_velocity -> SetMinimum(12);
	g_eff_velocity -> SetMaximum(16);
        g_eff_velocity -> Draw("AP");

	TLatex * tex_EV = new TLatex(120,13,"PRELIMINARY");
        tex_EV -> SetTextColorAlpha(1,0.3);;
        tex_EV -> SetTextSize(0.24);
        tex_EV -> SetTextAngle(15);
        tex_EV -> Draw("same");

        c2 -> Print("eff_velocity.pdf");
	// ----------------------------------------------------------------------------------------
	// Resolutions
	int Res_ctr = 0;
        double resolutions[3][600] = {{0}};
        f.open("input/resolutions.txt");
        while(!f.eof()){
                f >> sec;
                f >> lay;
                f >> com;
                f >> resolutions[1][Res_ctr];
                resolutions[0][Res_ctr] = (double)(100*sec + 10*lay + com);
                Res_ctr++;
        }
        Res_ctr--;
        f.close();

        TGraphErrors * g_resolutions = new TGraphErrors(Res_ctr,resolutions[0],resolutions[1],0,resolutions[2]);
        PrettyTGraphErrors( g_resolutions , 62 , "bar ID" , "Resolution/#sqrt{2} [ps]" , "" );

        TCanvas * c3 = new TCanvas("c3","c3",800,400);
        gPad -> SetTopMargin(0.03);
        gPad -> SetRightMargin(0.02);
        gPad -> SetLeftMargin(0.10);
        gPad -> SetBottomMargin(0.15);
        g_resolutions -> SetMinimum(150);
        g_resolutions -> SetMaximum(400);
        g_resolutions -> Draw("AP");

        TLatex * tex_RE = new TLatex(120,180,"PRELIMINARY");
        tex_RE -> SetTextColorAlpha(1,0.3);;
        tex_RE -> SetTextSize(0.24);
        tex_RE -> SetTextAngle(15);
        tex_RE -> Draw("same");

        c3 -> Print("resolutions.pdf");
        // ----------------------------------------------------------------------------------------
}
// ===========================================================================================================================================
void PrettyTGraphErrors( TGraphErrors * gP , int color , TString xTit , TString yTit , TString Tit ){
	gP -> GetXaxis() -> CenterTitle();
	gP -> GetYaxis() -> CenterTitle();
	gP -> GetXaxis() -> SetNdivisions(107);
	gP -> GetYaxis() -> SetNdivisions(107);
	gP -> GetXaxis() -> SetTitleSize(0.07);
	gP -> GetYaxis() -> SetTitleSize(0.07);
	gP -> GetXaxis() -> SetLabelSize(0.07);
        gP -> GetYaxis() -> SetLabelSize(0.07);
	gP -> GetXaxis() -> SetTitleOffset(1.0);
	gP -> GetYaxis() -> SetTitleOffset(0.7);

	gP -> SetMarkerStyle(20);
	gP -> SetMarkerColor(color);
	
	gP -> GetXaxis() -> SetTitle(xTit);
	gP -> GetYaxis() -> SetTitle(yTit);
	gP -> SetTitle(Tit); 
}
