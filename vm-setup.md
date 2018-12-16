# cs410

### start jupyter notebook in gcp vm
nohup jupyter notebook --ip=0.0.0.0 --allow-root &

### run a container with notebook
```
docker run -d --privileged -w /home/gemeng -it -p 8888:8888 -p 5001:5001 -v <volumn_mount_mapping> hamelsmu/ml-cpu bash
```

### setup python
```
bash setup.sh
```
