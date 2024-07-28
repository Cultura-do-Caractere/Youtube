GitOps com FluxCD

Instale o FluxCD no seu Laptop

```
brew install fluxcd/tap/flux # para macos

curl -s https://fluxcd.io/install.sh | sudo bash  # Linux

choco install flux # Windows
```

```
  export GITHUB_TOKEN=seu_token_aqui
```

Faça o bootstrap com o Image Automation component e a deploy key como read/write
```
flux bootstrap github \
  --owner=Cultura-do-Caractere \
  --repository=Youtube \
  --branch=main \
  --path=./video7/cluster \
  --read-write-key \
  --personal   \
  --components-extra image-reflector-controller,image-automation-controller
```

Crie um Kustomization apontando para os seus Manifests do Kubernetes
```
flux create kustomization go-app2 \
  --target-namespace=cdc-dev \
  --source=flux-system \
  --path="./video7/environments/dev/go-app" \
  --prune=true \
  --wait=true \
  --interval=30m \
  --retry-interval=2m \
  --health-check-timeout=3m \
  --export > ./video7/cluster/go-app2.yaml
```
