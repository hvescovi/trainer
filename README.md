# Trainer (inTeRActive Images sequeNcER)

## Getting started

* Take screenshot of each screen you want to show or explain, with notes about something on the screen
  * run shooter.py
* Adjust each screen positioning the box message and resizing it
  * run designer_backend.py
  * open index.html on a web server. I ran docker in that way: docker run -p 80:80 -d -v /home/friend/01-github/trainer:/usr/share/nginx/html nginx

Each line of the file sequence.txt (separated by "|") contains:
* image name
* message
* coordinates (x and y) of box message
* coordinates (x and y) of the navigation bar (previous and next)
* size of the box message (height and width)

References:
  * https://datatofish.com/screenshot-python