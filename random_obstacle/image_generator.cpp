#include <bits/stdc++.h>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/core/core.hpp"
#include <iostream>
#include <math.h>
#include <string.h>


using namespace std;
using namespace cv;

#define NUMBER 5
#define SIZE_X 1000
#define SIZE_Y 1000

Mat A;



int Drawing_Random_Rectangles( Mat image, char* window_name, RNG rng )
{
  int lineType = 8;
  Point pt1, pt2;
  Point all_point1[NUMBER];
  Point all_point2[NUMBER];
  int m=1;


  int x_1=1;
  int x_2=SIZE_X;
  int y_1=1;
  int y_2=SIZE_Y;
  //int k=1000/NUMBER;

  int r=0;

  Mat temp;



  for( int i = 0; i < NUMBER; i++ )
  { 
    temp=Mat(SIZE_X,SIZE_Y,CV_8UC3,Scalar(255,255,255));;
    m=1;
   pt1.x = rng.uniform( x_1, x_2);
   pt1.y = rng.uniform( y_1, y_2);
   pt2.x = rng.uniform( x_1, x_2);
   pt2.y = rng.uniform( y_1, y_2);


   
   rectangle(temp,pt1,pt2, cv::Scalar(0, 0, 0),CV_FILLED);

   for (int p = 0; p < SIZE_X; ++p)
   {
    for (int q = 0; q < SIZE_Y; ++q)
    {
      if(temp.at<Vec3b>(p,q)[0]==0 && image.at<Vec3b>(p,q)[0]==0 && temp.at<Vec3b>(p,q)[1]==0 && image.at<Vec3b>(p,q)[1]==0 && temp.at<Vec3b>(p,q)[2]==0 && image.at<Vec3b>(p,q)[2]==0 )
        {
          m=0;
          break;
          break;
        }
      }

    }

  if(m==0)
  {
    i--;
    continue;
  }
    else
      {
        rectangle(image,pt1,pt2, cv::Scalar(0, 0, 0),CV_FILLED);
      }




  all_point1[i]=pt1;
  all_point2[i]=pt2;



   imshow( window_name, image );

  }

  ofstream myfile ("End_points.txt");
  if (myfile.is_open())
  {

    for (int i = 0; i < NUMBER; ++i)
    {
      myfile<<all_point1[i].x<<" "<<all_point1[i].y<<" "<<all_point2[i].x<<" "<<all_point2[i].y<<"\n";
    }
  }
  else cout << "Unable to open file";

  waitKey(0);
  return 0;
}




int main()
{
  
   
    
    int seed;
    cin>>seed;
    RNG rng( seed );

    A=Mat(SIZE_X,SIZE_Y,CV_8UC3,Scalar(255,255,255));
    imshow( "Output", A);


    int c = Drawing_Random_Rectangles(A, "Output", rng);
  return 0;

}