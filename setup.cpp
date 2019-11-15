#include <iostream>

using namespace std;

void getdata();
void anotherwork();
int sum(int num1,int num2);
int sub(int num1,int num2);
int mul(int num1,int num2);
int div(int num1,int num2);
float Area_Of_Cycle(int radius);
float circumference(int radius);
void draw_foursquare(int width,int height);
int main(){
	getdata();
	return 0;
}
void getdata(){
	int method , num1 , num2, num3;
	cout << "please Enter a number:" <<endl
			<< "1.+" << endl
			<< "2.-" << endl
			<< "3.x" << endl
			<< "4./" << endl
			<< "5.Area of cycle" << endl
			<< "6.Circumference" << endl
			<< "7.Draw foursquare" << endl;
	cin >> method;
	switch(method){
		case 1:
			cout << "Enter a number:";
			cin >> num1;
			cout << "Enter another number : ";
			cin >> num2;
			cout << sum(num1,num2);
			anotherwork();
			break;
		case 2:
			cout << "Enter a number:";
			cin >> num1;
			cout << "Enter another number : ";
			cin >> num2;
			cout << sub(num1,num2);
			anotherwork();
			break;
		case 3:
			cout << "Enter a number:";
			cin >> num1;
			cout << "Enter another number : ";
			cin >> num2;
			cout << mul(num1,num2);
			anotherwork();
			break;	
		case 4:
			cout << "Enter a number:";
			cin >> num1;
			cout << "Enter another number : ";
			cin >> num2;
			cout << div(num1,num2);
			anotherwork();
			break;
		case 5:
			cout << "please enter cycle radius:";
			cin >> num1;
			cout << Area_Of_Cycle(num1);
			anotherwork();
			break;
		case 6:
			cout << "please enter cycle radius:";
			cin >> num1;
			cout << circumference(num1);
			anotherwork();
			break;	
		case 7:
			cout << "Enter width : ";
			cin >> num1;
			cout << "Enter height : ";
			cin >> num2;
			draw_foursquare(num1,num2);
			anotherwork();
			break;		
		default:
			cout << "you entered a wrong number.please try again..." << endl;
			getdata();
			break;	
	}
}
void anotherwork(){
	int anotherwork;
	cout << endl << "Hava You Another Work : " << endl
		<< "1.yes" << endl
		<< "2.no" << endl;
	cin >> anotherwork;
	switch(anotherwork){
		case 1:
			getdata();
			break;
		case 2:
			cout << "/******************************** finish ***************************************/";
			break;	
	}	
		
}
int sum(int num1,int num2){
	return num1 + num2;
}
int sub(int num1,int num2){
	return num1 - num2;
}
int mul(int num1,int num2){
	return num1 * num2;
}
int div(int num1,int num2){
	return num1 / num2;
}
float Area_Of_Cycle(int radius){
	return 3.14 * (radius * radius);
}
float circumference(int radius){
	return 2 * 3.14 * radius;
}
void draw_foursquare(int width,int height){
	for(int y = 0 ;y< height;y++){
		for(int x =0;x < width;x++){
			cout << "*";
		}
		cout << endl;
	}
}
