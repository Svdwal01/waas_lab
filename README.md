# waas_lab
Automation scripts for Barracuda Networks WAF as a Service lab and training
For Barracuda Networks WAF as a Service a quick way of generating lab applications, manipulating them and removing them

Nobody is going to roll out a class of 20 students for a lab manually. This repo contains all the Python scripts used against Barracuda WAF as a Service to quickly deploy and manipulate multiple student applications.

/WAAS Lab contains: 
- Create Lab (waas_training.py)
- Disable back-end servers (for security reasons, these are very vulnerable apps) (turn_off_server.py)
- Enable back-end servers (turn_on_server.py)
- Delete lab (waas_training_delete.py)

Soon to be added /Azure or /AWS For deploying the back-end
