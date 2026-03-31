# dl-project-template-atmc
Deep learning project template repo. Provides typical directory structure, configs and scripts.

Three main entrypoints are `train.py`, `test.py` and `predict.py` scripts, each configured via `hydra` configuration module defined in their respective `yaml` file:
`train.yaml`, `test.yaml` and `predict.yaml`.

The layout of the project is typically mirrored by the configuration layout, which provides modularity for experiemtnation and keeps a soft record of configurations used that allow for reproducibility.

```
.
├── configs
│   ├── callbacks
│   │   └── callbacks_template.yaml
│   ├── data
│   │   └── datamodule_template.yaml
│   ├── evaluation
│   │   └── evaluator_template.yaml
│   ├── model
│   │   └── model_template.yaml
│   ├── paths
│   │   └── paths_template.yaml
│   ├── predict.yaml
│   ├── tests.yaml
│   └── train.yaml
├── notebooks
├── predict.py
├── README.md
├── scripts
├── src
│   ├── callbacks
│   │   └── __init__.py
│   ├── data
│   │   └── __init__.py
│   ├── evaluation
│   │   └── __init__.py
│   ├── inference
│   │   └── __init__.py
│   ├── __init__.py
│   ├── model
│   │   └── __init__.py
│   └── utils.py
├── test.py
└── train.py
```