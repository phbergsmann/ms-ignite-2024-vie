# Demo for Microsoft IGNITE 2024



## Setup & Prerequisits

### Cluster

- Azure Red Hat OpenShift (ARO) Cluster
- Pull secret from your Red Hat account
  - Add it in the Azure Portal when you are creating the cluster
  - Or [Add or update your Red Hat pull secret on an Azure Red Hat OpenShift 4 cluster](https://learn.microsoft.com/en-us/azure/openshift/howto-add-update-pull-secret)
  
### Azure OpenAI Models

Tested with `gpt-35-turbo` and `text-embedding-ada-002`.

Name of models in the code (can be changed, of course):
- `gpt-35-turbo`
- `text-embedding-3-small`

### Environment variables

Add them in your ARO cluster

- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`

### Demo run

![](./assets/demo1.png)
