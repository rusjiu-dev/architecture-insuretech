
kubectl get hpa scaletestapp-hpa -w
NAME               REFERENCE                 TARGETS           MINPODS   MAXPODS   REPLICAS   AGE
scaletestapp-hpa   Deployment/scaletestapp   memory: 23%/80%   1         10        1          32m
scaletestapp-hpa   Deployment/scaletestapp   memory: 23%/80%   1         10        1          32m
scaletestapp-hpa   Deployment/scaletestapp   memory: 76%/80%   1         10        1          32m
scaletestapp-hpa   Deployment/scaletestapp   memory: 93%/80%   1         10        1          33m
scaletestapp-hpa   Deployment/scaletestapp   memory: 50%/80%   1         10        2          33m
scaletestapp-hpa   Deployment/scaletestapp   memory: 46%/80%   1         10        2          33m

kubectl get events

7m49s       Normal    SuccessfulRescale              horizontalpodautoscaler/scaletestapp-hpa   New size: 1; reason: All metrics below target
94s         Normal    SuccessfulRescale              horizontalpodautoscaler/scaletestapp-hpa   New size: 2; reason: memory resource utilization (percentage of request) above target

kubectl get pods -l app=scaletestapp -w
NAME                            READY   STATUS    RESTARTS        AGE
scaletestapp-65df4db597-v9hjk   1/1     Running   1 (4m37s ago)   8m45s
scaletestapp-65df4db597-4b2pq   0/1     Pending   0               0s
scaletestapp-65df4db597-4b2pq   0/1     Pending   0               0s
scaletestapp-65df4db597-4b2pq   0/1     ContainerCreating   0               0s
scaletestapp-65df4db597-4b2pq   0/1     Running             0               3s
scaletestapp-65df4db597-4b2pq   1/1     Running             0               9s
scaletestapp-65df4db597-4b2pq   1/1     Running             0               9s