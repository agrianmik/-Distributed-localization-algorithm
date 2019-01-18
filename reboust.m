function check= reboust(a,b,c)
 
%set the threshold to be 45 
reboust_thresh=45;
 
%determine the side having the minimum distance
if (a<=b && a<=c)
    minvalue=a;  d=b; e=c;
elseif (b<=a && b<=c)
    minvalue=b; d=a; e=c;
else
    minvalue=c; d=a; e=b;
end
 
%check with the minimum distance 
costh=((d)^2+(e)^2-(minvalue)^2)/(2*d*e);
 
%if it is not reboust then return 0
%if it is reboust then return 1
 
if (minvalue*(1-(costh)^2) < reboust_thresh)
    
    check=0;
else 
    check=1;
    
end
 
 
end
