- Procedure to Build docker container and run python program
1) git clone
```bash
git clone https://github.com/varunreddy1234/getVendor.git
```
2) Build Dockerfile
```bash
cd getVendor
docker build -t getVendor:public .
```

3) Run container
```bash
docker run -it <image id>
```
4) Run python program from container with mac address as given parameter to python script

```bash
python getVendor.py <MAC ADDRESS>
