# Installing LLVM from source
We will be following the document https://llvm.org/docs/GettingStarted.html#getting-started-with-llvm for installing LLVM from source

### Downloading source code
```
$ git clone --depth 1 https://github.com/llvm/llvm-project.git
```
This would download the source code of latest revision of LLVM

### Building
1. ```$ cd llvm-project ```
2. ```$ cmake -S llvm -B build -DBUILD_SHARED_LIBS=on -DCMAKE_BUILD_TYPE=Release ```
3. ```$ cd build ```
4. ```$ cmake --build . ```
5. ``` $cmake --build . --target install ```

After this, you can see llvm executables in ```llvm-project/build/bin/``` folder.

While installing TVM, provide the ```/path/to/llvm-project/build/bin/llvm-config```
