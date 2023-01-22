
![Time Back Machine Logopng](https://user-images.githubusercontent.com/52424334/213900240-dadb923e-6534-4759-9ce6-be73d83f4bcb.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
This is a code repository for an app that takes the top 100 musics of a certain day and create a playlist on spotify based on that.

<h3>Requirements</h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
In order to locally use this program, you must install the libraries requirements using the following command: 

```bash
 pip install -r requirements.txt
```
    
<h3>Environment Variables</h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
This project requires a Spotify account and a custom Spotify's application that can be done following a guide inside the program; this information can be added inside the GUI or directly into the JSON file by changing the following libraries.

`client_id` = "ID"

`client_secret` = "secret"

`website_url` = "website"

<h3>Expected Output</h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Once the code is initialized, a window will open showing a calendar widget

<img src="https://user-images.githubusercontent.com/52424334/213900302-1516bd72-631c-4a9b-8377-0df768419749.png" width="500">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Once a date is selected, a pop-up window will appear to request Spotify's application details; once provided with this information, the next time the user clicks a date, a Spotify authorization window will appear on the browser; after accepting the terms, the user must copy the link of the webpage and paste on the terminal in other to generate the token. This process only needs to be done once.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
After all that, the program will start to web-scrape billboard to 100 songs on that specific date:

<img src="https://user-images.githubusercontent.com/52424334/213900515-bc027fe5-03cc-4e0e-b47f-6258c12594cc.png" width="500">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Once the project is done, if everything works out, you will have a playlist on your Spotify account

<img src="https://user-images.githubusercontent.com/52424334/213900553-32c0fdf4-f0ed-40b5-afad-97fdfb159f44.png" width="300" align="left">
<img src="https://user-images.githubusercontent.com/52424334/213900559-779c0fba-0cef-44a6-b6f1-f51f529f23bb.png" width="300" align="left">
