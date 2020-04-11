<?php 
Header("Content-type: image/png"); 
$picWidth=360*2; 
$picHeight=200; 
$pic=ImageCreate($picWidth+1,$picHeight+1); 
$cWhite=ImageColorAllocate($pic,255,255,255); 
ImageFilledRectangle($pic,0,0,$picWidth+1,$picHeight+1,$cWhite); 
$cRed=ImageColorAllocate($pic,255,0,0); 
$cBlue=ImageColorAllocate($pic,0,0,255); 
$curX=0; 
$curY=$picHeight; 
for($pt=0;$pt<$picWidth;$pt++){ 
$newX=$curX+1; 
$newY=($picHeight/2)+(cos(deg2rad($newX))*($picHeight/2)); 
ImageLine($pic,$curX,$curY,$newX,$newY,$cRed); 
$curX=$newX; 
$curY=$newY; 
} 
$curX=0; 
$curY=$picHeight/2; 
for($pt=0;$pt<$picWidth;$pt++){ 
$newX=$curX+1; 
$newY=($picHeight/2)+(sin(deg2rad($newX))*($picHeight/2)); 
ImageLine($pic,$curX,$curY,$newX,$newY,$cBlue); 
$curX=$newX; 
$curY=$newY; 
} 
$cBlack=ImageColorAllocate($pic,0,0,0); 
ImageLine($pic,0,0,0,$picHeight,$cBlack); 
ImageLine($pic,0,$picHeight/2,$picWidth,$picHeight/2,$cBlack); 
ImagePNG($pic); 
ImageDestroy($pic); 
?> 