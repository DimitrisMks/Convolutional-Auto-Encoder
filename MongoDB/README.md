##  Prerequisites: You need to have Docker preinstalled. You can install it from https://docs.docker.com/get-docker/.
## Run MongoDB as a Docker Container
# To set up a MongoDB Docker container, we’ll use a Docker run command to deploy a MongoDB instance and also give it a container name run this in your terminal:
docker run -d -p 27017:27017 --name MONGO_CONTAINER mongo:latest

# After you download the tripadvisor data and unzip the file from here
https://1drv.ms/u/c/d73d9002b8780658/EXG-IYJbVlJEptKFrG97sEkB_Lb9GY0OxKVFfJ8MyAZLlQ?e=hyBEPX 
# run this command ( the path for the file will be different so use your own) :
docker cp "C:\Users\dimit\OneDrive\Desktop\tripadvisor_european_restaurants\tripadvisor_european_restaurants.json" MONGO_CONTAINER:/tripadvisor.json
to copy the file  in the container. 
# Acess the container
docker exec -it MONGO_CONTAINER bash
# and run 
mongoimport --db lab --collection restaurants --file /tripadvisor.json --jsonArray
# this will create the database lab and will import the collection with the documents restaurants
# Still inside the container to verify the data run the next 4 commands
mongosh

use lab

db.restaurants.countDocuments()

db.restaurants.findOne()
## Now you can work in the terminal or u can connect via python and use PyMongo API like in the notebook
