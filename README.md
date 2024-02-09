# tvm_work

## TVM Installation From Source
We will be following the document https://tvm.apache.org/docs/install/from_source.html for installing TVM from source
### Download the source code
Download TVM source code from https://tvm.apache.org/download
1. ```$ tar xvf apache-tvm-src-v0.13.0.tar.gz ```
2. ```$ mv apache-tvm-src-v0.13.0.tar.gz tvm ```

### Install Pre-Requirements
1. ```$ sudo apt-get update ```
2. ```$ sudo apt-get install -y python3 python3-dev python3-setuptools gcc libtinfo-dev zlib1g-dev build-essential cmake libedit-dev libxml2-dev ```
3. Install python dependencies which are present at the end of the document.
3. ```$ pip3 install numpy decorator attrs ```
4. ```$ pip3 install typing-extensions psutil scipy ```
5. ```$ pip3 install tornado ```
6. ```$ pip3 install 'xgboost>=1.1.0' cloudpickle ```

### Building
1. ```$ cd tvm ```
2. ```$ mkdir build ```
3. ```$ cp cmake/config.cmake build```
4. ```$ cd build ```
5. Edit the config.cmake according and make sure to include the LLVM path ```/path/to/bin/llvm-config``` since TVM requires LLVM ( see the LLVM installation from source )
6. ```$ cmake .. ```
7. ```$ make -j4```

### Set enviornment variable PYTHONPATH to use tvm
1. Edit the file ```vi ~/.bashrc```
2. Add the following in the file
```
export TVM_HOME=/path/to/tvm
export PYTHONPATH=$TVM_HOME/python:${PYTHONPATH}
```
3. ```$ source ~/.bashrc```
