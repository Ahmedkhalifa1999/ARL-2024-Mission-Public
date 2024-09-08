# Description

## Debugging the docker image

When trying to build the cpp project using the provided `Dockerfile`, you encounter an error. Your task is to debug this error and fix it. Document the error you encountered and the steps you took to fix it, and provide resources that helped you in the debugging process. (BONUS: fix the error in the provided `Dockerfile`)

## Debugging the code

After successfully building the project, you run the binary and encounter a logical error in the implementation of the DFS traversal. The program is not returning the correct closest value to the target value. Your task is to debug this error and fix it. Document the error you encountered and the steps you took to fix it, and provide resources that helped you in the debugging process.


# To Install Docker

## Windows

Run `debugging_assignment.bat` and follow its steps

## Linux

1. Update the apt package index and install packages

```bash
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

2. Add Docker’s official GPG key

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

3. Set up the stable repository

```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

4. Install Docker CE

```bash
sudo apt-get update
sudo apt-get install docker-ce
```

5. Verify that Docker CE is installed correctly by running the hello-world image

```bash
sudo docker run hello-world
```

**Note:** You will have to use `sudo` to the Docker commands.

# To build the Docker image

1. Open a terminal/cmd in the root directory of the project.
2. Run the following command to build the Docker image

```bash
docker build -t debug_image .
```

# To run the Docker container

1. Go to the root directory of the project
2. Open a terminal/cmd in the root directory of the project.
3. Run the following command to run the Docker container

```bash
docker run -it -v ./src:/home/user/ debug_image
```

# To build the cpp file

1. Build and Run the Dockerfile
2. Run the following command to build the cpp file

```bash
cmake .
make
```

# To run the cpp file

1. Run the following command to run the cpp file

```bash
./debugging_code
```

# Hints

1. You can debug the cpp file outside the Docker container, the file will update automatically inside the container when you run the image.
2. After applying changes inside the Docker container, you can save the changes by running the following command

#### Exit the container

```bash
exit
```

#### Get container ID

```bash
docker ps -l
```

#### Commit the changes

```bash
docker commit <container_id> debug_image
```
`<container_id>` is the id you got from the previous step 

When you run the image again, the changes will be saved. This will be helpful when you want to save the changes you made inside the container while debugging.


# Extra Notes
## Binary Tree
A binary search tree is a data structure that is used to store data in a way that allows for fast search, insert, and delete operations. A binary search tree is a binary tree in which each node has a value, a left child, and a right child. The left child of a node has a value that is less than the value of the node, and the right child of a node has a value that is greater than the value of the node. The binary search tree property ensures that the values in the tree are ordered, which allows for efficient search operations.

## Depth-First Search
To find the closest value in a binary search tree to a given target value, we can perform a depth-first search (DFS) traversal of the tree. During the traversal, we can keep track of the closest value encountered so far and update it whenever we find a closer value. We can start the traversal at the root of the tree and recursively visit the left or right child of each node based on the value of the target and the value of the current node.
