# FluxCD and Data Migrations


### Comandos usados:

```
flux get kustomizations  --watch 
```

```
flux tree kustomization python-app-pre-deploy
```

```
kubectl logs -f job/db-migration -n python-app-ns
```

```
kubectl get pods -n python-app-ns --watch
```

```
alembic revision --autogenerate -m "adding column last_name"
```