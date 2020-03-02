#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main( int argc, char ** argv ){
	if( argc!=2 ){
		cerr << "Incorrect number of arguments used. Please instead use:\n"
			<< "\t./code [Input Resolutions]\n";
		return -1;
	}

	string PMTs[5] = {"R7724","R7724","ET9214","ET9214","R7724"};
	int LENGTHs[5] = {160,200,50,50,200};
	int BARS_PER_SECT[6][5] = {{3,7,6,6,2},{3,7,6,6,2},{3,7,6,6,2},{3,7,6,6,2},{3,7,5,5,0},{3,7,6,6,2}};
	

	for( int layer = 0 ; layer < 4 ; layer++ ){
		for( int sector = 0 ; sector < 4 ; sector++){
			for( int comp = 0 ; comp < BARS_PER_SECT[layer][sector] ; comp++){
				string temp = R"(\\)";
				cout << (sector+1) << "\t&" << (layer+1) << "\t&" << (comp+1) << "\t&" << LENGTHs[sector] 
					<< "\t&" << PMTs[sector] << "\t&" << "XXX" << "\t&" << "XXX" << temp <<" \n";
			
			}// end loop over component
		} // end sector loop
	} // end layer loop



	return 1;
}
