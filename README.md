<h1>RAM monitoring Api system</h1>
the code uses these libraries and frameworks to achieve this:
<ul>
<li><b>Psutil:</b> to get the data from the machine, highly compatible with various operating systems but does need to be installed (use the requirements.cmd to install)</li>
<li><b>FastApi:</b> to make the API (same as above, need to have it installed with requirements.cmd)</li>
<li><b>Time:</b> to get the timestamp epoch and set delays of 60 seconds between each read</li>
<li><b>SQlite3:</b> to store the data and recover once needed</li>
</ul>

use the <b>record.py</b> to make the database or add more data to it

use the <b>Start.cmd</b> to initiate the API
