<h2>Ciao Restaurant website with Django</h2>

<h4>Description</h4>
This is a simple restaurant website with booking system which has connected to MySQL database. Customers can make reservation by choosing date, time and how many person 
together with their contact information with mobile and e-post which are mandatory. There is a optional field for special request. 
Each booking submit will be confirmed and showed on a new page. And the webiste has also a simple map showing the location of the restaurant. 

<h4>Relevant Frameworks/Modules/Plugins</h4>
<ul>
  <li>Django 2.1.4</li>
  <li>Boostraps 4</li>
  <li>Leaflet JS</li>
  <li>Mapbox</li>
  <li>MySQL Workbrench</li>
</ul> 

<h4>Set up</h4>
<ol>
  <li>Create virtual environment up an running.</li>
  <li>Install dependencies <br> 
    ```
    pip install -r requirements.txt
    ```</li>
  <li>I used MySQL Workbrench. You will need to make changes to the setting.py file according to your database setting.</li>
  <li>You can create superuser for admin page.</li>
  <li>I have also a timezone setting to "CET" in setting.py</li>
  <li>Migrate the database  <br> `python manage.py migrate`</li>
  </ol> 
