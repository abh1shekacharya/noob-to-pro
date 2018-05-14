# Week-2 : Basic Shell scripting ( Sed and Awk )

**( Timeline : 14<sup>th</sup> May'18 - 19<sup>th</sup> May'18 )**
 
 **All the below actions are to be performed on given access.log file**

|#| Task		| Points	|	Format To Submit	|
|--| ------------- 	| -------------	|	-------------------		|
|1| Find the useragent and print the whole line if it is not a Chrome browser  | 50  |	C	|
|2| Print all the "POST" requests only  | 50  |	C	|
|3| Make a csv file with fields as : #, ip_addr,date_accessed,endpoint_accessed, useragent.Only print logs with status code as 404.<sup>1</sup>  | 150  |	C	|
|4| Repeat the 3rd task but only for lines 20-33  | 50  |	C	|
|5| Repeat task 3, just replace the Chrome useragent with GoogleBot's useragent.<sup>2</sup>  | 50  |	C	|
|6| Print only logs for the time period between 12:00:00 to 14:52:50 ( 13th May ) ( cause the administrator suspects, the attack occurred during that time interval ;) )  | 50  |	C	|
|7| Programmatically calculate ( using awk ) the no. of lines printed  | 50  |		C	|
|8| Print the size of the object requested ( check apache log format to get the correct field )  | 50  |		C	|
|9| Find the total requested object size on 12 May between 8:00 am to 9:00 am	| 50	| C	|
|| **TOTAL** 	| **550**	|


1 : 

**Sample Output ( for csv file )**
![Sample output of csv file](https://user-images.githubusercontent.com/17861054/39969781-f97739b6-56fe-11e8-91d5-1ea45ef9ddf3.png)

2 : Find google bot's useragent from the web



Index	|	|
--------|-------|
C	| Code	|
S	| Screenshot	|
G/V	| Gif/Video	|


### Note :

1. Output of each code should be attached or screenshot.
2. A few more tasks may be added later.
3. Download the access.log [here](https://github.com/M1doriya/noob-to-pro/files/1998729/access.log)



### enjoy hacking :)
### try harder
