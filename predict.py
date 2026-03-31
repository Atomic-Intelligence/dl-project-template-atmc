import hydra


def run_inference(cfg):
    pass


@hydra.main(version_base="1.3", config_path="configs", config_name="predict")
def main(cfg):
    run_inference(cfg)


if __name__ == "__main__":
    main()
